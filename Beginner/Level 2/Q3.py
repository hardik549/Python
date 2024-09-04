def find_pairs(arr, k):
    pair = 0
    visited = set()
    
    for num in arr:
        complement = k - num 
        if complement in visited:
            pair += 1
        visited.add(num)
    
    return pair


list1=list(map(int,input("Enter the elements : ").split()))
k = int(input())
print(f"Pair count : ",find_pairs(list1, k))
