# CustomCMD Scripting API Documentation
- [Back to README.md](README.md)
## Overview

### Functions

- **`load_config(fp: str) -> dict`**
  - Returns the configuration file based on the provided filepath.

- **`start() -> None`**
  - Initiates the startup behavior.

- **`cmd_exists(name: str) -> bool`**
  - Checks if a command exists by its name.

- **`find_cmd(name: str) -> Command`**
  - Locates a command by its name.

- **`exec_cmd(name: str) -> None`**
  - Executes a command by its name.

- **`get_cmds() -> list`**
  - Retrieves a list of all command names.

### Exceptions/Errors

- **`InvalidCommandError(name: str)`**
  - Raised if a specified command doesn't exist.

### Classes

- **`Command(name: str, action: callable)`**
  - Creates a command and automatically adds it to the list of commands.

## Setting Up Scripts in Your CustomCMDDB

### Starting Out

1. **Importing the Main File:**
   - To utilize functions and classes from the main file, import it using either:
     ```python
     import __main__
     ```
     or for a cleaner syntax:
     ```python
     from __main__ import *
     ```

2. **Defining the `main` Function:**
   - All executable code within your script should be encapsulated in a function named `main`. This function will be automatically executed just before the startup behavior.

### Example:

```python
# Importing the Main File
from __main__ import *

# Defining the main Function
def main():
    # Your script code here
    print("Hello, World!")
```

## Custom Commands

Unlock the full potential of the API by creating custom commands for the command line. The API seamlessly adds any initialized command class to the list of available commands.

There are two approaches to crafting a command: assigning a function to the command or using a lambda expression.

1. **Assigning a Function to a Command**

    Instead of using `hello()` as the input, provide the function name itself:

    ```python
    # Importing the Main File
    from __main__ import *

    # Command Behavior Function
    def hello():
        print("Hello, World!")

    # Defining the main Function
    def main():
        Command("hello", hello)
    ```

2. **Lambda Expression**

    Lambda expressions are ideal for one-time-use functions:

    ```python
    # Importing the Main File
    from __main__ import *

    # Defining the main Function
    def main():
        Command("hello", lambda: print("Hello, World!"))
    ```
