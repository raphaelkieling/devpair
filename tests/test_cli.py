from click.testing import CliRunner
from app.cli import cli
from unittest import mock


@mock.patch("app.manager.Manager")
def test_should_run_start(manager: mock.Mock):
    manager.run_start = mock.Mock()

    runner = CliRunner()
    result = runner.invoke(cli, ["start"])

    assert result.exit_code == 0
    assert manager.run_start.assert_called()
    assert result.output == "Hello Peter!\n"
