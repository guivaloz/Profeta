from equipos.equipos import Equipos


class EquiposLightSquidRealname(Equipos):
    """ Equipos /var/lib/dnsmasq/vlanNN/hosts """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposLightSquidGroup> Aviso: La consulta no arrojó equipos.')
