#!/usr/bin/env python3
import click
from click_aliases import ClickAliasedGroup
import os
import sys
import configparser
import sshamanager

@click.group(cls=ClickAliasedGroup)
def sshaman():
    """An SSH manager"""

@sshaman.command(aliases=['con'])
@click.argument('alias')
def connect(alias: str):
    """Connect to a managed connection"""
    sshamanager.connect(alias)


@sshaman.command()
@click.argument('alias')
@click.argument('connection')
@click.option('-e', '--env', help='Environment variables for the connection')
@click.option('-p', '--password', help='Inject the password non-interactively (LESS SECURE)')
def add(alias: str, connection: str, env: str = None, password: str = None):
    """Add a new connection for sshaman to managed"""
    sshamanager.add(alias, connection, env, password)


@sshaman.command(aliases=['rm', 'rem', 'del'])
@click.argument('alias')
def remove(alias: str):
    """Remove a connection from sshaman"""
    sshamanager.remove(alias)


@sshaman.command()
@click.argument('alias')
@click.option('-c', '--connection', help='Change the connection')
@click.option('-e', '--env', help='Change the environment variables')
@click.option('-p', '--password', help='Change the password')
def edit(alias: str, connection: str = None, env: str = None, password: str = None):
    """Edit a connection"""
    if connection or env or password:
        if connection:
            sshamanager.edit_one(alias, 'connection', connection)
        if env:
            sshamanager.edit_one(alias, 'env', env)
        if password:
            sshamanager.edit_one(alias, 'password', password)
    else:
        sshamanager.edit(alias)


@sshaman.command(aliases=['ls'])
@click.argument('query', required=False)
def list(query: str = None):
    """List all sshaman connections"""
    sshamanager.list(query)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] and sshamanager.alias_exists(sshamanager.read_config(), sys.argv[1]):
        sshamanager.connect(sys.argv[1])
    else:
        sshaman(prog_name='sshaman')