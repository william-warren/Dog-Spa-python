from json import load
from datetime import datetime

# Import modules here!

SERVICES_FILENAME = "./dog_spa/services.json"
TRANSACTIONS_FILENAME = "./dog_spa/transactions.txt"


def print_welcome_message():
    print(
        """
                         .--~~,__
            :-....,-------`~~'._.'
            `-,,,  ,_      ;'~U'
            _,-' ,'`-__; '--.
            (_/'~~      ''''(;
 WELCOME TO LUXURY DOG SERVICES!
    """
    )


def load_services():
    with open(SERVICES_FILENAME) as reference:
        services = load(reference)
    bath_name = services["services"]["bath"]["name"]
    bath_price = services["services"]["bath"]["price"]
    massage_name = services["services"]["massage"]["name"]
    massage_price = services["services"]["massage"]["price"]
    walk_name = services["services"]["walk"]["name"]
    walk_price = services["services"]["walk"]["price"]
    play_name = services["services"]["play"]["name"]
    play_price = services["services"]["play"]["price"]

    bath = f"Service: {bath_name}, Price: {bath_price}"
    massage = f"Service: {massage_name}, Price: {massage_price}"
    walk = f"Service: {walk_name}, Price: {walk_price}"
    play = f"Service: {play_name}, Price: {play_price}"
    print(bath, "\n", massage, "\n", walk, "\n", play)


def select_service():
    while True:
        selection = input(
            "Which service would you like to purchase? [bath, massage, walk, or play] "
        )
        if selection == "bath":
            print(">>>Bath")
            print("Thats a great choice, your total is $25")
            print("Thank you for your service!")
            return "bath"
        elif selection == "massage":
            print(">>>Massage")
            print("Thats a great choice, your total is $15")
            print("Thank you for your service!")
            return "massage"
        elif selection == "walk":
            print(">>>Walk")
            print("Thats a great choice, your total is $10")
            print("Thank you for your service!")
            return "walk"
        elif selection == "play":
            print(">>>Play")
            print("Thats a great choice, your total is $20")
            print("Thank you for your service!")
            return "play"
        else:
            print("Please enter a valid option")


def get_log(choice):
    with open(SERVICES_FILENAME) as reference:
        services = load(reference)
    now = datetime.now()
    if choice == "bath":
        bath_name = services["services"]["bath"]["name"]
        bath_price = services["services"]["bath"]["price"]
        return f"\n{now}, {bath_name}, {bath_price}"
    elif choice == "massage":
        massage_name = services["services"]["massage"]["name"]
        massage_price = services["services"]["massage"]["price"]
        return f"\n{now}, {massage_name}, {massage_price}"
    elif choice == "walk":
        walk_name = services["services"]["walk"]["name"]
        walk_price = services["services"]["walk"]["price"]
        return f"\n{now}, {walk_name}, {walk_price}"
    elif choice == "play":
        play_name = services["services"]["play"]["name"]
        play_price = services["services"]["play"]["price"]
        return f"\n{now}, {play_name}, {play_price}"

def log_data(log):
    with open(TRANSACTIONS_FILENAME, "a") as log_file:
        log_file.write(log)


def dog_spa():
    print_welcome_message()
    load_services()
    choice = select_service()
    log = get_log(choice)
    log_data(log)


if __name__ == "__main__":
    dog_spa()
