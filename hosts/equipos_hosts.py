from equipos.equipos import Equipos


class EquiposHosts(Equipos):
    """ Equipos hosts """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<Error> La consulta no arrojó equipos.')
        contenido = list()
        if self.vlan != '':
            contenido.append("#")
            contenido.append("# /var/lib/dnsmasq/vlan{0}/hosts".format(self.vlan))
            contenido.append("#")
            contenido.append("")
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
                contenido.append("{0} {1}  # {2}: {3}".format(
                    equipo.ip,
                    mayusculas.lower(),
                    equipo.nombre,
                    equipo.dispositivo,
                    ))
        contenido.append("")
        contenido.append("")
        return('\n'.join(contenido))

    def guardar(self):
        salida = self.crear()
        with open(self.salida, 'w') as file:
            file.write(salida)
            return('He escrito el archivo de configuración {0}'.format(self.salida))
