from setuptools import setup, find_packages


NAME = 'project_pareto'
VERSION = '0.1.0dev'


setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        'pyomo',
        'pandas==1.2.*',
        'openpyxl',
    ],
    maintainer="Keith Beattie",
    maintainer_email="ksbeattie@lbl.gov",
    platforms=["any"],
    license="TODO",
    keywords=[
        NAME
        # TODO add keywords
    ],
    classifiers=[
        # TODO add classifiers
    ]
)
