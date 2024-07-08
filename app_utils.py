import pandas as pd
import re
from fpdf import FPDF
from datetime import datetime
from constants import *


# Read the hotel data from a CSV file, ensuring the 'id' column is treated as string
df_hotels = pd.read_csv(HOTELS_DATA, dtype={'id': 'str'})
# Read the cards data from a CSV file into a pandas DataFrame, treating all columns as strings
# Convert the DataFrame into a list of dictionaries, The `orient='records'` argument specifies that each row of the DataFrame will be converted into a dictionary with column names as keys and corresponding values as values
df_cards = pd.read_csv(CARDS_DATA, dtype=str).to_dict(orient='records')
# Read the cards_security data from a CSV file into a pandas DataFrame, treating all columns as strings
df_cards_security = pd.read_csv(CARDS_SECURITY_DATA, dtype=str)


class UserInput:
    def input_hotel_id(self):
        """
        Prompts the user to input the hotel ID.

        Returns:
        - str: The hotel ID entered by the user.
        """
        while True:
            hotel_id = input(
                "\n\n- Enter the hotel ID for booking (3 digits): ")
            # Validation check using regex to return the hotel id
            if re.match(HOTEL_ID_PATTERN, hotel_id):
                return hotel_id
            else:
                print("\n-- Error: Please enter a 3-digit hotel ID. --\n")

    def input_full_name(self):
        """
        Prompts the user to input their full name.

        Returns:
        - str: The full name entered by the user.
        """
        while True:
            name = input(
                "\n\n- Enter your full name (first_name last_name): ")
            # Validation check using regex to return the name
            if re.match(NAME_PATTERN, name):
                return name
            else:
                print(
                    "\n-- Error: Please enter your full name in the format 'first_name last_name'. --\n")

    def input_credit_card_info(self):
        """
        Prompts the user to input credit card information.

        Returns:
        - dict: A dictionary containing the credit card information entered by the user.
        """
        print("\n\n- Enter information for your Card:")

        # Validation checks using regex
        while True:
            number = input("\n--> Card Number: ")
            if re.match(CARD_NUMBER_PATTERN, number):
                break
            else:
                print(
                    "\n-- Error: Invalid card number. Please enter a 16-digit number. --\n")

        while True:
            expiration = input("\n--> Expiration Date (MM/YY): ")
            if re.match(EXPIRATION_PATTERN, expiration):
                break
            else:
                print(
                    "\n-- Error: Invalid expiration date. Please enter in format MM/YY. --\n")

        while True:
            cvc = input("\n--> CVC: ")
            if re.match(CVC_PATTERN, cvc):
                break
            else:
                print("\n-- Error: Invalid CVC. Please enter a 3-digit number. --\n")

        while True:
            holder = input("\n--> Cardholder Name: ")
            if re.match(NAME_PATTERN, holder):
                break
            else:
                print(
                    "\n-- Error: Cardholder name must be in the format 'first_name last_name' and cannot be empty. --\n")

        # If all inputs are valid, return card information
        card_info = {
            "number": number,
            "expiration": expiration,
            "cvc": cvc,
            "holder": holder
        }
        return card_info

    def input_password(self):
        """
        Prompts the user to input their card authentication password.

        Returns:
        - str: The password entered by the user.
        """
        while True:
            password = input(
                "\n\n- Enter your card authentication password (minimum 6 characters long): ")
            # Validation check using regex to return the password
            if re.match(CARD_AUTH_PATTERN, password):
                return password
            else:
                print(
                    "\n-- Error: Card authentication password must be 6 characters or longer and cannot be empty. --\n")

    def input_spa_booking(self):
        """
        Prompt the user to book a Spa package.

        Returns:
        - str: 'yes' if the user wants to book a Spa package, 'no' otherwise.
        """
        while True:
            answer = input(
                "- Would you like to book a SPA package? (yes/no) ").lower()
            # Validation check to ensure the input is either 'yes', 'no', 'y', or 'n'
            if answer in ['y', 'yes']:
                return True
            elif answer in ['n', 'no']:
                return False
            else:
                print("\n-- Error: Please enter 'yes'/'y' or 'no'/'n'. --\n")


class Hotel:
    def __init__(self, hotel_id):
        """
        Initializes a Hotel object with the provided ID and retrieves its name from the DataFrame.

        Parameters:
        - hotel_id (str): The ID of the hotel.

        """
        self.id = hotel_id

        if hotel_id in df_hotels['id'].values:
            self.name = df_hotels.loc[df_hotels['id']
                                      == self.id, 'name'].squeeze().title()

    def book(self):
        """
        Marks the hotel as unavailable for booking and updates the DataFrame accordingly.

        """
        # Mark the hotel as unavailable for booking by setting its 'available' column to 'no'
        df_hotels.loc[df_hotels['id'] == self.id, 'available'] = 'no'
        # Save the updated DataFrame to a CSV file, excluding the index
        df_hotels.to_csv(HOTELS_DATA, index=False)

    def available(self):
        """
        Checks the availability of the hotel.

        Returns:
        - bool: True if the hotel is available, False otherwise.
        - str or None: Message indicating the availability status or None if the hotel exists.

        """
        if self.id not in df_hotels['id'].values:
            return False, "-- Hotel with provided ID not found."
        # Filter the DataFrame to get the availability status of the hotel with the given ID
        # Using .loc[] to select rows where 'id' column matches self.id, and 'available' column is selected
        # .squeeze() is used to convert the result to a scalar value (removing extra dimensions)
        availability = df_hotels.loc[df_hotels['id']
                                     == self.id, 'available'].squeeze()

        return availability == 'yes', None


class SpaHotel(Hotel):
    """
    Represents a Spa Hotel, inheriting from the Hotel class.

    This class allows users to book Regular or Premium Spa packages.
    """

    def book_spa_package(self):
        """
        Prompt the user to book a Spa package and set the package type.

        The user is prompted to choose between a Regular package ('r') or a Premium package ('p').

        Returns:
        - None
        """
        while True:
            package_type = input(
                "\n--> Choose a Spa package (Regular/Premium): Enter 'r' or 'p': ").lower()

            # Validate the input to set the package type
            if package_type in ['regular', 'r']:
                self.spa_package = 'Regular'
                break
            elif package_type in ['premium', 'p']:
                self.spa_package = 'Premium'
                break
            else:
                print(
                    "\n-- Error: Please enter 'r'/'regular' for Regular package or 'p'/'premium' for Premium package. --\n")


class HotelReservationTicket:
    def __init__(self, customer_name, hotel_object):
        """
        Initializes a HotelReservationTicket object with the provided customer name and hotel object.

        Parameters:
        - customer_name (str): The name of the customer.
        - hotel_object (Hotel): The Hotel object associated with the reservation.

        """
        self.customer_name = customer_name.title()
        self.hotel = hotel_object

    def generate(self):
        """
        Generates a reservation ticket with customer and hotel details.

        Returns:
        - str: The generated reservation ticket.

        """
        self.content = f"""
Thank you for your reservation!

Here are your booking data:

    - Name: {self.customer_name}
    - Hotel: {self.hotel.name}

"""
        return self.content


class CreditCard:
    def __init__(self, card_number):
        """
        Initializes a CreditCard object with the provided card number.
        """
        self.number = card_number

    # In this app, we currently validate credit cards using a database which is represented by a CSV file. However, in a production environment, such databases are typically hosted remotely. Our program would access these databases through APIs, enabling it to verify the existence of a card within the database.
    def validate(self, expiry_date, holder, cvc_number):
        """
        Validates the credit card information against a database.

        Parameters:
        - expiry_date (str): Expiration date of the credit card (format: MM/YY).
        - holder (str): Name of the cardholder.
        - cvc_number (str): CVC (Card Verification Code) of the credit card.

        Returns:
        - bool: True if the credit card is valid, False otherwise.
        """
        this_card = {
            'number': self.number,
            'expiration': expiry_date,
            'cvc': cvc_number,
            'holder': holder,
        }

        return this_card in df_cards


class SecureCreditCard(CreditCard):
    """
    A subclass of CreditCard that implements additional security features.
    """

    def authenticate(self, password_input):
        """
        Authenticate the credit card using a password.

        Parameters:
        - password_input (str): The password input provided by the user.

        Returns:
        - bool: True if the password input matches the stored password for the card, False otherwise.
        """
        # Extract the stored password for the card from the security database
        this_card_password = df_cards_security.loc[df_cards_security['number']
                                                   == self.number, 'password'].squeeze()
        # Compare the provided password input with the stored password for the card
        return password_input == this_card_password


class SpaReservationTicket:
    def __init__(self, customer_name, hotel_object):
        """
        Initializes a SpaReservationTicket object with the provided customer name and hotel object.

        Parameters:
        - customer_name (str): The name of the customer.
        - hotel_object (Hotel): The Hotel object associated with the reservation.

        """
        self.customer_name = customer_name.title()
        self.hotel = hotel_object

    def generate(self):
        """
        Generates a reservation ticket with customer and hotel with spa package details.

        Returns:
        - str: The generated reservation ticket.

        """
        self.content = f"""
Thank you for your SPA reservation!

Here are your SPA booking data:

    - Name: {self.customer_name}
    - Hotel: {self.hotel.name}
    - Spa Package: {self.hotel.spa_package}

"""
        return self.content


class Receipt(FPDF):
    """
    A class to generate PDF receipts for a list of ticket objects.

    Inherits from FPDF class.
    """

    def __init__(self, tickets):
        """
        Initialize the Receipt object.

        Parameters:
        - tickets (list): A list of ticket objects to be included in the receipt.
        """
        super().__init__(orientation='P', unit='mm', format='A4')

        self.tickets = tickets

        # Generate output path based on current date
        current_date = datetime.now().strftime("%Y_%m_%d")
        self.output_path = RECEIPT_DIR / f"receipt_{current_date}.pdf"

    def generate(self):
        """
        Generate the PDF receipt.

        Adds a page for each ticket, sets font and style, adds ticket information, and outputs the PDF.
        """
        for ticket in self.tickets:
            self.add_page()
            # Add image
            self.image(str(LOGO_FILE), w=30, h=30)
            self.set_font(family='Courier', size=16, style='B')
            self.multi_cell(w=0, h=8, txt=ticket.content)

        # Output the PDF receipt
        self.output(self.output_path)
