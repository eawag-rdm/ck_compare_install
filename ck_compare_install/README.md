# compare_install

Compares set of modules loaded in two CKAN instances on two different machines.
Useful to compare deployment- with development environment. Also compares the
git revison of plugins that are loaded by both apps.

## Usage:

|compare_install <host1> [<host2>]
|compare_install -h

## Arguments:

`<host1>`:   First machine in URL notation, e.g. "https://remote-server.eawag.ch".
`<host2>`:   Second machine in URL notation [default: http://localhost:5000]

## Options:

`-h --help`    Show this help.
    
## Assumptions:
	
+ All remote hosts involved are reachable with passwordless ssh.

+ On all involved machines there exists a directory under which all git
  repositories for ckan core and the plugins are stored.
  The version that is checked out there is the running version.

  For development on localhost this is asumed to be `/usr/lib/ckan/default/src`.

  For remote machines the default is given by the constant
  `GITBASE_REMOTE` (`/home/ckan/git`).

  To temporarily set `GITBASE_REMOTE` or use different `GITBASE_REMOTE for
  `<host1>` and `<host2>`, set environment variable(s)
  ^GITBASE_REMOTE_<normalized_hostname>`. `<normalized_hostname>` is the hostname
  this path refers to, where all characters are uppercase and all
  non-alphanumerical characters have been replaced with an underscore ("_").

  Example:
  |GITBASE_REMOTE_DEPLOY_SERV=/home/Ckan/ckan/git compare_install \
  |https://deploy-serv.mydomain.tld http://localhost:5000
