# https://www.codewars.com/kata/new-cashier-does-not-know-about-space-or-shift/train/python
menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich",
        "Onionrings", "Milkshake", "Coke"]

def get_order(order):
    order += "1"
    order0, item = {}, ""
    for i in order:
        if item == "":
            item = i.upper()
        elif item not in menu:
            item += i
        elif item in order0:
            order0[item] += 1
            item = i.upper()
        else:
            order0[item] = 1
            item = i.upper()
    answer = ""
    for i in menu:
        if i in order0:
            for _ in range(order0[i]):
                answer += " " + i
    return answer[1:]


print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))
