# Copyright (C) 2013 Oregon State University
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#
# To contact us, go to http://oregonstate.edu/cws/contact and fill out the contact form.
#
# Alternatively mail us at:
#
# Oregon State University
# Central Web Services
# 121 The Valley Library
# Corvallis, OR 97331

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

