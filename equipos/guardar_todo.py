import os

from equipos.equipos_dnsmasqconf import EquiposDnsmasqconf
from equipos.equipos_hosts import EquiposHosts
from equipos.equipos_netdev import EquiposNetdev
from equipos.equipos_network import EquiposNetwork
from equipos.equipos_service import EquiposService


class GuardarTodo(object):
    """ Guardar todo """

    NETWORK_DEVICE = 'enp1s0'
    IP_ADDRESS_PREFIX = '192.168'
    IP_ADDRESS_PROFETA_N = '254'
    VLANS = ['11', '12', '13', '14', '15', '16', '17', '18']
    DNSMASQCONF_DIR = 'var/lib/dnsmasq'
    NETWORK_DIR = 'etc/systemd/network'
    SERVICE_DIR = 'usr/lib/systemd/system'

    def __init__(self, salvar, entrada):
        self.salvar = salvar
        self.entrada = entrada

    def guardar(self):
        mensajes = list()
        for vlan in self.VLANS:
            #
            # hosts
            directorio = '{0}/vlan{1}'.format(self.DNSMASQCONF_DIR, vlan)
            if not os.path.exists(directorio):
                os.makedirs(directorio)
            salida = '{0}/hosts'.format(directorio)
            equipos_hosts = EquiposHosts(self.salvar, self.entrada, vlan, salida)
            equipos_hosts.guardar()
            mensajes.append("He escrito {0}".format(salida))
            # dnsmasq.conf
            salida = '{0}/dnsmasq.conf'.format(directorio)
            equipos_hosts = EquiposDnsmasqconf(self.salvar, self.entrada, vlan, salida)
            equipos_hosts.guardar()
            mensajes.append("He escrito {0}".format(salida))
            #
            # netdev
            if not os.path.exists(self.NETWORK_DIR):
                os.makedirs(self.NETWORK_DIR)
            salida = '{0}/{1}.{2}.netdev'.format(self.NETWORK_DIR, self.NETWORK_DEVICE, vlan)
            equipos_netdev = EquiposNetdev(self.salvar, self.entrada, vlan, salida)
            equipos_netdev.guardar()
            mensajes.append("He escrito {0}".format(salida))
            # network
            salida = '{0}/{1}.{2}.network'.format(self.NETWORK_DIR, self.NETWORK_DEVICE, vlan)
            equipos_network = EquiposNetwork(self.salvar, self.entrada, vlan, salida)
            equipos_network.guardar()
            mensajes.append("He escrito {0}".format(salida))
            #
            # service
            if not os.path.exists(self.SERVICE_DIR):
                os.makedirs(self.SERVICE_DIR)
            salida = '{0}/dnsmasqvlan{1}.service'.format(self.SERVICE_DIR, vlan)
            equipos_service = EquiposService(self.salvar, self.entrada, vlan, salida)
            equipos_service.guardar()
            mensajes.append("He escrito {0}".format(salida))
        return("\n".join(mensajes))

    def __repr__(self):
        mensajes = list()
        for vlan in self.VLANS:
            equipos_hosts = EquiposHosts(self.salvar, self.entrada, vlan, 'hosts')
            mensajes.append(str(equipos_hosts))
            mensajes.append('-' * 80)
            equipos_dnsmasqconf = EquiposDnsmasqconf(self.salvar, self.entrada, vlan, 'dnsmasq.conf')
            mensajes.append(str(equipos_dnsmasqconf))
            mensajes.append('-' * 80)
            equipos_netdev = EquiposNetdev(self.salvar, self.entrada, vlan, '.netdev')
            mensajes.append(str(equipos_netdev))
            mensajes.append('-' * 80)
            equipos_network = EquiposNetwork(self.salvar, self.entrada, vlan, '.network')
            mensajes.append(str(equipos_network))
            mensajes.append('-' * 80)
            equipos_service = EquiposService(self.salvar, self.entrada, vlan, '.service')
            mensajes.append(str(equipos_service))
            mensajes.append('=' * 80)
        return("\n".join(mensajes))

