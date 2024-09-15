def make_stone_piles(n):
    piles = []
    
    if n % 2 == 0:
        start = 2
    else:
        start = 1
    
    while start <= n:
        piles.append(start)
        start += 2
    
    return piles

n = int(input("Enter the number of stones in the first pile: "))
print(f"Stones in a single pile = ", make_stone_piles(n))
