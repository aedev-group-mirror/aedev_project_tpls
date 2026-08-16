""" {portion_name or project_name} unit tests dummy. """

# ReplaceWith#(from {os_path_relpath(version_file, project_path)[:-3].replace("/", '.')} import __version__ as version)#


def test_version():
    assert version
    assert isinstance(version, str)
