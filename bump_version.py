import tomllib
import re

file = "pyproject.toml"

# Read version
with open(file, "rb") as f:
    data = tomllib.load(f)

current = data["project"]["version"]
major, minor, patch = map(int, current.split("."))

# bump patch
patch += 1
new_version = f"{major}.{minor}.{patch}"

# Replace inside file
with open(file, "r") as f:
    content = f.read()

content = re.sub(r'version\s*=\s*"[0-9]+\.[0-9]+\.[0-9]+"',
                 f'version = "{new_version}"',
                 content)

with open(file, "w") as f:
    f.write(content)

print(new_version)
