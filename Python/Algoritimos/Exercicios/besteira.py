import sys
from rich import print
from time import sleep

def print_lyric():
    lyrics = [
        ("Sometimes I", 1.0),
        ("Need to remember just to breathe", 1.9),
        ("Sometimes I", 1.9),
        ("Need you to stay away from me", 1.9),
        ("Sometimes I'm", 1.7),
        ("In disbelief I didn't know", 1.9),
        ("Somehow I", 1.7),
        ("Need you to go", 2.0),
        ("Don't stay", 1.0),
        ("Forget our memories", 1.5),
    ]
    for line, delay in lyrics:
        print(line)
        sleep(delay)

print_lyric()