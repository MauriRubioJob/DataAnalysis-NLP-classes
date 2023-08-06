
stock = {
    "apple": 15,
    "banana": 0,
    "orange": 8,
    "pear": 60
}

prices = {
    "apple": 1.5,
    "banana": 2.5,
    "orange": 0.8,
    "pear": 0.5
}

# [apple, apple, apple, banana, orange...., orange, pear]
def compute_bill(shopping_list):
    total = 0
    for item in shopping_list:
        # Check if the item is in stock
        if stock[item] > 0:
            # Increase the total by the price of the item
            # And remove one from the stock
            total = total + prices[item]
            stock[item] = stock[item] - 1
        else:
            print("Sorry, " + item + " is out of stock.")
    return total


my_shopping_list = []

for item in stock:
    print("How many " + item + "s would like?")
    amount = int(input())
    my_shopping_list.extend([item] * amount)


my_shopping_list = ["apple"] * 4 + ["banana"] * 10

total = compute_bill(my_shopping_list)
print("Total price is " + str(total) + "€")
    


