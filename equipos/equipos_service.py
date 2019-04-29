from equipos.equipos import Equipos


class EquiposService(Equipos):
    """ Equipos /usr/lib/systemd/system/dnsmasqvlanNN.service """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposService> Aviso: La consulta no arrojó equipos.')
        if self.vlan == '':
            raise Exception('<EquiposService> Aviso: Falta la VLAN.')
        contenido = list()
        contenido.append("[Unit]")
        contenido.append("Description=DHCP and DNS caching server for vlan{0}.".format(self.vlan))
        contenido.append("After=network.target")
        contenido.append("")
        contenido.append("[Service]")
        contenido.append("ExecStart=/usr/sbin/dnsmasq -k --bind-interfaces --listen-address={0}.{1}.1 --conf-file=/var/lib/dnsmasq/vlan{1}/dnsmasq.conf --pid-file=/var/lib/dnsmasqvlan{1}.pid".format(self.IP_ADDRESS_PREFIX, self.vlan))
        contenido.append("ExecReload=/bin/kill -HUP $MAINPID")
        contenido.append("Restart=on-failure")
        contenido.append("RestartSec=5")
        contenido.append("")
        contenido.append("[Install]")
        contenido.append("WantedBy=multi-user.target")
        contenido.append("")
        contenido.append("")
        return('\n'.join(contenido))

