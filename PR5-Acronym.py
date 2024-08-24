str_val = input("Enter a phrase:")

splitted_words = str_val.split()
print(splitted_words)
acronym = "" # empty string


for i in splitted_words:
    letter = i[0] # first letter
    letter = letter.upper()
    acronym += letter # concatenation

print('The acronym is:',acronym)
