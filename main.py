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

    # if endswith tscn, just lint the file.
    if sys.argv[1].endswith(".tscn"):
        lint_tscn_file(os.path.abspath(sys.argv[1]))
        sys.exit(0)
    # if it's the project.godot, lint all tscn files recursively.
    elif sys.argv[1].endswith("project.godot"):
        project_root = res_search.find_project_root(os.path.abspath(sys.argv[1]))
        if project_root is None:
            error_print("Could not find the Godot project root.")
            sys.exit(1)
        for root, dirs, files in os.walk(project_root):
            # get the abspath
            for file in files:
                if file.endswith(".tscn"):
                    lint_tscn_file(os.path.join(root, file))
        sys.exit(0)
