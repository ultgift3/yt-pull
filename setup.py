
__version__ = "0.0.1"
__description__ = (
    "Short and ill written script for extracting a transcript of a YouTube Video. "
    "Too many unnecessary  dependencies, but does the job."
    )
__author__ = "Gwansuk Oh"

from distutils.core import setup

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name="yt-pull",
    version=__version__,
    description=__description__,
    author=__author__,
    url="https://github.com/ultgift3/yt-pull",
    download_url="https://github.com/ultgift3/yt-pull/archive/refs/tags/ytpull.tar.gz",
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'yt-pull = ytpull:main',
        ],
    },
)
