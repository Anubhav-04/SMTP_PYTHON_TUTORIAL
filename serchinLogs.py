import re

# with open("app.log",'r') as f:
#     for l in f:
#         if "ERROR" in l or "CRITICAL" in l:
#             print(l.strip())


pattern = re.compile(r'.* - (ERROR|CRITICAL) - *')
with open("app.log",'r') as f:
    for l in f:
        if pattern.match(l):
            print(l.strip())