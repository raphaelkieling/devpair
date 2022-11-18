import os
import shutil
import time
from datetime import datetime, timezone
from unittest import mock

import pytest
from freezegun import freeze_time
from git import Actor, Repo

from app.manager import Manager


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
    return logger


def test_should_create_new_branch_first_time_on_start_command(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    m = Manager(path_repository=repo.working_dir, logger=logger)

    m.run_start()

    assert repo.active_branch.name == "pair/master"

    logger.info.assert_called_once()
    logger.info.assert_called_with(
        "Done, branch 'pair/master' created, happy pair programming 😄"
    )


def test_should_detect_repository_even_inside_child_folder(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    m = Manager(
        path_repository=os.path.join(repo.working_dir, "child-folder"), logger=logger
    )

    m.run_start()

    assert repo.active_branch.name == "pair/master"


def test_should_create_reuse_alread_create_branch_on_start_command(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    repo.active_branch.rename("pair/master")

    m = Manager(path_repository=repo.working_dir, logger=logger)

    m.run_start()

    assert repo.active_branch.name == "pair/master"

    logger.info.assert_called_once()
    logger.info.assert_called_with("Sync done, happy pair programming 😄")


def test_should_not_continue_if_run_next_outside_pair_branch(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    m = Manager(path_repository=repo.working_dir, logger=logger)

    m.run_next()

    logger.error.assert_called_once()
    logger.error.assert_called_with(
        "You need to be inside a pair/ branch before execute it."
    )


def test_should_not_continue_if_run_done_outside_pair_branch(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    m = Manager(path_repository=repo.working_dir, logger=logger)

    m.run_done()

    logger.error.assert_called_once()
    logger.error.assert_called_with(
        "You need to be inside a pair/ branch before execute it."
    )


def test_should_delete_and_back_to_main_after_run_done(repo: Repo, logger: mock.Mock):
    assert repo.active_branch.name == "master"

    # Initialize the commits
    # anyfile.txt comes from app/test_data. Check the repo fixture
    repo.index.add(["anyfile.txt"])
    repo.index.commit("Test")

    repo.active_branch.checkout(b="pair/master")

    assert repo.active_branch.name == "pair/master"

    m = Manager(path_repository=repo.working_dir, logger=logger)

    m.run_done()

    assert not repo.bare
    assert repo.active_branch.name == "master"
    logger.info.assert_called_once()
    logger.info.assert_called_with("🌟 Done, continue with the git commit command.")


@freeze_time("2017-05-21")
def test_should_show_simple_summary(repo: Repo, logger, capsys):
    repo.active_branch.rename("pair/master")

    commit_curr_date = datetime.fromtimestamp(time.time(), timezone.utc)

    # Initialize the commits
    # anyfile.txt comes from app/test_data. Check the repo fixture

    # developer A - Commits
    devA = Actor("dev-a", "dev-a@dev.com")

    repo.index.add(["anyfile.txt"])
    repo.index.commit(
        "Test Dev A", author=devA, committer=devA, commit_date=commit_curr_date
    )

    # developer B - Commits
    devB = Actor("dev-b", "dev-b@dev.com")

    repo.index.add(["anyfile2.txt"])
    repo.index.commit(
        "Test Dev B", author=devB, committer=devB, commit_date=commit_curr_date
    )

    repo.index.add(["anyfile3.txt"])
    repo.index.commit(
        "Test Dev B", author=devB, committer=devB, commit_date=commit_curr_date
    )

    m = Manager(path_repository=repo.working_dir, logger=logger)

    m.run_summary()

    result = capsys.readouterr().out.strip()

    expected_output = """
Last Dev: 
     dev-b@dev.com              | 2017-05-21 00:00:00
First Dev: 
     dev-b@dev.com              | 2017-05-21 00:00:00
Frequence: 
     dev-b@dev.com              | ▇ 2
     dev-a@dev.com              |  1
""".strip()

    assert result == expected_output


# TODO: Create this test
@pytest.mark.skip(reason="no way of currently testing this")
def test_should_delete_and_back_to_main_after_run_done_but_without_remote_branch(
    repo: Repo, logger: mock.Mock
):
    pass
