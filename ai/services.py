import random
import string


# For unique temp id in every new attempt
def unique_id():
    numbers = string.digits
    words = string.ascii_letters
    new_id = ""
    length = 10
    for _ in range(length):
        random_number = random.choice(numbers)
        random_word = random.choice(words)
        new_id = new_id + random_number + random_word
        if len(new_id) == length:
            break
    return new_id
