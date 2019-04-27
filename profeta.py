import click
from dnsmasqconf.equipos_dnsmasqconf import EquiposDnsmasqconf
from hosts.equipos_hosts import EquiposHosts


class Config(object):

    def __init__(self):
        self.salvar = False
        self.entrada = ''
        self.vlan = ''
        self.salida = ''


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--salvar', is_flag=True, help='Habilita el modo de salvar')
@click.option('--entrada', default='direcciones-ip.csv', type=str, help='Archivo CSV con insumos')
@click.option('--vlan', default='', type=str, help='Filtro por VLAN número')
@click.option('--salida', default='', type=str, help='Nombre del archivo a escribir')
@pass_config
def cli(config, salvar, entrada, vlan, salida):
    if salvar:
        config.salvar = True
        click.echo('<Aviso> En modo de salvar.')
    else:
        click.echo('<Aviso> En modo de probar.')
    config.entrada = entrada
    config.vlan = vlan
    config.salida = salida


@cli.command()
@pass_config
def dnsmasqconf(config):
    """
    Elaborar archivo dnsmasq.conf
    """
    equipos = EquiposDnsmasqconf(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos.crear())
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def hosts(config):
    """
    Elaborar archivo hosts
    """
    equipos = EquiposHosts(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos.crear())
    except Exception as e:
        click.echo(e)
