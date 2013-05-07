from fabric.api import *
from fabric.colors import *

from aegir_platform import *
from aegir_server import *
from aegir_site import *
from aegir_misc import *

env.user        = 'aegir'
env.shell       = '/bin/bash -c'
env.makefile    = 'http://drupal.oregonstate.edu/distro/7.21-cws-1.0.0.make.txt'
env.build       = '7.22-cws-1.0.0'
env.platform    = '@platform_722cws100'
env.webserver   = '@server_aegirpack1'
env.dbserver    = '@server_aegirvd11cwsoregonstateedu'
env.profile     = 'osu'



def get_all_sites():
 	sites = get_sites()
 	for site in sites:
 		print(yellow(site))

def get_all_platforms():
	platforms = get_platforms()
	for platform in platforms:
		print(yellow(platform))

def get_all_servers():
	servers = get_servers()
	for server in servers:
		print(yellow(server))

