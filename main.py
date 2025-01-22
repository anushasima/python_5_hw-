
import math
from idlelib.debugger_r import restart_subprocess_debugger


def convert_to_hashtag(some_text):
    some_word = some_text.strip().split()
    capitalize_word = [word.capitalize() for word in some_word]
    hashtag = "#" + "".join(capitalize_word)
    return hashtag[:140] if len(hashtag) > 140 else hashtag


some_test = input("enter sentence or one word: ")
result = convert_to_hashtag(some_test)
print(result)