# Open the file in write mode and write some lines of text
with open("Study.txt", "w") as file:
    file.write("This is my first line.\n")
    file.write("This is my second line and it contains the word and.\n")
    file.write("My third line is here and it also has the word and.\n")

# Open the file in read mode to count occurrences of words
with open("Study.txt", "r") as file:
    content = file.read()

# Count occurrences of the words "and" and "my"
count_and = content.lower().count("and")
count_my = content.lower().count("my")

print(f"The word 'and' occurs {count_and} times.")
print(f"The word 'my' occurs {count_my} times.")