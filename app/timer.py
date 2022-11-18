import os
import platform


class Timer:
    def start_timer(self, time: int):
        system = platform.system()

        if system == "Darwin" or system == "Linux":
            os.system(f"""sh -c 'sleep {time} && say Next dev' && devpair next &""")
