def perfect_num(num):
    if num <= 1:
        return False
    
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if(divisors_sum == num):
        return "Yes"
    else:
        return "No"


n = int(input("Enter a number: "))
print(perfect_num(n))

