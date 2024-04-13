# Hotel Booking System

## Overview
Hotel Booking System is a Python application that allows users to book hotels and spa packages. It provides functionalities for hotel reservation, credit card validation, and generating PDF receipts. In this app, credit cards are currently validated using a database represented by a CSV file. However, in a production environment, such databases are typically hosted remotely. The program would access these databases through APIs, enabling it to verify the existence of a card within the database. Additionally, users have the flexibility to customize the data by modifying the custom data files located in the `assets/data` directory, including `hotels.csv`, `cards.csv`, and `card_security.csv`, to suit their preferences. While the application is functional, there is room for improvement in terms of data collection and management, whether it's updating hotel information or enhancing the card validation process.


## Features
- **Hotel Booking**: Users can search for hotels and make reservations.
- **Spa Package Booking**: Users can book spa packages along with their hotel reservations.
- **Credit Card Validation**: Credit card information entered by users is validated against a database.
- **PDF Receipt Generation**: The application generates PDF receipts for hotel and spa reservations.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as file paths in `constants.py`.
5. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. Follow the prompts to book hotels, spa packages, and provide credit card information.
3. After completing the booking process, the application will generate a PDF receipt in the `assets/receipts` directory.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.


