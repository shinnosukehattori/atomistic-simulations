from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='emff',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'emff-simulate=emff.simulation:main',
        ],
    },
)
