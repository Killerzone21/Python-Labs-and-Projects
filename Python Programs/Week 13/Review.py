import re

def checkPat(my_String):
    ssnRegex = re.compile(r".@.")
    mo = ssnRegex.search(my_String)
    print("ssn is " + mo.group())


checkPat("this@that")
checkPat('123@789')
checkPat('here@there')
