from setuptools import setup

setup(
    name='michalmierzejewskiproject',
    version='1.0',
    description='package for python class',
    py_modules=['data_analysis', 'data_loading', 'data_transofrmation', 'main_script'],
    url='https://github.com/mierzej99/AirPollutionProject',
    author='Michal Mierzejewski',
    install_requires=[
        'pandas', 'pytest'
    ],
)
