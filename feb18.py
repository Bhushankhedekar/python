	# 							## String Functions Practices ##
		
	# 1. Write a Python program to convert the given string "hello world" to uppercase.
str = "hello world"
print("Upper: ",str.upper())

  	# 2. Convert the string "Python Programming" to lowercase.
str = "Python Programming"
print("Lower :",str.lower())

	# 3. Capitalize the first letter of "hello python learners".
str = "hello python learners"
print("Capitalize :",str.capitalize())

	# 4. Convert "welcome to python" to title case.
str = "welcome to python"
print("Title: ",str.title())

	# 5. Remove leading and trailing spaces from the string " Python String Functions " using strip().
str = " Python String Functions "
print("Strip: ",str.strip())

	# 6. Remove only trailing spaces from "Hello World " .
str = "Hello World "
print("Rstrip: ",str.rstrip())

	# 7. Remove only leading spaces from " Learn Python".
str = " Learn Python"
print("Lstrip: ",str.lstrip())

	# 8. Split the string "apple banana grape" into a list using split().
str = "apple banana grape"
print("Split: ",str.split())

	# 9. Join the list ['Python', 'is', 'fun'] into a single string using join() with space as a separator.
list1 = ['Python', 'is', 'fun']
print("Join: "," ".join(list1))

	# 10. Convert the list ['A', 'B', 'C'] into a single string "A-B-C" using join().
list2 = ['A', 'B', 'C']
print("Join: ","-".join(list2))

	# 11. Find the index of the first occurrence of "Python" in "I love Python programming".
str = "I love Python programming"
print("Index of Python: ",str.find("Python"))

	# 12. Find the last occurrence of "o" in "Hello World".
str = "Hello World"
print("Last occurrence of o: ",str.rfind("o"))

	# 13. Replace "Java" with "Python" in the string "I love Java".
str = "I love Java"
print("Replace Java with Python: ",str.replace("Java","Python"))

	# 14. Check if the string "Hello World" starts with "Hello".
str = "Hello World"
print("Starts with Hello: ",str.startswith("Hello"))

	# 15. Check if the string "example.txt" ends with ".txt".
str = "example.txt"
print("Ends with .txt: ",str.endswith(".txt"))

	# 16. Count the occurrences of "o" in "Hello, how are you?".
str = "Hello, how are you?"
print("Count of o: ",str.count("o"))

	# 17. Find the index of "r" in "programming".
str = "programming"
print("Index of r: ",str.index("r"))

	# 18. Try finding the index of "z" in "python" using index(), and observe the error.
try:
    str = "python"
    print("Index of z: ",str.index("z"))
except ValueError:
    print("ValueError raised because 'z' is not found in 'python'")

    #   19. find the last occurrence of "e" in "experience".
str = "experience"
print("Last occurrence of e: ",str.rfind("e"))

    #   20. find the first occurrence of "e" in "experience".
print("First occurance :",str.find("e"))

    #   21. Check if the string "Python" contains only alphabets.
str = "Python"
print("is python contains only alphabets:",str.isalpha())

    #   22. Verify if "12345" contains only digits.
str = "12345"
print("is 12345 contains only digits:",str.isdigit())

    #   23. Check if "Python123" is alphanumeric.
str = "Python123"
print("Is python123 is alphanumeric:",str.isalnum())

    #   24. Test if the string " " consists of only spaces.
str = " "
print("Is string with only spaces:",str.isspace())

    #   25. Check if "12345" is numeric using.
str = "12345"
print("is string numeric:",str.isnumeric())

    #   26. Use format() to insert "Python" and "fun" into the string "{} is {}!".
print("{} is {}!".format("Python","fun"))

    #   27. Partition the string "python-programming-language" at "-".
str = "python-programming-language"
print("Partition the string at -:",str.partition("-"))

    #   28. Use rpartition() to split "one-two-three" from the right sing "-".
str = "one-two-three"
print("Rpartition the string at -:",str.rpartition("-"))

    #   29. Convert "PYTHON" to lowercase using casefold().
str = "PYTHON"
print("To lower case using casefold:",str.casefold())

    #   30. Convert "42" into a 5-character string padded with zeros using zfill().
str = "42"
print("Zero-padded string:",str.zfill(5))

    #   31. Check if "HELLO" is in uppercase.
str = "HELLO"
print("Is hello uppercase:",str.isupper())

    #   32. Verify if "hello" is in lowercase.
str = "hello"
print("Is hello lowercase:",str.islower())

    #   33. Check if "Python Programming" follows title case.
str = "Python Programming"
print("IS str follows title case:",str.istitle())

    #   34. Sort the characters of "banana" alphabetically.
str = "banana"
print("Sorted characters of banana:",sorted(str))

    #   35. Find the length of the string "Data Science".
str = "Data Science"
print("Length of th string data science:",len(str))

    #   36. Sort the characters of "The Kiran  Academy" alphabetically in descending Order.
str = "The Kiran  Academy"
print("Sorted characters of The Kiran Academy in descending order:",sorted(str))
