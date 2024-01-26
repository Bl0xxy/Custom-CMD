"""
ConfigManager.py - Configuration System For CustomCMD
"""

import json
import sys
import os
sys.path.append(os.getcwd())

class ConfigManager:
    default_config: dict = {
        "CTRL_C_EXIT": False, "STARTING_DIRECTORY": os.path.expanduser('~'), "START_MESSAGE": "Microsoft Windows [Version 10.0.19045.3570]\n(c) Microsoft Corporation. All rights reserved.\n", "DEFAULT_COLOR": "07"
    }
    
    def __init__(self, fn) -> None:
        self.config = self.default_config
        self.config_dir = os.path.join(os.getcwd(), "save")
        self.path = self.config_dir + f"\\{fn}"

        self.load()

    def load(self) -> None:
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
            return

        try:
            with open(self.path, encoding='utf-8') as c:
                c = json.load(c)
                for v in self.config:
                    if v in c: self.config[v] = c[v]
        except FileNotFoundError:
            with open(self.path, "w+", encoding='utf-8') as f:
                json.dump(self.config, f)
        except Exception as e:
            print(f"Error: {e.args[0]}.  Please report it to the developer.")
            os.system('pause')
