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
        a = list()
        a.append("[NetDev]")
        a.append("Name={0}.{1}".format(self.NETWORK_DEVICE, self.vlan))
        a.append("Kind=vlan")
        a.append("")
        a.append("[VLAN]")
        a.append("Id={}".format(self.vlan))
        a.append("")
        a.append("")
        return('\n'.join(a))
