import re
pattern="a{2,3}"
#pattern="a+"
#a*
#a?
#a{2}
#a{2,3}   min2 max3

matcher=re.finditer(pattern,"aaaaabababababaaabababababaaababab")
count=0
for match in matcher:
    print(match.start(),match.group())
    count+=1
print("count:",count)