import os
import sys
import configparser
from getpass import getpass
import readline

config_file = os.path.dirname(os.path.realpath(__file__)) + '/sshaman.conf'


# Attempt to connect to an sshaman connection
def connect(alias):
    config = read_config()
    if alias_exists(config, alias):
        # fetch the password
        passwd = os.popen('pass sshaman/' + alias).read().strip()
        if env_exists(config, alias):
            # This connection has env varibles associated with it so connect with them injected
            os.system(config[alias]["env"] + ' sshpass -p ' + passwd + ' ssh ' + config[alias]["connection"])
        else:
            # This connection has no env variables, connect normally
            os.system('sshpass -p ' + passwd + ' ssh ' + config[alias]["connection"])
    else:
        print('sshaman connection \'' + alias + '\' was not found')

# Adds a new connection to sshaman
def add(alias, connection, env=None, password=None):
    config = read_config()
    if alias_exists(config, alias):
        print("sshaman creation failed: you already have a connection with that alias")
    else:
        config.add_section(alias)
        config.set(alias, "connection", connection)
        if env:
            config.set(alias, "env", env)
        if password:
            config.set(alias, "password", password)
        else:
            passwd = getpass("Enter password:")
            config.set(alias, "password", passwd)
        write_config(config)
        print("sshaman connection added")

# Remove a connection from sshaman
def remove(alias):
    config = read_config()
    if alias_exists(config, alias):
        config.remove_section(alias)
        write_config(config)
        print("sshaman connection removed")
    else:
        print("sshaman connection not found")

# Edit an sshaman connection (interactive)
def edit(alias):
    config = read_config()
    if alias_exists(config, alias):
        con = editable_input("Connection: ", config[alias]["connection"])

        if env_exists(config, alias):
            env = editable_input("Env. Vars.: ", config[alias]["env"])
        else:
            env = input("Env. Vars.: ")
            if env == "":
                env = None

        passwd = getpass("  Password: ")
        if passwd == "":
            passwd = config[alias]["password"]

        config.set(alias, "connection", con)
        if env is not None:
            config.set(alias, "env", env)
        config.set(alias, "password", passwd)

        write_config(config)

        print("sshaman connection updated")

    else:
        print("sshaman connection not found")

# Edit single sshaman connection field
def edit_one(alias, field, data):
    config = read_config()
    if alias_exists(config, alias):
        if field in ["connection", "env", "password"]:
            config.set(alias, field, data)
        write_config(config)
    else:
        print("sshaman connection not found")


# like the default input() function but has a default value that can be edited
def editable_input(prompt, prefill=''):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()


# List of sshaman connections
def list(query):
    config = read_config()
    if len(config.sections()) == 0:
        print("no sshaman connections found")
    else:
        if query:
            print("Query: "  + query)
            i = 0
            for section in config.sections():
                if query in config[section]["connection"]:
                    print_connection(config, section)
                    i = i + 1
            if i == 0:
                print("no sshaman connections found")
        else:
            for section in config.sections():
                print_connection(config, section)

def print_connection(config, alias):
    print(alias + ":")
    print("  " + config[alias]["connection"])
    if env_exists(config, alias):
        print("  " + config[alias]["env"])


# Read the config into memory
def read_config():
    if not os.path.isfile(config_file):
        # config file doesnt exist, so create it
        file = open(config_file, "w")
        file.write("")
        file.close()

    config = configparser.ConfigParser()
    config.read(config_file)
    return config

# Save the supplied config reference to the config file
def write_config(config):
    with open(config_file, "w") as output:
        config.write(output)

# Check if there is a connection with the supplied alias
def alias_exists(config, alias):
    if alias in config.sections():
        return True
    return False

# Checks if there are any ENV variables for the connection
def env_exists(config, alias):
    if "env" in config[alias]:
        return True
    return False
