import re


def extract_session(content):
    lines = content.split("\n")
    session_lines = [line for line in lines if "JSESSIONID" in line]
    print(session_lines)
    match = re.search('(?:")([0-9A-Fa-f]+)(?:")', session_lines[0])
    return match.group(1)
