import os
import json
from .plugin import plugin
from subprocess import Popen, PIPE, TimeoutExpired
from pprint import pprint

class total_commits(plugin):

    IDENTIFIER = "total_commits"

    def __init__(self, config: str):
        self.config = config

    def check_project(self, direntry):
        git_process = Popen(["git", "--no-pager", "log", "--oneline"], stdout=PIPE, cwd=direntry.path)
        count_commits = Popen(["wc", "-l"], stdin=git_process.stdout, stdout=PIPE)

        try:
            count = int(count_commits.communicate(timeout=2)[0])
        except TimeoutExpired:
            count_commits.kill()
            count = 0
        
        return {"total_commits": count}