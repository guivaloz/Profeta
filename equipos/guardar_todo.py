import os

from equipos.equipos_dnsmasqconf import EquiposDnsmasqconf
from equipos.equipos_hosts import EquiposHosts
from equipos.equipos_lightsquidgroup import EquiposLightSquidGroup
from equipos.equipos_lightsquidrealname import EquiposLightSquidRealname
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
    LIGHTSQUID_DIR = 'etc/lightsquid'

    def __init__(self, salvar, entrada):
        self.salvar = salvar
        self.entrada = entrada

    def guardar(self):
        m = list()
        for vlan in self.VLANS:
            #
            # hosts
            directorio = '{0}/vlan{1}'.format(self.DNSMASQCONF_DIR, vlan)
            if not os.path.exists(directorio):
                os.makedirs(directorio)
            salida = '{0}/hosts'.format(directorio)
            equipos_hosts = EquiposHosts(self.salvar, self.entrada, vlan, salida)
            equipos_hosts.guardar()
            m.append("He escrito {0}".format(salida))
            #
            # dnsmasq.conf
            salida = '{0}/dnsmasq.conf'.format(directorio)
            equipos_hosts = EquiposDnsmasqconf(self.salvar, self.entrada, vlan, salida)
            equipos_hosts.guardar()
            m.append("He escrito {0}".format(salida))
            #
            # netdev
            if not os.path.exists(self.NETWORK_DIR):
                os.makedirs(self.NETWORK_DIR)
            salida = '{0}/{1}.{2}.netdev'.format(self.NETWORK_DIR, self.NETWORK_DEVICE, vlan)
            equipos_netdev = EquiposNetdev(self.salvar, self.entrada, vlan, salida)
            equipos_netdev.guardar()
            m.append("He escrito {0}".format(salida))
            #
            # network
            salida = '{0}/{1}.{2}.network'.format(self.NETWORK_DIR, self.NETWORK_DEVICE, vlan)
            equipos_network = EquiposNetwork(self.salvar, self.entrada, vlan, salida)
            equipos_network.guardar()
            m.append("He escrito {0}".format(salida))
            #
            # service
            if not os.path.exists(self.SERVICE_DIR):
                os.makedirs(self.SERVICE_DIR)
            salida = '{0}/dnsmasqvlan{1}.service'.format(self.SERVICE_DIR, vlan)
            equipos_service = EquiposService(self.salvar, self.entrada, vlan, salida)
            equipos_service.guardar()
            m.append("He escrito {0}".format(salida))
        #
        # lightsquid group
        if not os.path.exists(self.LIGHTSQUID_DIR):
            os.makedirs(self.LIGHTSQUID_DIR)
        salida = '{0}/group.cfg'.format(self.LIGHTSQUID_DIR)
        equipos_lightsquidgroup = EquiposLightSquidGroup(self.salvar, self.entrada, '', salida)
        equipos_lightsquidgroup.guardar()
        m.append("He escrito {0}".format(salida))
        #
        # lightsquid realname
        salida = '{0}/realname.cfg'.format(self.LIGHTSQUID_DIR)
        equipos_lightsquidrealname = EquiposLightSquidRealname(self.salvar, self.entrada, '', salida)
        equipos_lightsquidrealname.guardar()
        m.append("He escrito {0}".format(salida))
        return("\n".join(m))

    def __repr__(self):
        m = list()
        for vlan in self.VLANS:
            equipos_hosts = EquiposHosts(self.salvar, self.entrada, vlan, 'hosts')
            m.append(str(equipos_hosts))
            m.append('-' * 80)
            equipos_dnsmasqconf = EquiposDnsmasqconf(self.salvar, self.entrada, vlan, 'dnsmasq.conf')
            m.append(str(equipos_dnsmasqconf))
            m.append('-' * 80)
            equipos_netdev = EquiposNetdev(self.salvar, self.entrada, vlan, '.netdev')
            m.append(str(equipos_netdev))
            m.append('-' * 80)
            equipos_network = EquiposNetwork(self.salvar, self.entrada, vlan, '.network')
            m.append(str(equipos_network))
            m.append('-' * 80)
            equipos_service = EquiposService(self.salvar, self.entrada, vlan, '.service')
            m.append(str(equipos_service))
            m.append('=' * 80)
        equipos_lightsquidgroup = EquiposLightSquidGroup(self.salvar, self.entrada, '', 'group.cfg')
        m.append(str(equipos_lightsquidgroup))
        m.append('-' * 80)
        equipos_lightsquidrealname = EquiposLightSquidRealname(self.salvar, self.entrada, '', 'realname.cfg')
        m.append(str(equipos_lightsquidrealname))
        return("\n".join(m))
