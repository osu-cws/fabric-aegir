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


