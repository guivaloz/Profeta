import csv
import os
from tabulate import tabulate

from equipos.equipo import Equipo


class Equipos(object):
    """ Equipos """

    NETWORK_DEVICE = 'enp1s0'
    IP_ADDRESS_PREFIX = '192.168'
    IP_ADDRESS_PROFETA_N = '254'

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

    def obtener_profeta_ip_address(self):
        if str.isdigit(self.vlan):
            return(f'{self.IP_ADDRESS_PREFIX}.{self.vlan}.{self.IP_ADDRESS_PROFETA_N}')
        else:
            raise Exception('<Equipos> Aviso: Falta la VLAN.')

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

    def crear(self):
        if self.cargado == False:
            self.cargar()
        if self.cantidad == 0:
            raise Exception('<Equipos> Aviso: La consulta no arrojó equipos.')
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

    def guardar(self):
        salida = self.crear()
        with open(self.salida, 'w') as file:
            file.write(salida)
            return('He escrito {0}'.format(self.salida))

    def __repr__(self):
        self.cargar()
        return(self.crear())
