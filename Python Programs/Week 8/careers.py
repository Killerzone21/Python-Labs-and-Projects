careers = ['plumber','programmer','artist','bartender','server','host']
print(careers.index('artist'))
if 'artist' in careers:
    print('yes')
careers.append('driver')
careers.insert(0,'gardener')
print(careers)
for i in range (len(careers)):
    print(careers[i])
print(careers[0])
print(careers[len(careers)-1])
last = careers.pop()
print(last)
print(careers.pop(2))
careers.remove('plumber')
print(careers)


