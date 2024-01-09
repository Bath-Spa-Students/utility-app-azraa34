from prettytable import PrettyTable
import pyfiglet
import colorama
from colorama import Style, init

# Initialize colorama
init(autoreset=True)
colorama.init()

class VendingMachine:
    def __init__(self):
        # Initialize the vending machine with initial state
        self.money_inserted = 0.0
        self.purchased_drink = False

        # Define items for drinks and snacks separately
        self.drink_items = {
            "A. Latte": {"price": 3.50, "code": "A", "count": 5},
            "B. Americano": {"price": 2.50, "code": "B", "count": 4},
            "C. Cappuccino": {"price": 3.25, "code": "C", "count": 6},
            "D. Matcha": {"price": 4.00, "code": "D", "count": 3},
            "E. Espresso": {"price": 2.00, "code": "E", "count": 7},
            "F. Frappuccino": {"price": 3.00, "code": "F", "count": 4},
            "G. Mocha": {"price": 3.50, "code": "G", "count": 5},
            "H. Hot Chocolate": {"price": 3.00, "code": "H", "count": 4},
            "I. Macchiato": {"price": 3.25, "code": "I", "count": 7},
            "J. Iced Coffee": {"price": 2.50, "code": "J", "count": 5},
        }

        self.snack_items = {
            "K. Croissants": {"price": 1.50, "code": "K", "count": 8},
            "L. Eclairs": {"price": 3.00, "code": "L", "count": 4},
            "M. Crepes": {"price": 3.50, "code": "M", "count": 6},
            "N. Macarons": {"price": 2.00, "code": "N", "count": 5},
            "O. Cheesecake": {"price": 3.50, "code": "O", "count": 4},
            "P. Fruit Tarts": {"price": 2.25, "code": "P", "count": 7},
            "Q. Chocolate Cake": {"price": 2.50, "code": "Q", "count": 5},
            "R. Donuts": {"price": 2.80, "code": "R", "count": 5},
            "S. Honeycake": {"price": 2.20, "code": "S", "count": 7},
            "T. Pretzels": {"price": 2.75, "code": "T", "count": 6},
        }

    def cute_welcome_message(self):
        # Display a cute welcome message using pyfiglet in dark brown
        welcome_ascii = pyfiglet.figlet_format("Welcome to the\nCoffee Vending Machine", font="script")
        print("\033[38;2;139;69;19m" + welcome_ascii + Style.RESET_ALL)

    def validate_code(self, user_code):
        # Validate the user-entered code against the available items (drinks and snacks)
        for code, item in {**self.drink_items, **self.snack_items}.items():
            if code.split(".")[0].upper() == user_code.upper():
                return item
        return None

    def display_menu(self, items, title_color, title):
        # Display the menu with custom formatting for the borders and specified title color
        print("\033[38;2;" + title_color + "m" + title + Style.RESET_ALL)  # Set the title color
        table = PrettyTable()
        table.field_names = ["Code", "Item", "Price ($)", "Stock"]
        for code, item in items.items():
            table.add_row([code.split(".")[0], code.split(".")[1], f"{item['price']:.2f}", item['count']])
        table.border = True
        table.header = True
        print(table)

    def display_insert_money_option(self):
        # Prompt the user to insert money
        print("\nPlease insert money:")
        self.money_inserted = float(input("Amount: $"))
        print("\033[38;2;139;0;139m" + f"Money inserted: ${self.money_inserted:.2f}" + "\033[0m")  # Dark Purple

    def ask_for_another_purchase(self):
        # Ask the user if they want to make another purchase
        response = input("\nWould you like to make another purchase? (yes/no): ").lower()
        return response == 'yes'

    def process_transaction(self, user_selection):
        if user_selection:
            if user_selection['count'] > 0:
                if self.money_inserted >= user_selection['price']:
                    # Process the transaction and provide the item to the user
                    change = self.money_inserted - user_selection['price']
                    print("\033[38;2;0;128;0m" + f"\nDispensing {user_selection['code']}. Please collect your item." + Style.RESET_ALL)  # Set the success message color
                    print("\033[38;2;139;69;19m" + f"Change: ${change:.2f}" + Style.RESET_ALL)  # Set the text color
                    self.money_inserted = 0.0  # Reset money_inserted to 0 for a successful transaction
                    user_selection['count'] -= 1  # Decrease the count of the item
                    self.purchased_drink = user_selection['code'] in self.drink_items.keys()
                    return True
                else:
                    print("\033[38;2;139;0;0m" + "\nInsufficient money inserted. Please try again.\n" + Style.RESET_ALL)  # Set the error message color
            else:
                print("\033[38;2;139;0;0m" + "\nItem out of stock. Please try another item.\n" + Style.RESET_ALL)  # Set the error message color
        else:
            print("\033[38;2;139;0;0m" + "\nInvalid code entered. Please try again.\n" + Style.RESET_ALL)  # Set the error message color

        return False

    def run(self):
        # Main execution of the vending machine
        self.cute_welcome_message()

        while True:
            # Display the drink and snack tables side by side
            self.display_menu(self.drink_items, "184;134;11", "Drink Menu")  # Set light brown color for the title
            self.display_menu(self.snack_items, "184;134;11", "Snack Menu")  # Set light brown color for the title
            self.display_insert_money_option()

            user_code = input("\nPlease enter the item code (or 'Finish' to complete the purchase):").upper()

            if user_code == 'FINISH':
                break

            user_selection = self.validate_code(user_code)
            if self.process_transaction(user_selection):
                if not self.ask_for_another_purchase():
                    break  # Break if the user doesn't want to make another purchase

        self.cute_thank_you_message()

    def cute_thank_you_message(self):
        # Display a thank you message in magenta and cyan
        print("\033[38;2;138;43;226m" + "\nThank you for visiting the Coffee Shop! ✨" + Style.RESET_ALL)  # Set dark brown color for thank you message
        print("\033[38;2;0;139;139m" + "Hope you enjoyed your drink and snacks. Have a lovely day! 🌸" + Style.RESET_ALL)  # Set dark cyan color for message


if __name__ == "__main__":
    # Create an instance of the VendingMachine class and run the program
    vending_machine = VendingMachine()
    vending_machine.run()
