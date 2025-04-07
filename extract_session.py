import sys
import re

def extract_session(content):
	lines = content.split("\n")
	session_lines = [l for l in lines if "JSESSIONID" in l]
	print(session_lines)
	match = re.search('(?:")([0-9A-Fa-f]+)(?:")', session_lines[0])
	return match.group(1)
