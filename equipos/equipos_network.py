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
        contenido = list()
        contenido.append("[Match]")
        contenido.append("Name={0}.{1}".format(self.NETWORK_DEVICE, self.vlan))
        contenido.append("")
        contenido.append("[Network]")
        contenido.append("DHCP=no")
        contenido.append("")
        contenido.append("[Address]")
        contenido.append("Address={0}.{1}.1/24".format(self.IP_ADDRESS_PREFIX, self.vlan))
        contenido.append("")
        contenido.append("")
        return('\n'.join(contenido))
