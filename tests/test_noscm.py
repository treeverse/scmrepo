import pathlib

import pytest

from scmrepo.git import Git
from scmrepo.noscm import NoSCM


def test_noscm(tmp_dir: pathlib.Path):
    scm = NoSCM(tmp_dir)
    scm.add("test")


def test_noscm_raises_exc_on_unimplemented_apis(tmp_dir: pathlib.Path):
    class Unimplemented(Exception):
        pass

    scm = NoSCM(tmp_dir, _raise_not_implemented_as=Unimplemented)
    assert scm._exc is Unimplemented

    assert callable(Git.reset)
    with pytest.raises(Unimplemented):
        assert scm.reset()
