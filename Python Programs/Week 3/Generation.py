Gen = int(input("Enter the year you were born:"))

if Gen > 1900 and Gen < 1925:
    print("GI Generation")
elif Gen > 1924 and Gen < 1943:
    print("Silent Generation")
elif Gen > 1942 and Gen < 1965:
    print("Baby Boomers")
elif Gen > 1964 and Gen < 1980:
    print("Generation X")
elif Gen > 1979 and Gen < 2001:
    print("Millennials")
elif Gen > 2000 and Gen < 2016:
    print("Generation Z")
else:
    print("Not in a specific Generation type")
