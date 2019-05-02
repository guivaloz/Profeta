from equipos.equipos import Equipos


class EquiposDnsmasqconf(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/dnsmasq.conf """

    PROXY_SERVER = 'proxy.sesaec.lan'

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposDnsmasqconf> Aviso: La consulta no arrojó equipos.')
        a = list()
        if self.vlan != '':
            a.append("#")
            a.append("# /var/lib/dnsmasq/vlan{0}/dnsmasq.conf".format(self.vlan))
            a.append("#")
            a.append("")
            a.append("# Hosts files of the VLAN")
            a.append("addn-hosts=/var/lib/dnsmasq/vlan{0}/hosts".format(self.vlan))
            a.append("")
            a.append("# Listen only on the device with this IP address")
            a.append("listen-address={0}.{1}.{2}".format(self.IP_ADDRESS_PREFIX, self.vlan, self.IP_ADDRESS_PROFETA_N))
            a.append("")
            a.append("# IP address range for unkown hosts")
            a.append("dhcp-range={0}.{1}.101,{0}.{1}.199,1h".format(self.IP_ADDRESS_PREFIX, self.vlan))
            a.append("")
        a.append("# Fixed IP address")
        for equipo in self.equipos:
            if self.vlan == '':
                a.append("# vlan{0} -> {1}, {2}, {3}, {4}".format(
                    equipo.vlan,
                    equipo.macaddress,
                    equipo.ip,
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
            elif equipo.vlan == self.vlan:
                a.append("dhcp-host={0},{1}  # {2}: {3}".format(
                    equipo.macaddress,
                    equipo.ip,
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
        a.append("")
        if self.vlan != '':
            a.append("# Lease file")
            a.append("dhcp-leasefile=/var/lib/dnsmasq/vlan{0}/dnsmasq.leases".format(self.vlan))
            a.append("")
            a.append("# URL del script de configuración automática de proxy en el navegador")
            a.append("dhcp-option=252,http://{0}/proxy.pac".format(self.PROXY_SERVER))
            a.append("# En cambio, para Windows, cuando no se tiene, se envía un avance de línea")
            a.append('#dhcp-option=252,"\\n"')
            a.append("")
            a.append("# Include all files in /etc/dnsmasq.d except RPM backup files")
            a.append("conf-dir=/etc/dnsmasq.d,.rpmnew,.rpmsave,.rpmorig")
            a.append("")
        a.append("")
        return('\n'.join(a))
