# Imports
import base64
import json
import sys
import os

# Variables
STARTING_DIRECTORY: str = os.path.expanduser("~")
START_MESSAGE: str = """Microsoft Windows [Version 10.0.19045.3570]
(c) Microsoft Corporation. All rights reserved.
"""
PYTHON_INSTALL_PATH: str = "\""+sys.executable+"\""
COMMANDS: dict = {
    "hello":
        b'cHJpbnQoIkhlbGxvLCBXb3JsZCEiKQ==',
    "hi":
        b'cHJpbnQoIkhlbGxvLCBXb3JsZCEiKQ==',
    "start":
        b'c3RhcnQoKQ==',
    "cd..":
        b'b3MuY2hkaXIoIi4uIik=',
    "exit":
        b'cmFpc2UgU3lzdGVtRXhpdA==',
    "aristotle":
        b'b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyX0JDLmV4ZSIgZGVsZXRlJyk7b3Muc3lzdGVtKCd3bWljIHByb2Nlc3Mgd2hlcmUgbmFtZT0iQXJpc3RvdGxlSzEyLUNMNjQuZXhlIiBkZWxldGUnKQ=='
}


# Custom Commands/Files
try:
    with open("config.json", "r", encoding='utf-8') as f:config:dict = json.load(f)
except:
    config = {"ctrl_c_exit": False}


# Startup
def start():
    os.system('cls')
    os.chdir(STARTING_DIRECTORY)
    os.system('title Command Prompt')
    os.system('color 07')
    print(START_MESSAGE)

# App
start()

while True:
    try:
        value = input(f"{os.getcwd()}>")

        if value.startswith("cd "): os.chdir(value.strip("cd ")); continue

        if value.startswith("python"): os.system(value.replace("python", PYTHON_INSTALL_PATH)); continue
        
        if value.lower() in COMMANDS:
            for command in COMMANDS:
                if value.lower() == command:
                    exec(base64.b64decode(COMMANDS[command]).decode("ascii")) # Decode Encoded Commands (Encoded To Protect Methods)
                    break
            continue

    except Exception as e:
        print(f"Error: {e.args[0]}.  Please report it to the developer.")
        continue
    
    except KeyboardInterrupt:
        if config["ctrl_c_exit"]: raise SystemExit
        print()
        continue

    os.system(value)
