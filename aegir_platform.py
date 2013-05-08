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


# Download and import a platform using Drush Make
def build_platform():
	print(green("Building new platform %s." % env.build))
	run("drush make %s /var/aegir/platforms/%s" % (env.makefile, env.build))

def make_platform_alias():
	print(green("Creating alias for platform %s." % env.build))
	run("drush provision-save %s --context_type='platform' --root='/var/aegir/platforms/%s' " % (env.platform, env.build))

def import_platform():
	print(green("Importing platform %s." % env.build))
	run("drush @hostmaster hosting-import %s" % env.platform)
	run("drush @hostmaster hosting-dispatch")


