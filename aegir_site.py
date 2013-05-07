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


