#!/usr/bin/env python3

import re
import os
import res_search
import res_valid
from print import *

def lint_tscn_file(filename):
    # check for missing resources
    res_search.check_resource_validity(filename)

    res_valid.check_ext_resource_validity(filename)
    res_valid.check_sub_resource_validity(filename)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python lint_tscn.py <filename>")
        sys.exit(1)

    lint_tscn_file(os.path.abspath(sys.argv[1]))
