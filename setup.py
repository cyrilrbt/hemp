try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='hemp',
    version=0.1,
    author='Cyril Robert',
    author_email='cyrilrbt@gmail.com',
    url='http://cyrilrobert.org/',
    install_requires=[
        'setuptools',
        'tornado',
        'mongoengine',
        'markdown',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['hemp',],
    entry_points={
          'console_scripts': [
              'development = hemp.main:development',
              'production = hemp.main:production',
          ]},
)
