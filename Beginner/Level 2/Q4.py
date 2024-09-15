def rotate_right(arr, D):
    D = D % len(arr)
    rotated_arr = arr[-D:] + arr[:-D]
    return rotated_arr

arr=list(map(int,input("Enter the elements : ").split()))
D = int(input("Enter the element D: "))
print("arr after rotation", rotate_right(arr, D))
