import sys, os
while True:
    try: command, *args = input(f"{os.getcwd()}>").split(); os.chdir(' '.join(args)) if command in ['chdir', 'cd'] else os.chdir('..') if command == 'cd..' else sys.exit() if command == "exit" else os.system(' '.join([command] + args))
    except Exception: print("[CustomCMD Lite] Unknown Error!")
