import pandas as pd
from constants import *


# Read the hotel data from a CSV file, ensuring the 'id' column is treated as string
df = pd.read_csv(HOTELS_DATA, dtype={'id': 'str'})


class Hotel:
    def __init__(self, hotel_id):
        """
        Initializes a Hotel object with the provided ID and retrieves its name from the DataFrame.

        Parameters:
        - hotel_id (str): The ID of the hotel.

        """
        self.id = hotel_id

        if hotel_id in df['id'].values:
            self.name = df.loc[df['id'] == self.id, 'name'].squeeze().title()

    def book(self):
        """
        Marks the hotel as unavailable for booking and updates the DataFrame accordingly.

        """
        # Mark the hotel as unavailable for booking by setting its 'available' column to 'no'
        df.loc[df['id'] == self.id, 'available'] = 'no'
        # Save the updated DataFrame to a CSV file, excluding the index
        df.to_csv(HOTELS_DATA, index=False)

    def available(self):
        """
        Checks the availability of the hotel.

        Returns:
        - bool: True if the hotel is available, False otherwise.
        - str or None: Message indicating the availability status or None if the hotel exists.

        """
        if self.id not in df['id'].values:
            return False, "-- Hotel with provided ID not found."
        # Filter the DataFrame to get the availability status of the hotel with the given ID
        # Using .loc[] to select rows where 'id' column matches self.id, and 'available' column is selected
        # .squeeze() is used to convert the result to a scalar value (removing extra dimensions)
        availability = df.loc[df['id'] == self.id, 'available'].squeeze()

        return availability == 'yes', None


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        """
        Initializes a ReservationTicket object with the provided customer name and hotel object.

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
        content = f"""
Thank you for your reservation!

Here are your booking data:

    - Name: {self.customer_name}
    - Hotel: {self.hotel.name}

"""
        return content
