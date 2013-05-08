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
import time

def site_add(site):
	site_save_alias(site)
	site_install(site)
	site_import(site)


def site_save_alias(site):
    print(green("Saving the Drush alias for %s." % site))
    run("drush provision-save @%s \
    --context_type=site \
    --uri=%s \
    --platform=%s \
    --server=%s \
    --db_server=%s \
    --profile=%s " \
    % (site, site, env.platform, env.webserver, env.dbserver, env.profile))


# Install a site on a platform, and kick off an import of the site
def site_install(site):
	print(green("Installing site %s" % site))
	run("drush @%s provision-install" % site)

def site_verify(site):
	print(green("Verifying site %s" % site))
	run("drush @%s provision-verify" % site)

# Import a site into the frontend
def site_import(site):
	print(green("Importing site into Aegir front end %s" % site))
	run("drush @hostmaster hosting-import @%s" % site)
	run("drush @hostmaster hosting-task @%s verify" % site)
	run("drush @hostmaster hosting-task @%s enable" % site)

# Migrate a site to a new platform
def site_migrate(site, platform):
	if not platform:
		platform = "@platform_" + env.build
	print(green("Migrating the site to the new platform"))
	run("drush @%s provision-migrate %s" % (site, platform))


