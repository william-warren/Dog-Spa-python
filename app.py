from json import load
from datetime import datetime

# Import modules here!

SERVICES_FILENAME = "services.json"
TRANSACTIONS_FILENAME = "transactions.txt"


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
        service_list = services["services"]
    for service in service_list:
        name = service_list[f"{service}"]["name"]
        price = service_list[f"{service}"]["price"]
        option = {f"{service}": {"name": f"{name}", "price": f"{price}"}}
        print(f"{name} ~ ${price}")


def select_service():
    while True:
        selection = input("Which service would you like to purchase?")
        with open(SERVICES_FILENAME) as reference:
            services = load(reference)
            service_list = services["services"]
        for service in service_list:
            if selection.strip().lower() == service_list[f"{service}"]["name"]:
                name = service_list[f"{service}"]["name"]
                price = service_list[f"{service}"]["price"]
                message = f">>>{name.capitalize()}\nWhat a great choice!\nYou're total will be ${price}"
                print(message)
                result = selection.lower().strip()
                return result
        print("Please choose a valid option.")


def get_log(choice):
    with open(SERVICES_FILENAME) as reference:
        services = load(reference)
    service_list = services["services"]
    now = datetime.now()
    for service in service_list:
        if choice == service_list[f"{service}"]["name"]:
            name = service_list[f"{service}"]["name"]
            price = service_list[f"{service}"]["price"]
            return f"\n{now}, {name}, {price}"


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
