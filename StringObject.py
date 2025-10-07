import re

string = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# Step 1: Normalize the text to lowercase and remove extra spaces
normalize = lambda string: string.capitalize().replace("  ", "")  # Convert the entire string to lowercase and remove extra spaces
string1 = normalize(string)
#print(string1)



# Step 2: Add a new sentence with the last words of each existing sentence
def get_last_word(line):
    # Extract the last word of the line, removing punctuation like `.` or `:`
    return re.sub("\\.||\\:", "", line.strip().split()[-1])


string1 += "\n"  # Add a newline character to ensure proper processing of the last sentence
for line in string1.splitlines():  # Split the text into lines and iterate through each line
    if len(line) > 1:  # Process only non-empty lines
        string1 += get_last_word(line) + " "  # Append the last word to the string, followed by a space
string2 = re.sub("( )$", ".", string1)  # Replace the trailing space at the end of the string with a period
#print(string2)



# Step 3: Fix the misspelling of "iz" to "is" (only when it is a mistake)
replace_iz = lambda string : string.replace(" iz ", " is ")  # Replace occurrences of " iz " with " is "
string3 = replace_iz(string2)  # Replace occurrences of " iz " with " is "
#print(string3)



# Step 4: Count the number of whitespace characters (excluding newlines)
string_list = [ch for ch in string]
def count(*args):
    counter = 0  # Initialize a counter for whitespace characters
    for char in args:  # Iterate through each character in the original string
        # Check if the character is a whitespace character (using `\s`) and ensure it is not a newline (`\n`)
        if re.search(r"\s", char) and not re.search(r"\n", char):
            counter += 1  # Increment the counter for each valid whitespace character
    return counter
#print(count(*string_list))
