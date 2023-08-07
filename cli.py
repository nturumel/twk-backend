# twk_backend/cli.py
import subprocess


def test():
    subprocess.run(["pytest"])


def lint():
    subprocess.run(["flake8", "twk_backend", "tests"])


def typecheck():
    subprocess.run(["mypy", "twk_backend", "tests"])


def format_code():
    subprocess.run(["black", "twk_backend", "tests"])


def checkformat():
    subprocess.run(["black", "--check", "twk_backend", "tests"])


def docs():
    subprocess.run(["sphinx-build", "docs/source", "docs/build"])


def launch():
    subprocess.run(["python", "twk_backend/router.py"])
