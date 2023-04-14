import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     #Access index and row
#     #Access row.student or row.score
#     # print(index, row)
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter:row.code for (index, row) in df.iterrows() }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = list(input("Enter a word to create a list with Nato words: ").upper())

nato_list = [nato_dictionary[letter] for letter in input_word]
print(nato_list)
