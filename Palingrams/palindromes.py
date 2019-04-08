import load_dictionary

dict_path = 'dictionary.txt'
word_list = load_dictionary.load(dict_path)
pali_list = []

for word in word_list:
    if word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
