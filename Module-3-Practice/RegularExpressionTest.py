import re
print(re.sub(r'[ad]','*',"abcd abcde def"))
print(re.sub(r'[BC]','bc',"ABCD BCDE"))