from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="plaz_beta",
    version="0.0.1",
    author="Linden",
    author_email="<Linden@aktfast.net>",
    description="Plaz_Beta - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linden1910/plaz_beta",
    download_url="https://github.com/linden1910/plaz_beta.git",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'plaz_beta=plaz_beta:main',
        ],
        'qtpyvcp.vcp': [
            'plaz_beta=plaz_beta',
        ],
    },
)
