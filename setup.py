import os
from setuptools import setup, find_packages
from codecs import open
from os import path
from jupyter_packaging import (
    ensure_python, get_version
)

ensure_python(('2.7', '>=3.7'))
pjoin = path.join
name = 'jupyter_paperboy'
here = path.abspath(path.dirname(__file__))
version = get_version(pjoin(here, 'paperboy', '_version.py'))


print('WARNING: https://issues.apache.org/jira/browse/AIRFLOW-1430?subTaskView=unresolved')
os.environ['AIRFLOW_GPL_UNIDECODE'] = '1'

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requires = [r for r in f.read().split(os.linesep) if '-e' not in r]
    if os.name == 'nt':
        # no gunicorn on windows
        if 'gunicorn' in requires:
            requires.remove('gunicorn')
        requires.append('waitress')

setup(
    name=name,
    version=version,
    description='Jupyter notebooks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/timkpaine/paperboy',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='BSD 3 Clause',
    python_requires='>=3.5',
    install_requires=requires,
    extras_require={'dev': requires + ['pytest', 'pytest-cov', 'pytest-falcon', 'pylint', 'flake8', 'codecov', 'nose', 'mock', 'sphinx', 'sphinx_rtd_theme']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='juyter notebooks jupyterlab analytics',
    zip_safe=False,
    packages=find_packages(exclude=[]),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'paperboy = paperboy.server:main',
            'paperboy-worker = paperboy.worker:main'
        ],
    },
)
