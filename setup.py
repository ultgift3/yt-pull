
__version__ = "0.0.1"
__description__ = (
    "Short and ill written script for extracting a transcript of a YouTube Video. "
    "Too many unncessary dependencies, but does the job."
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
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'yt-pull = ytpull:main',
        ],
    },
)
