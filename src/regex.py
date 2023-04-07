import re

s = ""

pattern = r"^\w+@\w+\.\w{1,4}$"
repattern = re.compile(pattern)
if repattern.search(s) is not None:
    print("Yes")
else:
    print("No")

pattern = r"ru(?=r)"
repattern = re.compile(pattern)
print(repattern.sub("ra", s))
