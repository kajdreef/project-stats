import os
import json
from subprocess import Popen, PIPE, TimeoutExpired
from .plugin import plugin

class sloc(plugin):

    IDENTIFIER = "sloc"

    def __init__(self, config: str):
        self.config = config

    def check_project(self, direntry):
        git_process = Popen(["scc", "."], stdout=PIPE, cwd=direntry)
        language_count = {}

        try:
            output = git_process.communicate(timeout=2)[0]
            data = output.decode()
            languages = self.config["languages"]

            for line in data.split('\n'):
                for lang in languages:
                    if line.startswith(lang):
                        language_count.update({lang : int(line.split()[-2])})
                
        except TimeoutExpired:
            count_commits.kill()
        
        return language_count