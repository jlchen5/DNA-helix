import time
import os

def clear_console():
    # Clear console for Windows, Mac, and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dna(length=20, delay=0.1):
    pattern = [
        "A-----T",
        " T---A ",
        "  G-G  ",
        "   C   ",
        "  G-G  ",
        " T---A ",
        "A-----T",
        " T---A ",
        "  G-G  ",
        "   C   "
    ]
    
    while True:
        for i in range(len(pattern)):
            clear_console()
            for j in range(length):
                print(pattern[(i + j) % len(pattern)])
            time.sleep(delay)

if __name__ == "__main__":
    print_dna(20, 0.1)
