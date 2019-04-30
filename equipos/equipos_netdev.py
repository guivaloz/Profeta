from equipos.equipos import Equipos


class EquiposNetdev(Equipos):
    """ Equipos /etc/systemd/network/enp1s0.NN.netdev """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposNetdev> Aviso: La consulta no arrojó equipos.')
        if self.vlan == '':
            raise Exception('<EquiposNetdev> Aviso: Falta la VLAN.')
        contenido = list()
        contenido.append("[NetDev]")
        contenido.append("Name={0}.{1}".format(self.NETWORK_DEVICE, self.vlan))
        contenido.append("Kind=vlan")
        contenido.append("")
        contenido.append("[VLAN]")
        contenido.append("Id={}".format(self.vlan))
        contenido.append("")
        contenido.append("")
        return('\n'.join(contenido))

