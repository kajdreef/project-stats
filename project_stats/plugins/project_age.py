import datetime
from .plugin import plugin
from subprocess import Popen, PIPE, TimeoutExpired
from datetime import datetime

class project_age(plugin):

    IDENTIFIER = "project_age"

    def __init__(self, config: str):
        self.config = config

    def check_project(self, direntry):
        return {self.IDENTIFIER: {
            "first_commit": self._first_commit(direntry),
            "last_commit": self._last_commit(direntry)
        }}

    def _string_to_datetime(self, date_str):
        return datetime.strptime(date_str, "'%a %b %D %H:%M:%S %y %z'")


    def _first_commit(self, direntry):
        git_process = Popen(["git", "log", "--format='%ad'"], stdout=PIPE, cwd=direntry)
        first_commit_date = Popen(["tail", "-n 1"], stdin=git_process.stdout, stdout=PIPE)
        
        try:
            first_commit_date = self._string_to_datetime(first_commit_date.communicate(timeout=2)[0].decode("utf-8").strip())
        except TimeoutExpired:
            first_commit_date.kill()
            first_commit_date = ""
        
        return first_commit_date

    def _last_commit(self, direntry):
        git_process = Popen(["git", "log", "--format='%ad'"], stdout=PIPE, cwd=direntry)
        last_commit_date = Popen(["head", "-n 1"], stdin=git_process.stdout, stdout=PIPE)

        try:
            last_commit_date = self._string_to_datetime(last_commit_date.communicate(timeout=2)[0].decode("utf-8").strip())
        except TimeoutExpired:
            last_commit_date.kill()
            last_commit_date = ""

        return last_commit_date


        