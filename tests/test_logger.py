from unittest import mock

from app.logger import Logger


def test_should_call_functions(logger: mock.Mock):
    app_logger = Logger(logger=logger)

    app_logger.error("Test A")
    app_logger.debug("Test B")
    app_logger.info("Test C")
    app_logger.warn("Test D")

    logger.error.assert_called_once_with("Test A")
    logger.debug.assert_called_once_with("Test B")
    logger.info.assert_called_once_with("Test C")
    logger.warn.assert_called_once_with("Test D")
