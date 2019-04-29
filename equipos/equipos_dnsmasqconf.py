from equipos.equipos import Equipos


class EquiposDnsmasqconf(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/dnsmasq.conf """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposDnsmasqconf> Aviso: La consulta no arrojó equipos.')
        contenido = list()
        if self.vlan != '':
            contenido.append("#")
            contenido.append("# /var/lib/dnsmasq/vlan{0}/dnsmasq.conf".format(self.vlan))
            contenido.append("#")
            contenido.append("")
            contenido.append("# Hosts files of the VLAN")
            contenido.append("addn-hosts=/var/lib/dnsmasq/vlan{0}/hosts".format(self.vlan))
            contenido.append("")
            contenido.append("# Listen only on the device with this IP address")
            contenido.append("listen-address={0}.{1}.{2}".format(self.IP_ADDRESS_PREFIX, self.vlan, self.IP_ADDRESS_PROFETA_N))
            contenido.append("")
            contenido.append("# IP address range for unkown hosts")
            contenido.append("dhcp-range={0}.{1}.101,{0}.{1}.199,1h".format(self.IP_ADDRESS_PREFIX, self.vlan))
            contenido.append("")
        contenido.append("# Fixed IP address")
        for equipo in self.equipos:
            if self.vlan == '':
                contenido.append("# vlan{0} -> {1}, {2}, {3}, {4}".format(
                    equipo.vlan,
                    equipo.macaddress,
                    equipo.ip,
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
            elif equipo.vlan == self.vlan:
                contenido.append("dhcp-host={0},{1}  # {2}: {3}".format(
                    equipo.macaddress,
                    equipo.ip,
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
        contenido.append("")
        if self.vlan != '':
            contenido.append("# Lease file")
            contenido.append("dhcp-leasefile=/var/lib/dnsmasq/vlan{0}/dnsmasq.leases".format(self.vlan))
            contenido.append("")
            contenido.append("# Include all files in /etc/dnsmasq.d except RPM backup files")
            contenido.append("conf-dir=/etc/dnsmasq.d,.rpmnew,.rpmsave,.rpmorig")
            contenido.append("")
        contenido.append("")
        return('\n'.join(contenido))

