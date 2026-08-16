""" project_tpls unit tests dummy. """

from aedev.project_tpls import __version__ as version


def test_version():
    assert version
    assert isinstance(version, str)
