from fabric.api import *
from fabric.colors import *



def migrate_site(site):
	puts(green("Migrating site %s to platform %s." % (site env.platform))
	run("drush %s provision-migrate %s" % (site, env.platform))

def migrate():
	old_platform = '@platform_7.20-cws-1.2.0'
	sites = get_sites(old_platform)
	for site in sites:
		run("drush @%s provision-migrate %s" % (site, env.platform))



