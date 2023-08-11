import re
import string


def split_html_tags(input_string):
    pattern = r"<[^<>]+>|[^<>]+"
    tags = re.findall(pattern, input_string)
    return tags


def test_subfinder():
    print(split_html_tags("<div><br>hello</br></div>"))
