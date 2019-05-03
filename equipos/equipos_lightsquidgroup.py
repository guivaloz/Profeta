from equipos.equipos import Equipos


class EquiposLightSquidGroup(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/hosts """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposLightSquidGroup> Aviso: La consulta no arrojó equipos.')
        a = list()
        numero = 0
        secuencias = dict()
        for equipo in self.equipos:
            if equipo.departamento in secuencias:
                sec = secuencias[equipo.departamento]
            else:
                numero += 1
                sec = str(numero).zfill(2)
                secuencias[equipo.departamento] = sec
            # Direccion IP
            # Secuencia
            # Departamento
            a.append("{0}\t{1}\t{2}".format(equipo.ip, sec, equipo.departamento))
        a.append("")
        a.append("")
        return('\n'.join(a))
