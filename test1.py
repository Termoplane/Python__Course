import re

pattern = r"(\w+)-\1"
string = "test-test"

match = re.match(pattern, string)

print(match)