""" {portion_name or project_name} unit tests. """

# ReplaceWith#(from {os_path_relpath(version_file, project_path)[:-3].replace("/", '.')} import __doc__, __version__)#


def test_docstring():
    """ test existence of this {project_type} project docstring. """
    assert __doc__
    assert isinstance(__doc__, str)


def test_version():
    """ test existence of this {project_type} project version number. """
    assert __version__
    assert isinstance(__version__, str)
    assert __version__.count(".") == 2
