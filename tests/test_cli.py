from unittest import mock

from click.testing import CliRunner

from app.cli import cli
from app.logger import Logger
from app.manager import Manager


@mock.patch.object(Manager, "run_start")
@mock.patch.object(Logger, "set_verbose")
def test_should_setup_verbose(fake_set_verbose, _):
    runner = CliRunner()
    result = runner.invoke(cli, ["-v", "start"])

    assert result.exit_code == 0
    fake_set_verbose.assert_called_once_with(True)


@mock.patch.object(Manager, "run_start")
def test_should_run_start(fake_run_start):
    runner = CliRunner()
    result = runner.invoke(cli, ["start"])

    assert result.exit_code == 0
    fake_run_start.assert_called_once()


@mock.patch.object(Manager, "run_start")
def test_should_run_start_with_timer(fake_run_start):
    runner = CliRunner()
    result = runner.invoke(cli, ["start", "33"])

    assert result.exit_code == 0
    fake_run_start.assert_called_once()
    fake_run_start.assert_called_once_with(33)


@mock.patch.object(Manager, "run_next")
def test_should_run_next(fake_run_next):
    runner = CliRunner()
    result = runner.invoke(cli, ["next"])

    assert result.exit_code == 0
    fake_run_next.assert_called_once()


@mock.patch.object(Manager, "run_done")
def test_should_run_done(fake_run_done):
    runner = CliRunner()
    result = runner.invoke(cli, ["done"])

    assert result.exit_code == 0
    fake_run_done.assert_called_once()


@mock.patch.object(Manager, "run_timer")
def test_should_run_timer(fake_start_timer):
    runner = CliRunner()
    result = runner.invoke(cli, ["timer", "33"])

    assert result.exit_code == 0
    fake_start_timer.assert_called_once_with(33)


@mock.patch.object(Manager, "run_cow")
def test_should_run_cow(fake_run_cow):
    runner = CliRunner()
    result = runner.invoke(cli, ["cow"])

    assert result.exit_code == 0
    fake_run_cow.assert_called_once()
