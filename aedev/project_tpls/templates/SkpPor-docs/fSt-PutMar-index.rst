{project_name} documentation
{'#' * len(project_name + ' documentation')}

welcome to the documentation of the {project_name} project.

.. toctree::
    :maxdepth: 1

    {format_file_paths("features_and_examples*.rst", path_prefix=DOCS_FOLDER)}
    code-conventions.rst


main module
***********

.. autosummary::
    :toctree: _autosummary
    :nosignatures:

    {import_name}

{'''

manuals and tutorials
*********************

.. toctree::

    ''' + _manus if (_manus := format_file_paths('man', "**", "*.rst", path_prefix=DOCS_FOLDER) else ""}

indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* `portion repositories at {repo_domain} <{repo_root}>`_
