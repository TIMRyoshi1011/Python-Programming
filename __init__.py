#Encoding: UTF-8
"""Test your luck with a fourtune cookie.

This video game is basic, straightforward, and quick to play. A fortune cookie is a 
cookie with a piece of paper with a little statement inscribed in it. This statement 
contains a life message. Each fortune cookie contains a different message for your life.
By choosing a random cookie you will be letting luck work for you.

As soon as you click on one of the choices, you will receive your message. The message 
that will come out has already been predestined for you. It may contain a secret, a tip, 
a teaching for your future, or an important warning sign.

Each player receives a distinct fortune cookie, which holds a different message. As a 
result, your daily message will be determined by your luck.
"""
# * Imports
import functools as fn
import json
import pathlib
from typing import Callable, Final

import rich.console
import rich.traceback

# * Metadata
__authors__ = (
    "Joseph Lina",
    "Jeremy Lusuegro",
    "John Kamantigue",
    "Keizel Salvador",
    "Marcus Timothy Ramos",
    "Tyrone Tolentino",
    "Viktor Harold Marticio",
)
__version__ = "0.1.0" # Major.Minor.Patch
__stage__ =  "alpha"

# Constants
# ! NOTE: I haven't tested any of these constants yet
ROOT: Final = pathlib.Path(__file__).parent.as_posix() # Root folder
CFG: Final = pathlib.Path(f"{ROOT}/cfg").as_posix()
ASSETS: Final = pathlib.Path(f"{ROOT}/assets").as_posix()
SFX: Final = pathlib.Path(f" {ASSETS}/sfx").as_posix()
IMG: Final = pathlib. Path(f"{ASSETS}/img").as_posix()

console: Final[rich.console.Console] = rich.console.Console()

with pathlib.Path(f" {CFG}/dev.json").open("r") as file:
    dev: dict = json.load(file)

with pathlib.Path(f"{CFG}/user-settings.json").open("r") as file:
    settings: dict = json.load(file)

# * Globals
rich.traceback.install(show_locals=True)


def deprecated(_function=None, /, *, message: str = ""):  # noqa: CFQ004
    """Mark a function as deprecated.

    Mark a decorated function as deprecated. This will print a warning that the given 
    function while still usable is considered obsolete, and that you are recommended to 
    use a suitable replacement.

    ### Parameters
    message: 'str = ""
        - Deprecation message.

    ### Usage
    ```py
    import fortune_cookie

    # It is important to add the
    # parentheses at the end of
    # this decorator.
    @fortune_cookie.deprecated()
    def function(...):
        ...
        return ...
    ```
    """

    def _decorated (function: Callable):
        @fn.wraps (function)
        def _wrapper(*args, **kwargs):
            if __debug__:
                WARN = "[bold black on yellow] WARN [/]"

                if message:
                    console.print(f"{WARN} (message)")
                else:
                    console.print(
                    f"(WARN) [bright_magenta]{function._name_} (/) is deprecated.",
                    )

            return function(*args, **kwargs)

        return _wrapper

    if function is None:
        return _decorated
    
    return _decorated(function)
