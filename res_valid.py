import re
import os
from print import *

def check_ext_resource_validity(tscn_path):
    """Check the validity of ExtResource references in the TSCN file."""
    with open(tscn_path, 'r') as tscn_file:
        tscn_content = tscn_file.readlines()

    ext_resource_ids = set()
    instance_ids = set()

    for line in tscn_content:
        ext_resource_match = re.match(r'\[ext_resource .+ id="([^"]+)"', line)
        instance_match = re.match(r'.*instance=ExtResource\("([^"]+)"\)', line)

        if ext_resource_match:
            ext_resource_ids.add(ext_resource_match.group(1))
        if instance_match:
            instance_ids.add(instance_match.group(1))

    invalid_instance_ids = instance_ids - ext_resource_ids
    if invalid_instance_ids:
        error_print("The following external resource ids are invalid: ")
        for instance_id in invalid_instance_ids:
            error_print(instance_id)
    else:
        success_print("All instance ids are valid.")

def check_sub_resource_validity(tscn_path):
    """Check the validity of SubResource references in the TSCN file."""
    with open(tscn_path, 'r') as tscn_file:
        tscn_content = tscn_file.readlines()

    sub_resource_ids = set()
    subresource_instance_ids = set()

    for line in tscn_content:
        sub_resource_match = re.match(r'\[sub_resource .+ id="([^"]+)"', line)
        subresource_instance_match = re.match(r'.*SubResource\("([^"]+)"\)', line)

        if sub_resource_match:
            sub_resource_ids.add(sub_resource_match.group(1))
        if subresource_instance_match:
            subresource_instance_ids.add(subresource_instance_match.group(1))

    invalid_subresource_instance_ids = subresource_instance_ids - sub_resource_ids
    if invalid_subresource_instance_ids:
        error_print("The following subresource ids are invalid:")
        for subresource_instance_id in invalid_subresource_instance_ids:
            error_print(subresource_instance_id)
    else:
        success_print("All subresource instance ids are valid.")

