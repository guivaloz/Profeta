from equipos.equipos import Equipos


class EquiposNetwork(Equipos):
    """ Equipos /etc/systemd/network/enp1s0.NN.network """

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<EquiposNetwork> Aviso: La consulta no arrojó equipos.')
        if self.vlan == '':
            raise Exception('<EquiposNetwork> Aviso: Falta la VLAN.')
        a = list()
        a.append("[Match]")
        a.append("Name={0}.{1}".format(self.NETWORK_DEVICE, self.vlan))
        a.append("")
        a.append("[Network]")
        a.append("DHCP=no")
        a.append("")
        a.append("[Address]")
        a.append("Address={0}.{1}.{2}/24".format(self.IP_ADDRESS_PREFIX, self.vlan, self.IP_ADDRESS_PROFETA_N))
        a.append("")
        a.append("")
        return('\n'.join(a))
