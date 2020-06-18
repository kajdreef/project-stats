import os
import importlib
import json
import sys
import argparse
from pprint import pprint
from pathlib import Path
from .config import CONFIG

def load_plugins(configs):
    plugins = []

    # use reflection to load modules!
    for plugin_name, config in configs.items():
        module = importlib.import_module(f'project_stats.plugins.{plugin_name}')
        plugin = getattr(module, plugin_name)

        plugins.append(plugin(config))

    return plugins

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_path", help="Path to project you want to analyze.")
    return parser.parse_args()

def main():
    arguments = parse_arguments()

    path = arguments.project_path
    plugins = load_plugins(CONFIG)

    if not os.path.isdir(f"{path}{os.path.sep}.git{os.path.sep}"):
        exit(1)

    results = {}
    for plugin in plugins:
        results[plugin.IDENTIFIER] = plugin.check_project(Path(path))

    print(json.dumps(results, indent=2))
    exit(0)
