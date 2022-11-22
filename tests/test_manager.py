import os
import time
from datetime import datetime, timezone
from unittest import mock

import pytest
from freezegun import freeze_time
from git import Actor, Repo

from app.manager import Manager


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


def test_should_start_the_timer_on_start_command(repo: Repo, logger: mock.Mock):
    timer_mock = mock.Mock()
    timer_mock.start_timer = mock.Mock()

    m = Manager(path_repository=repo.working_dir, logger=logger, timer=timer_mock)

    m.run_start(time_in_minutes=1)

    timer_mock.start_timer.assert_called_once_with(60)


def test_should_not_call_the_timer_on_start_command_if_none_or_less_than_one(
    repo: Repo, logger: mock.Mock
):
    timer_mock = mock.Mock()
    timer_mock.start_timer = mock.Mock()

    m = Manager(path_repository=repo.working_dir, logger=logger, timer=timer_mock)

    m.run_start(time_in_minutes=0)
    timer_mock.start_timer.assert_not_called()

    m.run_start(time_in_minutes=-5)
    timer_mock.start_timer.assert_not_called()

    m.run_start(time_in_minutes=None)
    timer_mock.start_timer.assert_not_called()


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

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        m = Manager(path_repository=repo.working_dir, logger=logger)

        m.run_next()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

    logger.error.assert_called_once()
    logger.error.assert_called_with(
        "You need to be inside a pair/ branch before execute it."
    )


def test_should_not_continue_if_run_done_outside_pair_branch(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        m = Manager(path_repository=repo.working_dir, logger=logger)

        m.run_done()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1

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


def test_should_back_to_main_after_run_done_keeping_the_changes_files(
    repo: Repo, logger: mock.Mock
):
    assert repo.active_branch.name == "master"

    # Initialize the commits in master
    repo.index.add(["anyfile.txt"])
    repo.index.commit("Test")

    # Initialize the commits in pair/master
    repo.active_branch.checkout(b="pair/master")
    repo.index.add(["anyfile2.txt", "anyfile3.txt"])
    repo.index.commit("Test 2")

    m = Manager(path_repository=repo.working_dir, logger=logger)
    m.run_next = mock.Mock()
    m.run_done()

    assert not repo.bare
    assert repo.active_branch.name == "master"

    diff = repo.git.execute("git diff --name-only HEAD".split(" "))
    assert diff == "anyfile2.txt\nanyfile3.txt"


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


def test_should_run_timer_with_param_number(repo: Repo, logger: mock.Mock):
    timer_mock = mock.Mock()
    timer_mock.start_timer = mock.Mock()

    m = Manager(path_repository=repo.working_dir, logger=logger, timer=timer_mock)

    m.run_timer(time_in_minutes=1)

    timer_mock.start_timer.assert_called_once_with(60)


def test_should_run_timer_even_outside_repository_path(tmpdir, logger: mock.Mock):
    timer_mock = mock.Mock()
    timer_mock.start_timer = mock.Mock()

    m = Manager(path_repository=tmpdir, logger=logger, timer=timer_mock)

    m.run_timer(time_in_minutes=1)

    timer_mock.start_timer.assert_called_once_with(60)
