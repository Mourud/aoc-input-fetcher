# Advent of Code Input Fetcher

`aoc_input_fetcher` is a Python package that automates fetching input files for [Advent of Code](https://adventofcode.com) challenges, assuming a specific file structure for your project.

---

## Features

- Automatically fetches input for Advent of Code puzzles from file name and directory sturcture.
- Supports user-provided session cookies for authentication.
- Simplifies managing input files for each day of the challenge.
- Easy to integrate with your existing workflow.

---

## Installation

You can install the package via pip:

```bash
pip install aoc_input_fetcher
```

## Usage

### Setup

To use aoc_input_fetcher, you need to:
	1.	Log in to Advent of Code and copy your session cookie.
	2.	Save the cookie to a .env file in the following format:
```bash
AOC_COOKIE=<your_session_cookie>
```


### File Structure

The package expects the following file structure for your Advent of Code project:


```
aoc/2024/
├── day1.py
├── day5.py
├── inputs/
│   ├── day1.txt
│   └── day5.txt
```
### Fetch Input

Example of fetching input for Day 1:
```python
from aoc_input_fetcher import fetch_input

input = fetch_input(__input__)
```
This will download the input for Day 1 and save it to inputs/day1.txt in the project root. The input is returned as a string as well.

**Demo**

Here’s a quick demo of how to use the package:

from aoc_input_fetcher import fetch_input
```python
from aoc_input_fetcher import fetch_input

def main():
    input = fetch_input(__file__)
    if input is None:
        return
    formatted_input = format_input(input)
    print(part1(formatted_input))
    print(part2(formatted_input))
main()
```
For a detailed look at how I have been using it check out my [Advent of Code repository](https://github.com/mourud/advent-of-code/tree/main/2024)

## Requirements
This package requires:
	•	Python 3.6 or newer
	•	requests library (automatically installed with the package)
    •   python-dotenv library (automatically installed with the package)

## Contributing
Contributions are welcome! If you have ideas for improvements or find bugs:
	1.	Fork the repository.
	2.	Make your changes.
	3.	Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Support
If you encounter issues or have questions, feel free to open an issue on GitHub.

