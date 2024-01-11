import os
from pathlib import Path

def generate_file_structure(package_name, file_list):
    for filepath in file_list:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass  # create an empty file


if __name__ == "__main__":
    package_name = "mongodb_connect"

    file_list = [
        ".github/workflows/ci.yaml",
        f"src/{package_name}/__init__.py",
        f"src/{package_name}/mongo_crud.py",
        "tests/__init__.py",
        "tests/unit/__init__.py",
        "tests/integration/__init__.py",
        "init_setup.sh",
        "requirements.txt",
        "setup.py",
        "setup.cfg",
        "pyproject.toml",
        "tox.ini",
        "experiments/experiments.ipynb",
    ]

    generate_file_structure(package_name, file_list)
