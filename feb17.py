# String method
# string 25 functions 

str = " Python is a high level programming language 1234567890 "
# 1. capitalize() : converts the first character of the string to uppercase and the rest to lowercase
print("Capitalize: ",str.capitalize())

# 2. casefold() : converts the string to lowercase
print("Casefold: ",str.casefold())

# 3. center() : returns a centered string of a specified width
print("Center: ",str.center(50,"*"))

# 4. count() : returns the number of occurrences of a substring in the string
print("Count: ",str.count("a"))

# 5. encode() : returns an encoded version of the string
print("Encode: ",str.encode("utf-8"))

# 6. endswith() : returns True if the string ends with a specified suffix, otherwise returns False
print("Endswith: ",str.endswith("0 "))

# 7. expandtabs() : returns a copy of the string where all tab characters are
# replaced with spaces
print("Expandtabs: ",str.expandtabs(4))

# 8. find() : returns the lowest index of the substring if it is found in
# the string, otherwise returns -1
print("Find: ",str.find("a"))

# 9. format() : formats the string using placeholders
print("Format: {} is a programming language".format("Python"))

# 10. format_map() : formats the string using a mapping
print("Format_map: {name} is a programming language".format_map({"name":"Python"}))

# 11. index() : returns the lowest index of the substring if it is found in
# the string, otherwise raises a ValueError
print("Index: ",str.index("a"))

# 12. isalnum() : returns True if all characters in the string are 
# alphanumeric, otherwise returns False
print("Isalnum: ",str.isalnum())

# 13. isalpha() : returns True if all characters in the string are alphabetic
# otherwise returns False
print("Isalpha: ",str.isalpha())

# 14. isdecimal() : returns True if all characters in the string are decimal
# characters, otherwise returns False
print("Isdecimal: ",str.isdecimal())

# 15. isdigit() : returns True if all characters in the string are digits
# otherwise returns False
print("Isdigit: ",str.isdigit())

# 16. isidentifier() : returns True if the string is a valid identifier, otherwise
# returns False
print("Isidentifier: ",str.isidentifier())

# 17. islower() : returns True if all characters in the string are lowercase,
# otherwise returns False
print("Islower: ",str.islower())

# 18. isnumeric() : returns True if all characters in the string are numeric,
# otherwise returns False
print("Isnumeric: ",str.isnumeric())

# 19. isprintable() : returns True if all characters in the string are printable
# otherwise returns False
print("Isprintable: ",str.isprintable())

# 20. isspace() : returns True if all characters in the string are whitespace,
# otherwise returns False
print("Isspace: ",str.isspace())

# 21. istitle() : returns True if the string is a titlecased string
# otherwise returns False
print("Istitle: ",str.istitle())

# 22. isupper() : returns True if all characters in the string are uppercase,
# otherwise returns False
print("Isupper: ",str.isupper())

# 23. join() : returns a string that is the concatenation of the strings in an
# iterable
print("Join: ",",".join(str))

# 24. ljust() : returns a left-justified string of a specified width
print("Ljust: ",str.ljust(50,"*"))

# 25. lower() : returns a copy of the string with all characters in lowercase
print("Lower: ",str.lower())

