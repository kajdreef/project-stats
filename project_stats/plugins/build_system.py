import os
import json
from functools import reduce
from .plugin import plugin

class build_system(plugin):
    
    IDENTIFIER = "build_system"

    def __init__(self, config: str):
        self.config = config

    def check_project(self, direntry):
        for build_system, identifier in self.config.items():
            result = reduce(lambda x, y: x or y, map(lambda x: identifier in x, os.listdir(direntry)))
            if result:
                return build_system
            else:
                continue
        return "unknown"