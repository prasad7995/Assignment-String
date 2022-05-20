import re

def find(string):
    x = '[@_!$%^&*()<>?/\|}{~:]#'
    special_char=re.compile(x)
    
    if special_char.search(string) == None:
        return "string is accepted"
    else:
        return "string not accpeted"
   

s="Python is a high level programming language"
print(find(s))
