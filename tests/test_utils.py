import os

import pytest

from scmrepo.utils import relpath


@pytest.mark.skipif(os.name != "nt", reason="Windows only")
def test_relpath_windows():
    assert relpath("C:\\dir1\\dir2\\file.txt", "C:\\dir1") == "dir2\\file.txt"
    assert relpath("C:\\dir1\\file.txt", "c:\\dir2") == "..\\dir1\\file.txt"


@pytest.mark.skipif(os.name != "nt", reason="Windows only")
def test_relpath_windows_different_drives():
    path = "A:\\some\\path"
    assert relpath(path, "B:\\other\\path") == path


def test_relpath():
    assert relpath(os.path.join("foo", "bar"), "foo") == "bar"
    assert relpath(os.path.join("foo", "bar"), os.path.join("foo", "baz")) == (
        os.path.join("..", "bar")
    )
