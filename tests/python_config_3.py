import sys

SYS = {"VERSION": sys.hexversion}

A1 = {"B1": {"c1": 1, "C2": 2, "c3": 3}, "B2": {"c1": "a", "c2": True, "c3": 1.1}}

A2 = {
    "b1": {"c1": "f", "C2": False, "c3": None},
    "b2": {"c1": 10, "c2": "YWJjZGVmZ2g=", "c3": "abcdefgh"},
}

del sys
