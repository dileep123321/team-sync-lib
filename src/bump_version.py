import toml

pyproject = toml.load("pyproject.toml")
current = pyproject["project"]["version"]

major, minor, patch = map(int, current.split("."))

patch += 1
new_version = f"{major}.{minor}.{patch}"

pyproject["project"]["version"] = new_version

with open("pyproject.toml", "w") as f:
    toml.dump(pyproject, f)

print(new_version)
