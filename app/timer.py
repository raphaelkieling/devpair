import os
import platform

from app.logger import Logger


class Timer:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def _execute_unix_timer(self, time: int, message: str) -> None:
        commands = [
            f"sleep {time}",
            f"say {message}",
        ]

        joined_command = " && ".join(commands)

        os.system(f"""sh -c '{joined_command}' &""")

    def _get_current_system(self) -> str:
        return platform.system()

    def start_timer(self, time: int, message: str = "Next dev"):
        system = self._get_current_system()

        if system == "Darwin" or system == "Linux":
            self._execute_unix_timer(time, message)
            return

        # TODO: Add support for windows
        self.logger.warn("Currently we only have the timer for MacOS and Linux")
