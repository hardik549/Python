def rev(input_sentence):
    if input_sentence.startswith('“') and input_sentence.endswith('”'):
        input_sentence = input_sentence[1:-1]

    words = input_sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

input_sentence  = input("Enter any sentence : ")
print("Output after reverse:", f'“{rev(input_sentence)}”')
