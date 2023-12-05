# Read Me


## Installation
To get Python working, go to [Python Download](https://www.python.org/downloads/release/python-3120/) and get the embeddable package.  Then when running main.pyc make sure to have it run with your python.exe file in the folder.

## Configuration System
If you want to customize CustomCMD, then you are now able to!  With the configuration system, you can now change all kinds of things.  v1.0 introduced the configuration system with the only changable thing being whether or not KeyboardInterrupt ends the program.

### Values
- `CTRL_C_EXIT` | bool | Should KeyboardInterrupt end the program?
- `STARTING_DIRECTORY` | str/path | What should the starting directory of the program be?
- `START_MESSAGE` | str | The starting message at the beginning of the program, generally used to inform the user of the OS version and copyright information.
- `PYTHON_INSTALL_PATH` | str/path | The path of your Python installation; only works if you have Python installed and if you are putting the correct path to python.exe or any other executable that runs Python.
- `DEFAULT_COLOR` | str | The default colors for the CLI.

#### Default Values
If you don't include a value in your config file, don't worry as it will automatically be replaced with the default value.  This is useful if you want to keep the default value but don't know how to manually plug it in.

#### Colors
Color attributes are specified by TWO hex digits -- the first
corresponds to the background; the second the foreground.  Each digit
can be any of the following values:

    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White

Example: 02 for black background, green text.

### How Do I Make The File
In the same directory as main.pyc, make a file called "config.json" and make brackets like these: `{}`

Now that you have these brackets, you are ready to put values in.  Let's use `CTRL_C_EXIT` as an example.  To give it a value, add a colon.  It should look like this now: `"CTRL_C_EXIT":`  Another important thing is for this to be inside of the brackets.  Now it should look like this: `{"CTRL_C_EXIT":}`  Without a value, you will get an error.  str values are text values, so you can put basically any text that is inside of double quotes.  A bool value is a boolean value.  These values can either be `true` or `false` being case sensitive.  A path variable is just a str but you need to enter a valid path.  In this case, `CTRL_C_EXIT` is a boolean value so you would enter `true` or `false` for the value.  Now it looks like `{"CTRL_C_EXIT":true}` and it works!  Now when you do CTRL C the program exits!  If you want to add more values, you can add a comma.  For example, `{"START_MESSAGE": "Welcome To CustomCMD!\n", "STARTING_DIRECTORY": "C:\Windows\System32"}`

## Coming Soon
- Auto Updater via GitHub
- Additional Supported Libraries (Only Suggested Ones)
- Whatever Suggested
- Scripting API
