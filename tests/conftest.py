import shutil
from git import Repo
import pytest
from unittest import mock


@pytest.fixture(name="repo")
def create_repo(tmpdir: str) -> Repo:
    repo_path = tmpdir / "test_data"
    shutil.copytree("tests/test_data", repo_path)

    repo = Repo.init(repo_path)
    repo.active_branch.rename("master")

    # It's added to allow github workflow to create a more realistic git repository
    repo.config_writer().set_value("user", "name", "myusername").release()
    repo.config_writer().set_value("user", "email", "myemail").release()

    return repo


@pytest.fixture(name="logger")
def create_logger() -> mock.Mock:
    logger = mock.Mock()
    logger.info = mock.Mock()
    logger.error = mock.Mock()
    logger.debug = mock.Mock()
    logger.warn = mock.Mock()
    return logger
