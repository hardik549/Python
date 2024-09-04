def count_frequency(input_list):
    freq = {}
    
    for item in input_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    return freq

input_list=list(map(int,input().split()))
print("Frequency count:", count_frequency(input_list))
