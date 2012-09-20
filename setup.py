from setuptools import setup, find_packages
import sys, os

version = '1.0beta'
shortdesc = "jQuery.datatables integration with souper"

longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()

tests_require = ['interlude', 'plone.testing[zca]']

setup(name='souper.datatables',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Environment :: Web Environment',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development',
      ],
      keywords='',
      author='Jens Klein, Benjamin Stefaner',
      author_email='dev@bluedynamics.com',
      license='General Public Licence',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['souper'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'souper',
      ],
      tests_require=tests_require,
      test_suite="souper.datatables.tests.test_suite",
      extras_require=dict(
          test=tests_require,
      ),
)
