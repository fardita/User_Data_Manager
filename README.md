# User Data Management with Tkinter and Pandas

## Overview

This small Python project is designed to manage and interact with user information using a Tkinter-based graphical user interface (GUI) and Pandas for data handling. The project includes two main components:

1. **User Class**: Represents an individual's information, including personal details such as name, surname, gender, employment status, job, country, CAP (Postal Code), and address. The class provides methods to interactively update each attribute. (not totally used in the current data manager version, goal is to enrich it for further development and integration ).

2. **Tkinter UI**: A user interface for interacting with the User class. It includes entry widgets for user input, labels for attribute descriptions, and buttons to trigger various actions like saving to Excel, visualizing data, and modifying existing data.

## User Class

The `User` class includes the following attributes:

- `name`: The person's first name.
- `surname`: The person's last name.
- `gender`: The person's gender (optional).
- `status`: The employment status, default is 'employed'.
- `job`: The person's job title (optional).
- `country`: The country of residence (optional).
- `cap`: The CAP (Postal Code) (optional).
- `address`: The residential address (optional).

### Methods:

- `name_update()`: Allows the user to update the name attribute interactively.
- `surname_update()`: Allows the user to update the surname attribute interactively.
- `status_update()`: Allows the user to update the employment status attribute interactively.
- `job_update()`: Allows the user to update the job attribute interactively.
- `country_update()`: Allows the user to update the country attribute interactively.
- `cap_update()`: Allows the user to update the CAP (Postal Code) attribute interactively.
- `address_update()`: Allows the user to update the address attribute interactively.

## Tkinter User Interface

The `UserUI` class handles the Tkinter user interface. It includes methods for saving user information to an Excel file, visualizing existing data, and editing data. The UI provides a clean layout with entry widgets, labels, and buttons for seamless interaction.

### Usage

1. **Save to Excel**: Enter user information in the respective entry fields and click the "Save to Excel" button to store the data in an Excel file.

2. **Visualize Data**: Click the "Visualize Data" button to display existing data in a new window.

3. **Modify Data**: Click the "Modify Data" button to edit existing data. Enter the index of the data to be edited and confirm the changes in the dialog box.

## Dependencies

Make sure to have the required dependencies installed:

```bash
pip install pandas openpyxl

## How to use it #2
run the exe file UserDataManager!
