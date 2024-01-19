while True:
    try: command, *args = input(f"{__import__('os').getcwd()}>").split(); __import__('os').chdir(' '.join(args)) if command in ['chdir', 'cd'] else __import__('os').chdir('..') if command == 'cd..' else __import__('sys').exit() if command == "exit" else __import__('os').system(' '.join([command] + args))
    except Exception: print("[CustomCMD Lite] Unknown Error!")
