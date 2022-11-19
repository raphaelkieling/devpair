from unittest import mock
from app.timer import Timer


def test_should_run(logger: mock.Mock):
    timer = Timer(logger=logger)

    timer._get_current_system = mock.Mock(return_value="Windows")

    timer.start_timer(0)

    logger.warn.assert_called_once_with(
        "Currently we only have the timer for MacOS and Linux"
    )


def test_should_execute_unix_timer_sending_correct_time(logger: mock.Mock):
    timer = Timer(logger=logger)

    timer._get_current_system = mock.Mock(return_value="Linux")
    timer._execute_unix_timer = mock.Mock()

    timer.start_timer(33)

    logger.warn.assert_not_called()
    timer._execute_unix_timer.assert_called_once_with(33)


@mock.patch("os.system")
def test_should_execute_unix_command(os_system, logger: mock.Mock):
    timer = Timer(logger=logger)

    timer._get_current_system = mock.Mock(return_value="Linux")

    timer.start_timer(1)

    os_system.assert_called_once_with("sh -c 'sleep 1 && say Next dev' &")
