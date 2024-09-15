def split_strings(string_list):
    result = list(map(list, string_list))
    return result

string_list = input("Enter a list of strings: ").split()
print(split_strings(string_list))
