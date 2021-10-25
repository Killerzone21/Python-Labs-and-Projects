import re

phoneNumRegex = re.compile(r'.\d{3}.-\d{3}-\d{4}')
mo = phoneNumRegex.search('Here is a number: (555)-123-1234 and 456-789-123')
print("Phone is: " + mo.group())

CreditCardRegex = re.compile(r'\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d')
mo2 = CreditCardRegex.search('Here is a card number: 5519-1234-4567-8901 and 2045-1234-456-4124')
print("Credit Card number is: " + mo2.group())


print(re.findall(r'\D{3}\d{4}',"Bulls are named: ABC6789, BCG9998 and TRH0001"))


repNameRegex = re.compile(r'Officer \w+')
print(repNameRegex.sub('UNKNOWN', 'The assailant was apprehended by Officer Thawne and Officer Joe today at 10:00 pm'))

repNameRegex = re.compile(r'Officer (\w)(\w*)')
print(repNameRegex.sub(r'\2***', 'Officer Able told Officer Baker to say nothing to Officer Charlie'))

atRegex = re.compile(r'at')
print(atRegex.findall('The cat in the hat sat on a fat bat'))
