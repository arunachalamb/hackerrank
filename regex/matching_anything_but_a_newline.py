regex_pattern = r"[^\n]{3}\.[^\n]{3}\.[^\n]{3}\.[^\n]{3}$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
