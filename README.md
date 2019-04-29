
# Profeta

Administrar las configuraciones de DNSmasq con varias VLANs.

### Instalación

Cree un entorno virtual de Python 3...

    $ virtualenv -p python3 Profeta
    $ cd Profeta
    $ . bin/activate

Clone este repositorio de GitHub...

    (Profeta) $ git clone https://github.com/guivaloz/Profeta.git
    (Profeta) $ cd Profeta

Instale los requerimientos y el comando 'profeta'...

    (Profeta) $ pip install -r requirements.txt
    (Profeta) $ pip install --editable .

### Insumo

Requiere un archivo CVS de 'entrada' con las siguientes columnas

    vlans,departamentos,nombres,dispositivos,macaddress,ips,puertos

### Uso

Consultar la ayuda integrada...

    (Profeta) $ profeta --help

Mostrar tabla de datos del archivo CSV...

    (Profeta) $ profeta --entrada direcciones-ip.csv equipos

Mostrar tabla de datos del archivo CSV, filtrando por VLAN 13...

    (Profeta) $ profeta --entrada direcciones-ip.csv --vlan 13 equipos

Mostrar información básica para cada configuración

    (Profeta) $ profeta --entrada direcciones-ip.csv hosts
    (Profeta) $ profeta --entrada direcciones-ip.csv dnsmasqconf

Mostrar contenido de `hosts` de la VLAN 13

    (Profeta) $ profeta --entrada direcciones-ip.csv --vlan 13 hosts

Mostrar contenido de `dnsmasq.conf` de la VLAN 13

    (Profeta) $ profeta --entrada direcciones-ip.csv --vlan 13 dnsmasqconf
