from setuptools import setup
from codecs import open
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytelegraf_exec',
    version='0.1.2',
    description='A easy to use line format convertor for influxdb.',
    long_description=long_description,
    # What does your project relate to?
    keywords='telegraf influxdb monitoring',
    # Module to share
    py_modules=["pytelegraf_exec"],
    # Author details
    author='Randy Coburn',
    author_email='development@newvoicemedia.com',

    # Choose your license
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: System :: Monitoring',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
