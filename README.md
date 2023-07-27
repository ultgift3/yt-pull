# Description

Short and ill written script for extracting a transcript of a YouTube Video. Too many unnecessary  dependencies, but does the job.

Thank you [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) and [clipboard](https://pypi.org/project/clipboard/) for saving my day!


# Installation

```
$ pip install yt-pull
```

# Usage
```
$ yt-pull "https://www.youtube.com/watch?v=some-ytvideo-id"
```

Options:

> `-o, --output`:
>> Path for saving the transcript to a file. (optional)

> `-s, --separator`:
>> Seperator for joining lines. \[default: '&nbsp; '\]

> `-l, --lang`:
>> Transcript language; must be provided by the source otherwise, error will occur. \[default: en\]

> `--help`:
>> Show help message.
