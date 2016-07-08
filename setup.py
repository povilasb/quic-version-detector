from setuptools import setup

setup(
    name='quic-version-detector',
    version='0.2.0',
    description='Simple tool to query QUIC servers for their supported versions.',
    long_description=open('README.rst').read(),
    url='https://github.com/povilasb/quic-version-detector',
    author='Povilas Balciunas',
    author_email='balciunas90@gmail.com',
    license='MIT',
    packages=['quic_version_detector'],
    entry_points = {
        'console_scripts': ['quicver = quic_version_detector.main:main']
    },
    zip_safe=False
)
