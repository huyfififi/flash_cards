import os
import random
import sys


DEFAULT_TXT_FILE = "naturalization_test.txt"


if __name__ == "__main__":
    cards = []
    with open(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TXT_FILE, "r") as f:
        for line in f.readlines():
            cards.append(line.replace("\n", ""))

    print(f"Successfully read {len(cards)} questions.")
    print("Enter `quit` or `exit` to finish.")

    counter = 1

    while True:
        question = random.choice(cards)
        print("=" * os.get_terminal_size().columns)
        print(f"[{counter}]\t{question}")
        counter += 1

        command = input(">>> ")
        if command in ["quit", "exit"]:
            break

    print("=" * os.get_terminal_size().columns)
    print("Well Done!")
