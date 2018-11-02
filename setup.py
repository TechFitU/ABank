import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt') as f:
    readme = f.read()

setup(
    name='ABank',
    version='1.0.0',
    url='https://github.com/kennethreitz/dj-database-url',
    license='BSD',
    author='TechFitU',
    author_email='alexmtnezf@techfitu.com',
    maintainer='TechFitU',
    maintainer_email='alexmtnezf@techfitu.com',
    description='The basic bank app built in with the Flask framework.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
