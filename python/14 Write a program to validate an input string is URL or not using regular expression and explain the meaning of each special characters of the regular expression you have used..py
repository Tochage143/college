import re


def is_valid_url(url):
    url_pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(:[0-9]+)?(/[-a-zA-Z0-9@:%_+.~#?&//=]*)?$'

    if re.match(url_pattern, url):
        return True
    else:
        return False


# Input from the user
url = input("Enter a URL to validate: ")

if is_valid_url(url):
    print("The URL is valid.")
else:
    print("The URL is not valid.")
