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
from fabric.utils import *
from fabric.contrib.console import confirm
from fabric.contrib.files import *
import time


# Issue a verify task
def verify(alias):
	print(green("Verifying %s .." % alias))
	run("drush @hostmaster hosting-task %s verify" % alias)

# Get a list of aliases
def get_aliases():
	print(green("Getting the list of aliases .."))
	lines   = run("drush sa" )
	aliases = lines.splitlines()
	for alias in aliases:
		print(yellow(alias))

# Get info for an aliases
def get_alias(alias):
	print(green("Getting info for alias %s .." % alias))
	run("drush sa %s" % alias )

# Get a site's status
def get_status(alias):
	print(green("Getting status for %s .." % alias))
	run("drush %s st" % alias )

# Get all the site's for a platform
# def get_sites(alias):
# 	print(green("Getting a list of sites for %s .." %alias))
# 	lines = run("drush ps %s" % alias )
# 	sites = lines.splitlines()
# 	for site in sites:
# 		print(yellow(site), show_prefix=False)

# Get all the site's for a platform
def get_platform_sites(platform):
	print(green("Getting a list of sites for %s .." %platform))
	lines = run("drush ps %s" % platform )
	sites = lines.splitlines()
	return sites

def get_platforms():
	print(green("Getting list of platforms"))
	return get_aliases_by_type('platform')

def get_servers():
	print(green("Getting list of servers"))
	return get_aliases_by_type('server')

def get_sites():
	print(green("Getting list of sites"))
	return get_aliases_by_type('site')


def get_aliases_by_type(type):
	lines = run("drush aat --context-type=%s" % type)
	return lines.splitlines()
