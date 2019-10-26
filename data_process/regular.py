import re
pattern = re.compile(r'hello.*!')
# 开头有个'a'，match()匹配不上，但是search()可以匹配上
match = pattern.match('ahello, peter! How are you?')
match1 = pattern.search('ahello, peter! How are you?')


if match:
    print(match.group())
else:
    print("None match")
if match1:
    print(match1.group())
else:
    print("None match1")
