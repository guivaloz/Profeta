import click
import os

from equipos.equipos import Equipos
from equipos.equipos_dnsmasqconf import EquiposDnsmasqconf
from equipos.equipos_hosts import EquiposHosts
from equipos.equipos_netdev import EquiposNetdev
from equipos.equipos_network import EquiposNetwork
from equipos.equipos_service import EquiposService
from equipos.guardar_todo import GuardarTodo


class Config(object):

    def __init__(self):
        self.salvar = False
        self.entrada = ''
        self.vlan = ''
        self.salida = ''


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--salvar', is_flag=True, help='Habilita el modo de salvar o guardar')
@click.option('--entrada', default='direcciones-ip.csv', type=str, help='Nombre del archivo CSV a cargar')
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
def equipos(config):
    """
    Mostrar equipos
    """
    equipos = Equipos(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        click.echo(equipos)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def dnsmasqconf(config):
    """
    Elaborar /var/lib/dnsmasq/vlanNN/dnsmasq.conf
    """
    equipos = EquiposDnsmasqconf(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def hosts(config):
    """
    Elaborar /var/lib/dnsmasq/vlanNN/hosts
    """
    equipos = EquiposHosts(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def netdev(config):
    """
    Elaborar /etc/systemd/network/enp1s0.NN.netdev
    """
    equipos = EquiposNetdev(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def network(config):
    """
    Elaborar /etc/systemd/network/enp1s0.NN.network
    """
    equipos = EquiposNetwork(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def service(config):
    """
    Elaborar /usr/lib/systemd/system/dnsmasqvlanNN.service
    """
    equipos = EquiposService(config.salvar, config.entrada, config.vlan, config.salida)
    try:
        if config.salvar:
            click.echo(equipos.guardar())
        else:
            click.echo(equipos)
    except Exception as e:
        click.echo(e)


@cli.command()
@pass_config
def guardar_todo(config):
    """
    Guardar todas las configuraciones
    """
    guardar_todo = GuardarTodo(config.salvar, config.entrada)
    try:
        if config.salvar:
            click.echo(guardar_todo.guardar())
        else:
            click.echo(guardar_todo)
    except Exception as e:
        click.echo(e)
