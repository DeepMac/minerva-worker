import json
import urllib.request
from importlib.metadata import version

PACKAGE_NAME = "minerva-worker"


def semver_tuple(v: str) -> tuple[int, int, int]:
    """Parse SemVer string into major, minor, patch tuple."""
    major, minor, patch = map(int, v.split("."))
    return (major, minor, patch)


def check_for_update() -> bool:
    installed_version = version(PACKAGE_NAME)

    with urllib.request.urlopen(f"https://pypi.org/pypi/{PACKAGE_NAME}/json") as response:
        data = json.load(response)

    latest_version = data["info"]["version"]

    if semver_tuple(latest_version) > semver_tuple(installed_version):
        print(f"Update available: {installed_version} → {latest_version}")
        print(f"To update run: pip install --upgrade {PACKAGE_NAME}")
        return True
    elif semver_tuple(latest_version) < semver_tuple(installed_version):
        print("Note: You are currently running a development version...")

    return False
