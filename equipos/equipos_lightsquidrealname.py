from equipos.equipos import Equipos


class EquiposLightSquidRealname(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/hosts """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposLightSquidGroup> Aviso: La consulta no arrojó equipos.')
        a = list()
        for equipo in self.equipos:
            a.append("{0}\t{1}".format(equipo.ip, equipo.nombre))
        a.append("")
        a.append("")
        return('\n'.join(a))
