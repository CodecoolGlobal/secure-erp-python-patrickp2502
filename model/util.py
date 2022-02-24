import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    alphabet_string_upper = "".join([char for char in string.ascii_uppercase if char.isalpha()])
    alphabet_string_lower = "".join([char for char in string.ascii_lowercase if char.isalpha()])
    digits = "".join(["1","2", "3", "4", "5", "6", "7", "8", "9", "0"])
    random_id = []
    random_id.append("".join(random.choices(alphabet_string_lower, k=number_of_small_letters)))
    random_id.append("".join(random.choices(alphabet_string_upper, k=number_of_capital_letters)))
    random_id.append("".join(random.choices(digits, k=number_of_digits)))
    random_id.append("".join(random.choices(allowed_special_chars, k=number_of_special_chars)))
    random.shuffle(random_id)
    random_id_string = "".join(random_id)
    return random_id_string
