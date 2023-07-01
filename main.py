def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

input_string = input("Enter a string: ")
output_string = remove_vowels(input_string)
print("String without vowels:", output_string)
