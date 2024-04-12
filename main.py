import pandas as pd
from app_utils import *
from constants import *


def app():
    """
    Main function to handle hotel booking application.
    """
    # Display the hotel data
    print("\n", df, "\n")

    # Prompt user to input hotel ID for booking and create a hotel instance
    hotel_id = input("\n- Enter the hotel ID for booking: ")
    hotel = Hotel(hotel_id)

    # Check availability of the hotel
    check_hotel, message = hotel.available()

    if check_hotel:
        # If hotel is available, proceed with booking
        hotel.book()
        # Prompt user to enter their name for reservation and create a ticket instance
        name = input("\n- Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        # Generate reservation ticket content
        ticket = reservation_ticket.generate()
        print("\n\n", ticket, "\n")
    else:
        # If hotel is not available, display appropriate message
        if message:
            print(f"\n{message}\n")
        else:
            print("\n-- Hotel with provided ID is not available.\n")


if __name__ == '__main__':
    app()
