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

    # Prompt user to input hotel ID for booking and create a SpaHotel instance inherited from Hotel class
    hotel_id = prompt.input_hotel_id()
    hotel = SpaHotel(hotel_id=hotel_id)

    # Check availability of the hotel
    check_hotel, message = hotel.available()

    # If hotel is available, proceed with booking
    if check_hotel:
        # Prompt user to enter their name for reservation
        name = prompt.input_full_name()
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
                # Create a ticket object
                hotel_ticket = HotelReservationTicket(
                    customer_name=name, hotel_object=hotel)
                # Generate hotel reservation ticket content and display it
                print("\n\n", hotel_ticket.generate(), "\n")

                # Prompt the user to input yes or no for spa booking package
                booking_spa_package = prompt.input_spa_booking()
                # If answer is yes (returned True) Proceed with the transaction of booking spa package
                if booking_spa_package:
                    hotel.book_spa_package()
                    # Create a spa reservation ticket object and Generate its content and display it
                    spa_ticket = SpaReservationTicket(
                        customer_name=name, hotel_object=hotel)
                    print("\n\n", spa_ticket.generate(), "\n")
                else:
                    # If no spa booking enter breaklines to display the last message better
                    print("\n\n")

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

    # Display a thank you and goodbye message
    print("--- Thank you for using our service. Have a great day! ---\n\n")


if __name__ == '__main__':
    app()
