import pandas as pd
from app_utils import *
from constants import *


def app():
    """
    Main function to handle hotel booking application.
    """
    # Create a UserInput object to prompt user for all inputs
    prompt = UserInput()
    # Display the hotel data
    print("\n", df_hotels, "\n")

    # Prompt user to input hotel ID for booking and create a hotel instance
    hotel_id = prompt.input_hotel_id()
    hotel = Hotel(hotel_id)

    # Check availability of the hotel
    check_hotel, message = hotel.available()

    # If hotel is available, proceed with booking
    if check_hotel:
        # Prompt the user to input credit card information
        card_info = prompt.input_credit_card_info()
        # Unpack the card_info dictionary into individual variables
        card_number, expiration, cvc, holder = card_info.values()
        # Create a SecureCreditCard object that already inherits everything from CreditCard (attributes + methods)
        credit_card = SecureCreditCard(card_number=card_number)

        # If Credit card is valid Proceed with the transaction
        if credit_card.validate(expiry_date=expiration, holder=holder, cvc_number=cvc):
            # Prompt the user to input card authentication password
            password = prompt.input_password()
            # If Credit card is authenticated Proceed with the transaction
            if credit_card.authenticate(password_input=password):
                hotel.book()
                # Prompt user to enter their name for reservation and create a ticket instance
                name = prompt.input_full_name()
                reservation_ticket = ReservationTicket(name, hotel)
                # Generate reservation ticket content
                ticket = reservation_ticket.generate()
                print("\n\n", ticket, "\n")
            else:
                # If Credit card is not authenticated Display an error message
                print("\n-- Credit card authentication failed. --\n")

        else:
            # If Credit card is not valid Display an error message
            print("\n-- Payment processing issue. --\n")

    else:
        # If hotel is not available, display appropriate message
        if message:
            print(f"\n{message}\n")
        else:
            print("\n-- Hotel with provided ID is not available. --\n")


if __name__ == '__main__':
    app()
