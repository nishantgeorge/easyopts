# easyopts - Stupid simple command-line options parsing for Python 3

## Install

```bash
pip install easyopts
```

## Usage

Arguments should be in the form of --\<opt-name\> \<opt-value\> pairs.

Example:
```bash
script.py --option1 value1 --option2 value2
```

Option name requirements:
- should start with a letter.
- May contain letters, numbers and hyphens
- Both upper case and lower case letters are allowed

If options are repeated, the value specified last will be used.

Use the `parseargs` function to parse arguments
Catch the `OptionParsingError` for parsing errors.

```python
import sys

from easyopts import parseargs, OptionParsingError

args = sys.argv[1:]
try:
    opts = parseargs(args)
    # Now `opts` is a dict of options and their values
except OptionParsingError as ex:
    print("Error parsing options:", str(ex))
    print("USAGE: ...")
    sys.exit()
```