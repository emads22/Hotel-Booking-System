import pandas as pd
from constants import *



class Hotel:
    def __init__(self, hotel_id):
        self.id = hotel_id

        if hotel_id in df['id'].values:
            self.name = df.loc[df['id'] == self.id, 'name'].squeeze().title()

    def book(self):
        df.loc[df['id'] == self.id, 'available'] = 'no'

        df.to_csv(HOTELS_DATA, index=False)

    def available(self):

        if self.id not in df['id'].values:
            return False, "-- Hotel with provided ID not found."

        availability = df.loc[df['id'] == self.id, 'available'].squeeze()

        return availability == 'yes', None


class ReservationTicket:
    def __init__(self, cutomer_name, hotel_object):
        self.customer_name = cutomer_name.title()
        self.hotel = hotel_object

    def generate(self):
        content = f"""
Thank you for your reservation!

Here are your booking data:

    - Name: {self.customer_name}
    - Hotel: {self.hotel.name}

"""
        return content


df = pd.read_csv(HOTELS_DATA, dtype={'id': 'str'})


def app():
    print(df)
    hotel_id = input("\n- Enter the hotel ID for booking: ")
    hotel = Hotel(hotel_id)

    check_hotel, message = hotel.available()

    if check_hotel:
        hotel.book()
        name = input("\n- Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        ticket = reservation_ticket.generate()
        print("\n\n", ticket, "\n")

    else:
        if message:
            print(f"\n{message}\n")
        else:
            print("\n-- Hotel with provided ID is not available.\n")


if __name__ == '__main__':
    app()
