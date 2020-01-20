Regex_Pattern = r"[\d]{2}[^\d][\d]{2}[^\d][\d]{4}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
