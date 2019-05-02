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
        a = list()
        a.append("[Unit]")
        a.append("Description=DHCP and DNS caching server for vlan{0}.".format(self.vlan))
        a.append("After=network.target")
        a.append("")
        a.append("[Service]")
        a.append("ExecStart=/usr/sbin/dnsmasq -k --bind-interfaces --listen-address={0}.{1}.{2} --conf-file=/var/lib/dnsmasq/vlan{1}/dnsmasq.conf --pid-file=/var/run/dnsmasqvlan{1}.pid".format(self.IP_ADDRESS_PREFIX, self.vlan, self.IP_ADDRESS_PROFETA_N))
        a.append("ExecReload=/bin/kill -HUP $MAINPID")
        a.append("Restart=on-failure")
        a.append("RestartSec=5")
        a.append("")
        a.append("[Install]")
        a.append("WantedBy=multi-user.target")
        a.append("")
        a.append("")
        return('\n'.join(a))
