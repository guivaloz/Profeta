
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

Instale los requerimientos y el comando [click](https://click.palletsprojects.com/en/7.x/) 'profeta'...

    (Profeta) $ pip install -r requirements.txt
    (Profeta) $ pip install --editable .

### Uso

Consulte la ayuda integrada...

    (Profeta) $ profeta --help
    Usage: profeta [OPTIONS] COMMAND [ARGS]...

    Options:
      --salvar        Habilita el modo de salvar
      --entrada TEXT  Archivo CSV con insumos
      --vlan TEXT     Filtro por VLAN número
      --salida TEXT   Nombre del archivo a escribir
      --help          Show this message and exit.

    Commands:
      dnsmasqconf  Elaborar archivo dnsmasq.conf
      hosts        Elaborar archivo hosts
