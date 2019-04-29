from equipos.equipos import Equipos


class EquiposHosts(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/hosts """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposHosts> Aviso: La consulta no arrojó equipos.')
        contenido = list()
        if self.vlan != '':
            contenido.append("#")
            contenido.append("# /var/lib/dnsmasq/vlan{0}/hosts".format(self.vlan))
            contenido.append("#")
            contenido.append("{0}.{1}.{2} {3}".format(self.IP_ADDRESS_PREFIX, self.vlan, self.IP_ADDRESS_PROFETA_N, 'wpad proxy profeta'))
        for equipo in self.equipos:
            mayusculas = ''.join([c for c in equipo.nombre if c.isupper()])
            if mayusculas == '':
                raise Exception('<Error> Las siglas se toman a partir de las mayúsculas, {} no las tiene.'.format(equipo.nombre))
            if self.vlan == '':
                contenido.append("# vlan{0}: {1} {2} -> {3}, {4}".format(
                    equipo.vlan,
                    equipo.ip,
                    mayusculas.lower(),
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
            elif equipo.vlan == self.vlan:
                contenido.append("{0}  {1} # {2}: {3}".format(
                    equipo.ip,
                    mayusculas.lower().ljust(6),
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
        contenido.append("")
        contenido.append("")
        return('\n'.join(contenido))

