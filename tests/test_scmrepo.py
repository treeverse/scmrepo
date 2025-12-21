import pathlib
from unittest.mock import MagicMock

from scmrepo.git import Git
from scmrepo.progress import GitProgressEvent


def test_clone(tmp_dir: pathlib.Path):
    progress = MagicMock()
    url = "https://github.com/treeverse/dvcyaml-schema"
    rev = "cf279597596b54c5b0ce089eb4bda41ebbbb5db4"

    repo = Git.clone(url, "dir", rev=rev, progress=progress)
    assert repo.get_rev() == rev

    ((event,), kw) = progress.call_args
    assert not kw
    assert isinstance(event, GitProgressEvent)
    assert (tmp_dir / "dir").exists()


def test_clone_shallow(tmp_dir: pathlib.Path):
    url = "https://github.com/treeverse/dvcyaml-schema"
    shallow_branch = "master"

    repo = Git.clone(url, "dir", shallow_branch=shallow_branch)
    shallow_file = tmp_dir / "dir" / ".git" / "shallow"
    assert shallow_file.exists()
    assert repo.get_rev() in shallow_file.read_text(encoding="utf-8").splitlines()
