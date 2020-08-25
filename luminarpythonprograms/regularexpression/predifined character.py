#pattern="\s" it will check spaces
#pattern="\d" it will check digit[0-9]
# "\D"    except numbers
# "\w" all  numbers and letters
# "\W"   except numbers and letters


from re import *
pattern="\D"

matcher=finditer(pattern,"abx 7ZXy@")
matcher=finditer(pattern,"abx 7ZXy@")
for match in matcher:
    print(match.start(),match.group())