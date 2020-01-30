import os
import importlib
import json
import sys
from pprint import pprint
from multiprocessing import Pool, cpu_count

def load_plugins(config):
    plugins = []

    # use reflection to load modules!
    for plugin_name, config in config.items():
        module = __import__('plugins.' + plugin_name)
        plugin_file = getattr(module, plugin_name)
        plugin = getattr(plugin_file, plugin_name)

        plugins.append(plugin(config))

    return plugins


if __name__ == "__main__":
    config = dict()
    
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("ERROR")
        path = '../test-architecture-erosion/projects/'

    print(path)

    # Read file as a dictionary
    with open("./config.json", 'r') as f:
        config = json.load(f)
        

    plugins = load_plugins(config)
    
    # start run the tool in multiple processes to speed up
    p = Pool(cpu_count())

    projects = dict()
    for project_dir in filter(os.path.isdir, os.scandir(path)):
        results = dict()
        for plugin in plugins:

            results[plugin.IDENTIFIER] = plugin.check_project(project_dir)

        projects[project_dir.path.split('/')[-1]]  = results
    
    pprint(projects)
