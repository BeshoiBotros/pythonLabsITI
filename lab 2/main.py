import random

def check_number_safely(prompt: str = 'Enter number: '):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                print("Error: please enter a valid number.")


#     1 - Ask the user to enter 5 numbers.
#         Store them, then display them in ascending order and descending order.
def task1():
    list_of_nums = []
    
    for i in range(5):
        num = check_number_safely()
        list_of_nums.append(num)
    
    print(f'Ascending order: {sorted(list_of_nums)}')
    print(f'Descending order: {sorted(list_of_nums, reverse=True)}')


# 2 - Write a function that takes two numbers: (length, start).
#       Generate a sequence of numbers with the given length,
#       starting from the given start number and increasing by one each time.
#       Print the result.

def task2():
    length = check_number_safely("Enter sequence length: ")
    start = check_number_safely("Enter start number: ")

    sequence = [start + i for i in range(length)]
    print("Generated sequence:", sequence)


# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.

def task3():
    numbers = []
    print('Enter numbers one by one. Type "done" to finish.')
    while True:
        value = input("Enter number (or 'done'): ").strip().lower()
        if value == "done":
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if numbers:
        total = sum(numbers)
        count = len(numbers)
        avg = total / count
        print(f"Total = {total}, Count = {count}, Average = {avg:.2f}")
    else:
        print("No valid numbers were entered.")


# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.
    
def task4():
    values = input("Enter numbers separated by spaces: ")
    try:
        nums = [int(x) for x in values.split()]
    except ValueError:
        print("Invalid input. Only numbers separated by spaces are allowed.")
        return

    sorted_nums = sorted(set(nums))
    print("Unique sorted list:", sorted_nums)


# 6 - Ask the user to enter a sentence.
#     Count how many times each word appears in the sentence
#     and display the result.

def task6():
    sentence = input("Enter a sentence: ")
    words = sentence.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print("Word frequencies:")
    for word, count in counts.items():
        print(f"{word}: {count}")


# 7 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.

def task7():
    students = {}
    for i in range(5):
        name = input(f"Enter student {i+1} name: ").strip()
        score = check_number_safely(f"Enter {name}'s score: ")
        students[name] = score

    scores = list(students.values())
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)

    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Average score:", round(average, 2))


# 8 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.

class CartItem:
    def __init__(self, name: str = '', price: (float|int) = 0, quantity: int = 0):
        self.name, self.price, self.quantity = name, price, quantity
    
    def __str__(self):
        return f'Item name: {self.name} \nItem price: {self.price} \nItem quantity: {self.quantity}'
    
    def __eq__(self, other):
        if isinstance(other, CartItem):
            return self.name.lower() == other.name.lower()
        return False

    def __hash__(self):
        return hash(self.name.lower())
    
class ShoppingCart:

    def __init__(self, username):
        self.username = username
        self.shopping_cart: set[CartItem] = set()
    
    def get_all_items_name(self):
        return [i.name for i in self.shopping_cart]

    def add_item(self, item: CartItem):
        if item.name in self.get_all_items_name():
            print('This item already exists in your cart')
            return
        self.shopping_cart.add(item)
        print("Item added into your cart successfully!")
    
    def delete_item(self, name: str):
        for item in list(self.shopping_cart):
            if item.name.lower() == name.lower():
                self.shopping_cart.remove(item)
                return f"{name} removed from your cart"
        print("Item not found in cart.")

    def list_items(self):
        if not self.shopping_cart:
            print('Your shopping cart is empty for now')
            return
        for i in self.shopping_cart:
            print(i.__str__())
    
    def total_cost(self):
        if not self.shopping_cart:
            print('Your shopping cart is empty for now')
            return
        return sum(item.price * item.quantity for item in self.shopping_cart)
    
    def set_quantity_by_name(self, name: str, quantity: int):
        for item in self.shopping_cart:
            if item.name.lower() == name.lower():
                item.quantity = quantity
                return f"Quantity of {name} updated to {quantity}"
        return "Item not found in cart."

def task8():
    username = input('Enter your Username: ')
    user_cart = ShoppingCart(username)

    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. Add Item to cart")
        print("2. Delete item from cart")
        print("3. List all items")
        print("4. View total cost")
        print("5. Change item quantity by name")
        print("0. Exit")

        choice = input("Choose -> ").strip()

        if choice == "1":
            item_name     = input('Enter Item name: ')
            item_price    = check_number_safely('Enter Item price: ')
            item_quantity = int(check_number_safely('Enter Item quantity: '))
            user_cart.add_item(CartItem(name=item_name, price=item_price, quantity=item_quantity))

        elif choice == "2":
            item_name = input('Enter item name to delete: ')
            print(user_cart.delete_item(item_name))

        elif choice == "3":
            user_cart.list_items()

        elif choice == "4":
            print("Total cost =", user_cart.total_cost())

        elif choice == "5":
            item_name = input('Enter item name to update quantity: ')
            new_quantity = int(check_number_safely("Enter new quantity: "))
            print(user_cart.set_quantity_by_name(item_name, new_quantity))

        elif choice == "0":
            print("Exiting Shopping Cart. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from the menu.")


# 9 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts.

def task9():
    number = random.randint(1, 20)
    attempts = 0
    print("Guess the number (between 1 and 20):")

    while True:
        guess = check_number_safely("Your guess: ")
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! The number was {number}. Attempts: {attempts}")
            break
        
        
if __name__ == '__main__':
    tasks = {
        "1": task1,
        "2": task2,
        "3": task3,
        "4": task4,
        "6": task6,
        "7": task7,
        "8": task8,
        "9": task9,
    }

    while True:
        print("\n=== Python Practice Menu ===")
        print("1: task 1")
        print("2: task 2")
        print("3: task 3")
        print("4: task 4")
        print("6: task 6")
        print("7: task 7")
        print("8: task 8")
        print("9: task 9")
        print("0: Exit")

        choice = input("Choose a task -> ")

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("Invalid choice. Please enter a valid number from the menu.")