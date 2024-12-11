import os
from pathlib import Path
import requests
from dotenv import load_dotenv

def fetch_input(filename):
    load_dotenv()

    stripped_filename = os.path.splitext(os.path.basename(filename))[0]
    year = os.path.basename(Path(filename).parent)
    day = stripped_filename.split("day")[1]
    directory = Path("inputs")
    input_path = directory / f"day{day}.txt"

    if input_path.exists():
        with open(input_path, "r") as file:
            return file.read()
        
    directory.mkdir(parents = True, exist_ok= True)
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookie = os.getenv("AOC_COOKIE")
    headers = {"Cookie" : f"session={cookie}",
                                "User-Agent": "Python Script - Advent of Code Input Fetcher"}
    try:
        response = requests.get(url, headers = headers)
        response.raise_for_status()
        with open(input_path, "w") as file:
            file.write(response.text)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None