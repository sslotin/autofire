# Autofire

Ridiculously small package that allows creating command line interfaces in O(0) time with Google's [Python Fire](https://github.com/google/python-fire).

To install with pip, run: `pip install autofire`

## Usage

Say you have a file `example.py`:

```python
def sum(a, b):
    return a + b

class Calculator:
    def double(self, some_number):
        return 2*some_number

import math
```

Then, from the command line, you can just run:

```bash
fire example.py sum 2 3
fire example.py Calculator double 5
fire example.py Calculator double --some_number=15
fire example.py math log 6
```
