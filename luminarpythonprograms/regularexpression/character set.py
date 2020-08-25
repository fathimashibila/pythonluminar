from re import *
pattern ="[A-z]"

matcher=finditer(pattern,"abx 7ZXy@")
for match in matcher:
    print(match.start(),match.group())
#"[a-z]" it will find all charcters from a to z
#"[A-Z]"
#"[abc]"
#"[a-zA-Z]"
#"[a-kA-Z]"
#"[0-9]"
#'[^0-9]" except 0 print all number
#"[^a-zA-Z0-9]"