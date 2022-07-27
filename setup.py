import os
from glob import glob
from setuptools import setup

package_name = 'rover_autodock'

setup(
    name=package_name,
    version='0.0.1',
    # Packages to export
    packages=[package_name],
    # Files we want to install, specifically launch files
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
         # Include all config files.
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
    ],
    # This is important as well
    install_requires=['setuptools'],
    zip_safe=True,
    author='Jack Rivera',
    author_email='jack@roverrobotics.com',
    maintainer='Rover Robotics',
    keywords=['foo', 'bar'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: TODO',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Rover autodocking package',
    license='TODO',
    # Like the CMakeLists add_executable macro, you can add your python
    # scripts here.
    entry_points={
        'console_scripts': [
            'rover_autodock = rover_autodock.autodock:main'
        ],
    },
)
