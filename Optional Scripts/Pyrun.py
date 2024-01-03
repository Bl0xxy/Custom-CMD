from __main__ import Command

def main():
    command = Command("pyrun", lambda:exec(command.args))
