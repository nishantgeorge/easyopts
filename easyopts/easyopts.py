"""
Easy command-line options for Python scripts.
"""

import re
import sys
from typing import Iterable


class OptionParsingError(Exception):
    """
    Raised when there is an error parsing options.
    """


def _validate_opt_name_arg(opt_name: str):
    """
    Validates an option name argument. Raises an OptionParsingError on failure.
    """
    if not opt_name.startswith("--"):
        raise OptionParsingError(f"The '{opt_name}' argument does not begin with '--'")
    opt_name = opt_name[2:]
    if re.match(r'^[a-zA-Z][a-zA-Z0-9-]*$', opt_name) is None:
        raise OptionParsingError(
            f"The '{opt_name}' option name is invalid. Option names must "
            "start with a letter and "
            "may contain letters, numbers and hyphens. "
            "Both upper case and lower case letters are allowed "
        )


def parseargs(args: Iterable[str]):
    """
    Passes arguments into a dict of options.
    Expects an iterable of only the option arguments, excluding the script argument.

    Arguments should be in the form of --<opt-name> <opt-value> pairs.

    opt-name requirements:
    - should start with a letter.
    - May contain letters, numbers and hyphens
    - Both upper case and lower case letters are allowed

    If options are repeated, the value specified last will be used.
    """
    if not len(args) % 2 == 0:
        raise OptionParsingError(f"Odd number of arguments, some option does not have a value")
    opts = {}
    # Make a copy of the arguments since we're going to modify the list
    args = list(args)
    while len(args) > 0:
        opt_name = args.pop(0)
        opt_val = args.pop(0)
        _validate_opt_name_arg(opt_name)
        # Get rid of the leading '--'
        opt_name = opt_name[2:]
        opts[opt_name] = opt_val
    return opts
