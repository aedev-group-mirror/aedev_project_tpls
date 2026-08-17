""" project_tpls unit tests. """

from aedev.project_tpls import __version__, __doc__


def test_version():
    """ test existence of this template package project version number. """
    assert __version__
    assert isinstance(__version__, str)
    assert __version__.count(".") == 2


def test_docstring():
    """ test existence of this template package project docstring. """
    assert __doc__
    assert isinstance(__doc__, str)
