import os
import json
from .plugin import plugin
from subprocess import Popen, PIPE, TimeoutExpired
from pprint import pprint

class contributors(plugin):

    IDENTIFIER = "contributors"

    def __init__(self, config: str):
        self.config = config

    def check_project(self, direntry):
        git_process = Popen(["git", "--no-pager", "shortlog", "-sn"], stdout=PIPE, cwd=direntry)
        contributor_count = Popen(["wc", "-l"], stdin=git_process.stdout, stdout=PIPE)

        try:
            count = int(contributor_count.communicate(timeout=2)[0])
        except TimeoutExpired:
            contributor_count.kill()
            count = 0
        
        return count