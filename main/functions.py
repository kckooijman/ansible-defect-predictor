import os
import re
from io import StringIO


def load(path):
    """ Returns a StringIO object representing the content of the file at <path>,
        if any; None otherwise """
    if not os.path.isfile(path):
        return None

    content = StringIO()
    with open(path, 'r') as file:
        for line in file.readlines():
            content.write(re.sub(r'\s{2,2}', '\\t', line).expandtabs(2))

    return content
