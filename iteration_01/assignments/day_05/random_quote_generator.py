# Starter file for students to create a Random Quote Generator
import random


# Step 1: Import any necessary modules
# Step 2: Define a function to load quotes from a file when called
# Step 3: Define a function that returns a random quote when called
# Step 4: Define a main function that runs the program. Make sure to call the function.

# Functions takes in filename parameter and returns list of strings with lines from file
from pathlib import Path

BASE_DIR = Path(__file__).parent
quotes_path = BASE_DIR / "quotes.txt"


def load_quotes(filename) -> list[str]:
    with open(filename, "r") as file:
        return file.read().splitlines()
    

# Function takes in list of strings and randomly chooses one to return
def get_random_quote(quotes: list[str]) -> str:
    return random.choice(quotes)

# Runs program. Main() is the only function called so that it calls the other functions appropriately and controls logic flow.
def main():
    strings = load_quotes(quotes_path)
    print(strings)
    returnVal = get_random_quote(strings)
    print(returnVal)
    return None 

main()





