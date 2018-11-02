from distutils.core import setup
import setuptools

setup(
  name = 'geospatial',
  py_modules = ['geospatialUtils', 'censusUtils'],
  version = '0.0.1',
  description = 'A Python Geospatial Tool',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/geospatial',
  keywords = ['geohash', 'location'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires=['geohash==0.0.1', 'Shapely', 'pyshp', 'utils==0.0.1', 'haversine'],
  dependency_links=['git+ssh://git@github.com/tgadf/geohash.git#egg=geohash-0.0.1', 'git+ssh://git@github.com/tgadf/utils.git#egg=utils-0.0.1']
)
 
