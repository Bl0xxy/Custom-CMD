# Configuration System
- [Back to README.md](README.md)

## Values
- `CTRL_C_EXIT` | bool | Should KeyboardInterrupt terminate the program?
- `STARTING_DIRECTORY` | str/path | What should be the starting directory of the program?
- `START_MESSAGE` | str | The initial message displayed at the program's start, often used to inform the user about the OS version and copyright information.
- `PYTHON_INSTALL_PATH` | str/path | The path to your Python installation; ensure it points to the correct python.exe or any other executable that runs Python.
- `DEFAULT_COLOR` | str | The default colors for the CLI.

### Path Variables
Just like in Python, the backslash character is used as an escape key. Example: `\\n` for a newline.

In path variables within JSON, you must use two backslashes.

### Default Values
If a value is not included in your config file, it will automatically be replaced with the default value. This is handy if you want to maintain the default value without manually entering it.

### Colors
Color attributes are specified by TWO hex digits – the first corresponds to the background, the second to the foreground. Each digit can be any of the following values:

    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White

Example: `02` for a black background with green text.

## How Do I Create The File
In the same directory as `main.pyc`, create a file named "config.json" and enclose it in curly braces: `{}`.

Now that you have these braces, you're ready to input values. Let's use `CTRL_C_EXIT` as an example. To assign it a value, add a colon. It should now look like this:

```json
"CTRL_C_EXIT":
```

Another crucial point is for this to be inside the braces. Now it should appear as:

```json
{"CTRL_C_EXIT": }
```

Without a value, you will encounter an error. String values are text values, so you can input essentially any text within double quotes. A bool value is a boolean value, which can be either **`true`** or **`false`**, and is case-sensitive. A path variable is similar to a str, but you need to enter a valid path. In this case, **`CTRL_C_EXIT`** is a boolean value, so you would enter **`true`** or **`false`** for the value. Now it looks like:

```json
{"CTRL_C_EXIT": true}
```

And it works! If you want to add more values, you can use a comma to separate values.

### Example
```json
{
  "START_MESSAGE": "Welcome To CustomCMD!\n",
  "STARTING_DIRECTORY": "C:\\Windows\\System32"
}
```
