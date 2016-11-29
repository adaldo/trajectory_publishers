from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['trajpub'],
    scripts=['scripts'],
    cfg=['cfg'],
    package_dir={'': 'src'}
)

setup(**d)
