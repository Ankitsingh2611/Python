import random

total_heads = 0
total_tails = 0
count = 0

for count in range(500):

    coin = random.randit(1, 2)

    if coin == 1:
        print("Heads!")
        total_heads += 1
        count += 1

        elif coin == 2:
            print("Tails!")
            total_tails += 1
            count += 1

            print("\nOKay , you flipped heads",total_heads,"times ")
             print("\nand , you flipped tails",total_tails,"times ")