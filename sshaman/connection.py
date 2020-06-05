from os import system

class Connection(object):
    def __init__(self, alias: str, connection: str, env: str = None):
        self.alias = alias
        self.connection = connection
        self.env = env

        self.password = None

    def connect(self):
        if self.password is None:
            self.password = self.decrypt()
        
        system(self.env + ' sshpass -p ' + self.password + ' ssh ' + self.connection)
       
    def edit(self):
        pass

    def decrypt(self):
        pass

    def __str__(self):
        string = self.alias + ":\n"
        string += "  " + self.connection + "\n"
        if self.env is not None:
            string += "  " + self.env
        return string


if __name__ == '__main__':
    con = Connection("droplet", "greg@ory.land", "TERM=xterm")
    print(con)
    con.connect()
