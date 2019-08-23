# sshaman
### a simple ssh manager

## requirements
* pass (this is used to store your passwords securely)
* sshpass (this is used to auto inject your ssh passwords)

## commands
### connect
connects to a sshaman connection, can be used without the con command
```{r,engine='sh'}
sshaman connect <alias>
sshaman con <alias>
sshaman <alias>
```
### list
lists all of the connections that sshaman manages, or gives info about the specified connection
```{r,engine='sh'}
sshaman list
sshaman list <alias>
sshaman ls
sshaman ls <alias>
```
### add
adds a new connection to the sshaman ssh manager
NOTE: the alias cannot be list, add, del, con, or help
```{r,engine='sh'}
sshaman add <alias> <hostname> <user>
```
### remove
removes the connection from the sshaman
```{r,engine='sh'}
sshaman remove <alias>
sshaman rm <alias>
```
### env
adds environment variables to a connection
```{r,engine='sh'}
sshaman env <alias> "your env vars"
```
## EXPERIMENTAL FEATURES
### push
pushes a file to remote server
```{r,engine='sh'}
sshaman push <alias> <local-file> <remote-destination>
sshaman put <alias> <local-file> <remote-destination>
```
if the remote-destination argument is left blank sshaman assumes the home directory of the remote server
```{r,engine='sh'}
sshaman push <alias> <local-file>
sshaman put <alias> <local-file>
```
### pull
pulls a file from the remote server
```{r,engine='sh'}
sshaman pull <alias> <remote-file> <local-destination>
sshaman get <alias> <remote-file> <local-destination>
```
if the local-destination argument is left blank sshaman assumes the current directory
```{r,engine='sh'}
sshaman pull <alias> <remote-file>
sshaman get <alias> <remote-file>
```
