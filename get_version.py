#!/usr/bin/python3

import json
import sys

pkg_path = sys.argv[1]
version_path = sys.argv[2]
build_version = sys.argv[3]

with open(pkg_path, "r") as f:
    pkg_data = json.load(f)

    version = pkg_data["version"]

    with open(version_path, "w") as f:
        f.write(f"{version}.{build_version}\n")
