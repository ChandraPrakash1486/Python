import re
"""
This script demonstrates various regular expression (regex) operations using Python's `re` module.
The script performs the following operations:
1. Matches any character followed by 'h' at the beginning of the string.
2. Matches the pattern 'Ch' at the beginning of the string.
3. Searches for the pattern 'Tekwani' at the end of the string.
4. Finds all occurrences of zero or more 'a' characters.
5. Finds all occurrences of one or more 'a' characters.
6. Searches for zero or one occurrence of 'a'.
7. Matches 'Ch' or 'Ph' at the beginning of the string.
8. Finds all occurrences of any character except 'C' or 'P' followed by 'a'.
9. Finds all occurrences of the substring 'and'.
10. Searches for the first occurrence of either 'C' or 'P'.
11. Finds all occurrences of the dollar sign ('$').
12. Finds exactly one occurrence of 'C'.
13. Finds all occurrences of the substring 'ra' and iterates over them.
14. Finds one or more occurrences of the substring 'ra'.
15. Searches for at least one and at most three occurrences of the substring 'ra'.
16. Finds all occurrences of any digit.
17. Finds all occurrences of any non-digit character.
18. Finds all occurrences of any alphanumeric character.
19. Finds all occurrences of any non-alphanumeric character.
20. Searches for any whitespace character.
21. Finds all occurrences of any non-whitespace character.
22. Finds the word boundary match for 'Chandra'.
23. Finds all occurrences of 'chandra' ignoring case.
24. Finds all occurrences of 'Chandra' in a multiline string, considering each line separately.
Additionally, the script demonstrates the use of regex flags such as `re.IGNORECASE` and `re.MULTILINE`.
"""

text = "Chandra Prakash Tekwani"
pattern = re.compile(".h") #Pattern object
matches = pattern.match(text).group() #Match object
print(matches)

pattern = re.compile("^Ch") #Pattern object
matches = pattern.match(text).group() #match object
print(bool(matches))

pattern = re.compile("Tekwani$")
matches = pattern.search(text) #I am using search method here, as match method only matches the pattern at the beginning of the string
print((matches.group()))

pattern = re.compile("a*")
matches = pattern.findall(text) 
print(matches)

pattern = re.compile("a+")
matches = pattern.findall(text)
print(len(matches))

pattern = re.compile("a?")
matches = pattern.search(text)
print((matches))

pattern = re.compile("[CP]h")
matches = pattern.match(text)
print(matches.group())

pattern = re.compile("[^CP]a")
matches = pattern.findall(text)
print(matches)
print(len(matches))

pattern = re.compile("(and)")
matches = pattern.findall(text)
print(matches)

pattern = re.compile("C|P")
matches = pattern.search(text) #search method looks for the pattern throughout the string, and stops at the first match.
print(matches) #C

pattern = re.compile("\$")
matches = pattern.findall(text)
print(matches)

pattern = re.compile("C{1}") #exactly 1 occurrence
matches = pattern.findall(text)
print(matches)

pattern = re.compile("(ra)")
matches = pattern.finditer(text)

for i in matches:
    # print(i) #prints match (2)objects
    # print(i.group(0))
    print(i.groups(1))
    print(i.groupdict()) #return dictionary/key-value pair of named groups()

pattern =re.compile("(ra){1,}") 
matches = pattern.findall(text)
print(matches)

pattern = re.compile("(ra){1,3}") #atleast 1 and atmost 3
matches = pattern.search(text)
print(matches.span())
print(matches.group())

pattern = re.compile("\d")
matches = pattern.findall(text)
print(bool(matches))

pattern = re.compile("\D")
matches = pattern.findall(text)
print(bool(matches))

pattern = re.compile("\w")
matches = pattern.findall(text)
print(bool(matches))
print((matches))


pattern = re.compile("\W") #matches non-alphnumeric characters - a-z,A-Z,0-9,_
matches = pattern.findall(text)
print(bool(matches)) #True, but
print((matches)) #['','']

pattern = re.compile("\s") #matchews for newline, sdpace, tab

matches = pattern.search(text) #at index 7
print(matches)

pattern = re.compile("\S")
matches = pattern.findall(text)
print(bool(matches))
print((matches))

pattern = re.compile("\\bChandra\\b")
matches = pattern.findall(text)
print(bool(matches))
print(matches)

# Flags in regex: optional parameteres that modify the behavior of regex

pattern = re.compile("chandra", re.IGNORECASE) #ignores case
matches = pattern.findall(text)
print(bool(matches))
print(matches)

text = "Chandra\nPrakash\nTekwani"
pattern = re.compile("Chandra",re.MULTILINE) #match start/end of each line within a multiline string, rather than just the entire string.
matches = pattern.findall(text)
print(bool(matches))
print(matches)


pattern = re.compile("(ra)",re.S) #DOTALL flag, makes . match any character, including newline
matches = pattern.findall(text)
print(bool(matches))
print(matches)

pattern = re.compile("Chandra #myFirstRegex",re.X) #VERBOSE flag, allows you to write regex in a more readable format. It ignores whitespace and comments within the pattern.
matches = pattern.findall(text)
print(bool(matches))
print(matches)

# strings are Unicode and not ASCII
# ASCII is limited to 128 characters and neigther include dagger nor ligatures , while Unicode has 1,114,112 characters.and includes dagger and ligatures and default to Python 3 re module
# ASCII is a subset of Unicode
# ASCII = American Standard Code for Information Interchange = \W = [^a-zA-Z0-9_], \w = [a-zA-Z0-9_], \d = [0-9], \D = [^0-9], \s = [ \t\n\r\f\v], \S = [^ \t\n\r\f\v]. it represents text using set of 128 unique 7-bit binary codes (0-127) in Decimal.
# Unicode = \w = [a-zA-Z0-9_], \W = [^a-zA-Z0-9_], \d = [0-9], \D = [^0-9], \s = [ \t\n\r\f\v], \S = [^ \t\n\r\f\v]
text = "Chandra\nP†œrakash\nTekwani" #†(Dagger) and œ(fi) are not a word character in eithet ASCII or Unicode
pattern = re.compile("\w+",re.ASCII) #ASCII flag, makes \w, \W, \b, \B, \d, \D, \s and \S dependent on the ASCII character set.
matches = pattern.findall(text)
print(bool(matches))
print(matches)


# import locale

# locale.setlocale(locale.LC_ALL, "")  # set the locale for the user's environment
# text = "Chandra\nP†œrakash\nTekwani"

# pattern = re.compile(
#     r"\w+", re.LOCALE
# )  # LOCALE flag, makes \w, \W, \b, \B, \d, \D, \s and \S dependent on the current locale.locale is a set of parameters that defines the user's language, region and any special variant preferences that the user wants to see in their user interface.
# matches = pattern.findall(text)
# print(bool(matches))
# print(matches)

pattern = re.compile(r"\w+", re.UNICODE)  # UNICODE flag, makes \w, \W, \b, \B, \d, \D, \s and \S dependent on the Unicode character properties database.
matches = pattern.findall(text)
print(matches)

pattern = re.compile(r"\w+", re.DEBUG) #DEBUG flag, displays debugging information about the pattern compilation.
matches = pattern.findall(text) 
print(matches)

#Combinining flags
pattern = re.compile(r"\w+", re.ASCII | re.IGNORECASE) #combining flags
matches = pattern.findall(text)
# print(bool(matches))
print(matches)

print()
print()
print()
#Inline flags
pattern = re.compile(r"(?i)chandra") #inline flags
matches = pattern.findall(text)
print(bool(matches))
print(matches)

pattern = re.compile(r"(?m)chandra") #inline flags
matches = pattern.findall(text)
print(bool(matches))
print(matches)

pattern = re.compile(r"(?s)chandra") #inline flags
matches = pattern.findall(text)
print(bool(matches))
print(matches)

pattern = re.compile(f"(?x){text}") #inline flags
matches = pattern.findall(text)
print(bool(matches))
print(matches)

pattern = re.compile(r"(?a)chandra") #inline flags
matches = pattern.findall(text)
print(bool(matches))
print(matches)