movie_name = input("Enter movie name: ")
price = int(input("Enter ticket price: "))
tickets = int(input("Enter number of tickets: "))


def calculate_ticket_cost(price, tickets):
    total = price * tickets
    return total


def calculate_discount(total):
    if total >= 1000:
        discount = total * 10 / 100
    else:
        discount = 0

    return discount


total = calculate_ticket_cost(price=price, tickets=tickets)
discount = calculate_discount(total)

final_amount = total - discount

print("\n===== MOVIE BOOKING =====")
print(f"Movie: {movie_name}")
print(f"Ticket Price: ₹{price}")
print(f"Tickets: {tickets}")
print(f"Total: ₹{total}")
print(f"Discount: ₹{discount}")
print(f"Final Amount: ₹{final_amount}")
