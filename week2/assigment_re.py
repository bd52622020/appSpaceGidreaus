import re

pattern = "^We.*Data$"
txt = "We love programming with Big Data"

x = re.search(pattern, txt)
if x == None:
    print("Match not found")
else:
    print("Match found: ", x.group())
