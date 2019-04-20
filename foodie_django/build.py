from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("pypi:pybuilder_django_enhanced_plugin")

name = "django_pybuilder_test"
default_task = "publish"

@init
def set_properties(project):
    project.set_property('django_project', 'login_registration')
    project.set_property('django_apps', ['apps.register'])
    project.set_property('django_subpath', 'django_project')
