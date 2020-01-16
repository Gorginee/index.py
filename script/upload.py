import os

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_version(package) -> str:
    """
    Return version.
    """
    __: dict = {}
    with open(os.path.join(here, package, "__version__.py")) as f:
        exec(f.read(), __)

    return __["__version__"]


os.chdir(here)
os.system(f"poetry version {get_version('index')}")
os.system(f"poetry publish")
os.system("git tag v{0}".format(get_version("index")))
os.system("git push --tags")