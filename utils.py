import re


def verify_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
