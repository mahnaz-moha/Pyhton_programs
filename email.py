import re
input1=input("")
re.search(r".+\@\w+\.\w+$",input1)

if re.search(r".+\@\w+\.\w+$",input1)==None:
    print("WRONG")
else:
    print("OK")

