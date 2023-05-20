import re
import os
from print import *

def find_project_root(file_path):
    """Find the root directory of the Godot project."""
    print("Trying to find res:// root of: ")
    print(file_path)
    dir_path = os.path.dirname(file_path)
    while True:  # We'll break manually if we reach the root
        potential_root = os.path.join(dir_path, 'project.godot')
        if os.path.exists(potential_root):
            return dir_path
        parent_dir_path = os.path.dirname(dir_path)
        if parent_dir_path == dir_path:  # Check if we've reached the root
            break
        dir_path = parent_dir_path
    return None

def check_resource_validity(tscn_path):
    """Check the validity of resource references in the TSCN file."""
    project_root = find_project_root(tscn_path)
    if project_root is None:
        error_print("Could not find the Godot project root.")
        return

    with open(tscn_path, 'r') as tscn_file:
        tscn_content = tscn_file.read()

    # Find all resource paths
    resource_paths = re.findall(r'res://[^\s"]+', tscn_content)

    print(f"{resource_paths}")
    print(f"Found {len(resource_paths)} resource references. Checking...")

    invalid_resources = []

    for resource_path in resource_paths:
        full_path = os.path.join(project_root, resource_path.replace('res://', ''))
        if not os.path.exists(full_path):
            invalid_resources.append(resource_path)
    
    if invalid_resources:
        error_print("The following resources are invalid:")
        for resource in invalid_resources:
            error_print(resource)
    else:
        success_print("All resource references are valid.")
