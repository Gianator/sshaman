import click
from click_aliases import ClickAliasedGroup

import sys
import configparser

from .utils import command_aliases
from .sshamanager import sshaman_connect, sshaman_add, sshaman_edit, sshaman_list, sshaman_remove, edit_one, alias_exists, read_config


@click.group(cls=ClickAliasedGroup)
def sshaman():
    """An SSH manager"""


@sshaman.command(aliases=command_aliases['connect'][1])
@click.argument('alias')
def connect(alias: str):
    """Connect to a manged connection"""
    sshaman_connect(alias)


@sshaman.command(aliases=command_aliases['add'][1])
@click.argument('alias')
@click.argument('connection')
@click.option('-e', '--env', help='Environment variables for the connection')
@click.option('-p', '--password', help='Inject the password non-interactively (LESS SECURE)')
def add(alias: str, connection: str, env: str = None, password: str = None):
    """Add a new connection to sshaman"""
    sshaman_add(alias, connection, env, password)


@sshaman.command(aliases=command_aliases['remove'][1])
@click.argument('alias')
def remove(alias: str):
    """Remove a connection from sshaman"""
    sshaman_remove(alias)


@sshaman.command(aliases=command_aliases['edit'][1])
@click.argument('alias')
@click.option('-c', '--connection', help='Change the connection')
@click.option('-e', '--env', help='Change the environment variables')
@click.option('-p', '--password', help='Change the password')
def edit(alias: str, connection: str = None, env=None, password: str = None):
    """Edit a connection"""
    if connection or env or password:
        if connection:
            edit_one(alias, 'connection', connection)
        if env:
            edit_one(alias, 'env', env)
        if password:
            edit_one(alias, 'password', password)
    else:
        sshaman_edit(alias)


@sshaman.command(aliases=command_aliases['list'][1])
@click.argument('query', required=False)
def ls(query: str = None):
    """List sshaman connections"""
    sshaman_list(query)


# def main():
#     if len(sys.argv) > 1 and sys.argv[1] and alias_exists(read_config(), sys.argv[1]):
#         sshaman_connect(sys.argv[1])
#     else:
#         sshaman(progName='sshaman')
