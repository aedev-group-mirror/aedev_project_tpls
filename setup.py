# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.89
""" setup of aedev namespace package portion project_tpls: managed Python project files templates. """
import pathlib
import sys
from typing import Any
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs: dict[str, Any] = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    'description': 'aedev namespace package portion project_tpls: managed Python project files templates',
    'extras_require': {
        'dev': [
            'aedev_project_tpls',
            'aedev_aedev',
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
        'docs': [],
        'tests': [
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
    },
    'install_requires': [],
    'keywords': [
        'configuration',
        'development',
        'environment',
        'productivity',
    ],
    'license': 'GPL-3.0-or-later',
    'long_description': (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    'long_description_content_type': 'text/markdown',
    'name': 'aedev_project_tpls',
    'package_data': {
        '': [
            'templates/fSt-PutMar-.gitignore',
            'templates/fSt-PutMar-CONTRIBUTING.rst',
            'templates/fSt-PutMar-dev_requirements.txt',
            'templates/fSt-README.md',
            'templates/PutMar-LICENSE.md',
            'templates/PutMar-SECURITY.md',
            'templates/SkpPor-fSt-PutMar-.readthedocs.yaml',
            'templates/PutMar-pyproject.toml',
            'templates/fSt-PutMar-setup.py',
            'templates/fSt-PutMar-.gitlab-ci.yml',
            'templates/SkpPor-docs/features_and_examples.rst',
            'templates/SkpPor-docs/fSt-PutMar-index.rst',
            'templates/SkpPor-docs/PutMar-Makefile',
            'templates/SkpPor-docs/fSt-PutMar-conf.py',
            'templates/SkpPor-docs/fSt-PutMar-requirements.txt',
            'templates/tests/fSt-PutMar-requirements.txt',
            'templates/tests/fSt-test_{portion_name or project_name}.py',
            'templates/tests/PutMar-conftest.py',
        ],
    },
    'packages': [
        'aedev.project_tpls',
        'aedev.project_tpls.templates',
        'aedev.project_tpls.templates.SkpPor-docs',
        'aedev.project_tpls.templates.tests',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/aedev-group/aedev_project_tpls/-/issues',
        'Documentation': 'https://aedev.readthedocs.io/en/latest/_autosummary/aedev.project_tpls.html',
        'Repository': 'https://gitlab.com/aedev-group/aedev_project_tpls',
        'Source': 'https://aedev.readthedocs.io/en/latest/_modules/aedev/project_tpls.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/aedev-group/aedev_project_tpls',
    'version': '0.3.90',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    ...
