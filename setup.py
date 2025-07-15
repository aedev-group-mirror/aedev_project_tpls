# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.tpl_project V0.3.36
""" setup of aedev namespace package portion project_tpls: outsourced Python project files templates. """



# noinspection PyUnresolvedReferences
import setuptools

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': ['Development Status :: 3 - Alpha', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 'Natural Language :: English', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.9', 'Topic :: Software Development :: Libraries :: Python Modules'],
    'description': 'aedev namespace package portion project_tpls: outsourced Python project files templates',
    'extras_require': {'dev': ['aedev_tpl_project', 'sphinx', 'sphinx-rtd-theme', 'sphinx_autodoc_typehints', 'sphinx_paramlinks', 'aedev_setup_project', 'anybadge', 'coverage-badge', 'aedev_git_repo_manager', 'flake8', 'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools', 'wheel', 'twine'], 'docs': ['sphinx', 'sphinx-rtd-theme', 'sphinx_autodoc_typehints', 'sphinx_paramlinks', 'aedev_setup_project'], 'tests': ['anybadge', 'coverage-badge', 'aedev_git_repo_manager', 'flake8', 'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools', 'wheel', 'twine']},
    'install_requires': [],
    'keywords': ['configuration', 'development', 'environment', 'productivity'],
    'license': 'OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'long_description': '# aedev_project_templates module 0.0.1\n\naedev_project_templates is a Python multi-platform module project based on the [__Kivy__ Framework](https://kivy.org) \nand some portions of the [__ae__ namespace(Application Environment)](https://ae.readthedocs.io "ae on rtd").\n\nthe source code is available at [Gitlab](https://gitlab.com/aedev_project_templates-group/aedev_project_templates)\nmaintained by the user group aedev_project_templates-group.\n\nadditional credits to:\n\n* [__Erokia__](https://freesound.org/people/Erokia/) and \n  [__plasterbrain__](https://freesound.org/people/plasterbrain/) at\n  [freesound.org](https://freesound.org) for the sounds.\n* [__iconmonstr__](https://iconmonstr.com/interface/) and\n  [__Google__](https://fonts.google.com/icons?icon.set=Material+Symbols) for the icon images.\n\n',
    'long_description_content_type': 'text/markdown',
    'name': 'aedev_project_tpls',
    'package_data': {'': ['templates/de_tpl_README.md', 'templates/de_sfp_de_otf_de_tpl_.readthedocs.yaml', 'templates/de_otf_de_tpl_dev_requirements.txt', 'templates/de_otf_de_tpl_.gitlab-ci.yml', 'templates/de_otf_de_tpl_.gitignore', 'templates/de_spt_app_de_otf_de_tpl_setup.py', 'templates/de_otf_SECURITY.md', 'templates/de_otf_LICENSE.md', 'templates/de_otf_de_tpl_CONTRIBUTING.rst', 'templates/tests/de_otf_de_tpl_requirements.txt', 'templates/tests/de_otf_de_tpl_test_{portion_name or package_name}.py', 'templates/tests/de_otf_conftest.py', 'templates/de_sfp_docs/de_otf_Makefile', 'templates/de_sfp_docs/de_otf_de_tpl_requirements.txt', 'templates/de_sfp_docs/de_otf_de_tpl_index.rst', 'templates/de_sfp_docs/features_and_examples.rst', 'templates/de_sfp_docs/de_otf_de_tpl_conf.py']},
    'packages': ['aedev.project_tpls', 'aedev.project_tpls.templates', 'aedev.project_tpls.templates.tests', 'aedev.project_tpls.templates.de_sfp_docs'],
    'project_urls': {'Bug Tracker': 'https://gitlab.com/aedev-group/aedev_project_tpls/-/issues', 'Documentation': 'https://aedev.readthedocs.io/en/latest/_autosummary/aedev.project_tpls.html', 'Repository': 'https://gitlab.com/aedev-group/aedev_project_tpls', 'Source': 'https://aedev.readthedocs.io/en/latest/_modules/aedev/project_tpls.html'},
    'python_requires': '>=3.9',
    'setup_requires': ['aedev_setup_project'],
    'url': 'https://gitlab.com/aedev-group/aedev_project_tpls',
    'version': '0.3.36',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
