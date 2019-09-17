from equipos.equipos import Equipos


class EquiposHosts(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/hosts """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposHosts> Aviso: La consulta no arrojó equipos.')
        a = list()
        if self.vlan != '':
            a.append("#")
            a.append("# /var/lib/dnsmasq/vlan{0}/hosts".format(self.vlan))
            a.append("#")
            a.append("{0} {1}".format(self.obtener_profeta_ip_address(), 'wpad proxy profeta'))
        for equipo in self.equipos:
            mayusculas = ''.join([c for c in equipo.nombre if c.isupper()])
            if mayusculas == '':
                raise Exception('<EquiposHosts> Las siglas se toman a partir de las mayúsculas, {} no las tiene.'.format(equipo.nombre))
            if self.vlan == '':
                a.append("# vlan{0}: {1} {2} -> {3}, {4}".format(
                    equipo.vlan,
                    equipo.ip,
                    mayusculas.lower(),
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
            elif equipo.vlan == self.vlan:
                a.append("{0}  {1} # {2}: {3}".format(
                    equipo.ip,
                    mayusculas.lower().ljust(6),
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
        a.append("")
        a.append("")
        return('\n'.join(a))
