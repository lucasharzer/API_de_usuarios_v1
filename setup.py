from setuptools import setup, find_packages

with open("requirements.txt") as r:
    install_requires = r.read()

setup(
    name = "API_de_usuarios_v1",
    version = "0.0.1",
    description = "Rest API simple with Python and Flask ",
    url = "https://github.com/lucasharzer/API_de_usuarios_v1",
    author = "Lucas Harzer",
    author_email = "lucasmatos592@gmail.com",
    license = "BSD",
    packages = find_packages(),
    install_requires = [install_requires],
    zip_safe = False
)