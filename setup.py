import os
import sys
from setuptools import setup, find_packages
from tethys_apps.app_installation import custom_develop_command, custom_install_command

### Apps Definition ###
app_package = 'grace_groundwater_monitoring_tool'
release_package = 'tethysapp-' + app_package
app_class = 'grace_groundwater_monitoring_tool.app:GraceGroundwaterMonitoringTool'
app_package_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tethysapp', app_package)

### Python Dependencies ###
dependencies = []

setup(
    name=release_package,
    version='0.0.1',
    tags='Hydrology,Groundwater,GRACE,GRACE-FO,GLDAS',
    description='This app displays data collected from NASA&#39;s GRACE and GRACE-FO missions.  It also soil moisture and surface water data from NOAA&#39;s GLDAS model and it displays changes in groundwater data derived from the above mentioned datasets.',
    long_description='',
    keywords='',
    author='Travis McStraw',
    author_email='travis.mcstraw@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['tethysapp', 'tethysapp.' + app_package],
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    cmdclass={
        'install': custom_install_command(app_package, app_package_dir, dependencies),
        'develop': custom_develop_command(app_package, app_package_dir, dependencies)
    }
)
