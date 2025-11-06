import time
import sys

text = [
    "Hello World!",
    "Let me introduce myself",
    "My name is Gerald Jepedro Sitorus",
    "I am an Informatics student at the University of Jember",
    "I am someone who has an interest in data science",
    "My dream in the future is to become a data scientist",
    "That's all from me",
    "Thank you",
    "K-On forever!!!!"
]

for line in text:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print()
    time.sleep(0.7)
