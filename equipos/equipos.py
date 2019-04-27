import csv
import os
import netaddr
from tabulate import tabulate


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


class Equipos(object):
    """ Equipos """

    def __init__(self, salvar, entrada, vlan, salida):
        # Parametros
        self.salvar = salvar
        self.entrada = entrada
        self.vlan = vlan
        self.salida = salida
        # Propios
        self.cargado = False
        self.equipos = None
        self.cantidad = 0

    def cargar(self):
        if not os.path.isfile(self.entrada):
            raise Exception("<Error> Archivo CSV {} no encontrado.".format(self.entrada))
        self.equipos = list()
        with open(self.entrada) as file:
            reader = csv.DictReader(file)
            for row in reader:
                equipo = Equipo(
                    row['vlans'].strip(),
                    row['departamentos'].strip(),
                    row['nombres'].strip(),
                    row['dispositivos'].strip(),
                    row['macaddress'].strip(),
                    row['ips'].strip(),
                    row['puertos'].strip(),
                    )
                if equipo.validar():
                    if self.vlan == '':
                        self.equipos.append(equipo)
                        self.cantidad += 1
                    elif equipo.vlan == self.vlan:
                        self.equipos.append(equipo)
                        self.cantidad += 1
        self.cargado = True

    def __repr__(self):
        if self.cantidad == 0:
            raise Exception('<Error> La consulta no arrojó equipos.')
        table = [Equipo.fieldnames()]
        for equipo in self.equipos:
            table.append(equipo.row_list())
        reporte = list()
        reporte.append('')
        reporte.append(tabulate(table, headers='firstrow'))
        reporte.append('')
        if self.vlan == '':
            reporte.append("Total {} equipos".format(self.cantidad))
        else:
            reporte.append("Total {0} equipos en VLAN {1}".format(self.cantidad, self.vlan))
        return('\n'.join(reporte))
