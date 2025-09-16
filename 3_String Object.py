import re

string = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# Step 1: Normalize the text to lowercase and remove extra spaces
string1 = string.lower().replace("  ", "")  # Convert the entire string to lowercase and remove extra spaces
#print(string1)



# Step 2: Add a new sentence with the last words of each existing sentence
string1 += "\n"  # Add a newline character to ensure proper processing of the last sentence
for line in string1.splitlines():  # Split the text into lines and iterate through each line
    #print(len(line))
    if len(line) > 1:  # Process only non-empty lines
        # Extract the last word of the line, removing punctuation like `.` or `:`
        lastWord = re.sub("\\.||\\:", "", line.strip().split()[-1])
        #print(lastWord)
        string1.join(lastWord)  # Join the last word to the string (this line has no effect and can be removed)
        string1 += lastWord + " "  # Append the last word to the string, followed by a space
    string2 = re.sub("( )$", ".", string1)  # Replace the trailing space at the end of the string with a period
#print(string2)



# Step 3: Fix the misspelling of "iz" to "is" (only when it is a mistake)
string3 = string2.replace(" iz ", " is ")  # Replace occurrences of " iz " with " is "
#print(string3)



# Step 4: Count the number of whitespace characters (excluding newlines)
counter = 0  # Initialize a counter for whitespace characters
for char in string:  # Iterate through each character in the original string
    # Check if the character is a whitespace character (using `\s`) and ensure it is not a newline (`\n`)
    if re.search(r"\s", char) and not re.search(r"\n", char):
        counter += 1  # Increment the counter for each valid whitespace character
#print(counter)
