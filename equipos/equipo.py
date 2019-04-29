import netaddr


class Equipo(object):
    """ Equipo """

    def __init__(self, vlan, departamento, nombre, dispositivo, macaddress, ip, puerto):
        self.vlan = vlan
        self.departamento = departamento
        self.nombre = nombre
        self.dispositivo = dispositivo
        self.ip = ip
        self.puerto = puerto
        # Convertir mac address a 00:00:00:00:00:00
        if macaddress != '':
            mac = netaddr.EUI(macaddress)
            mac.dialect = netaddr.mac_unix_expanded
            self.macaddress = str(mac)
        else:
            self.macaddress = ''

    @staticmethod
    def fieldnames():
        return([
            'vlans',
            'departamentos',
            'nombres',
            'dispositivos',
            'macaddress',
            'ips',
            'puertos',
            ])

    def validar(self):
        if not str.isdigit(self.vlan):
            return(False)
        if self.departamento == '':
            return(False)
        if self.nombre == '':
            return(False)
        if self.dispositivo == '':
            return(False)
        if self.macaddress == '':
            return(False)
        if self.ip == '':
            return(False)
        if not str.isdigit(self.puerto):
            return(False)
        return(True)

    def row_list(self):
        return([
            self.vlan,
            self.departamento,
            self.nombre,
            self.dispositivo,
            self.macaddress,
            self.ip,
            self.puerto,
            ])

    def __repr__(self):
        return("Equipo {}".format(self.nombre))

