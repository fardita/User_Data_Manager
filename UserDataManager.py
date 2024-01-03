import tkinter as tk
from tkinter import ttk, simpledialog, scrolledtext
import pandas as pd

class User():
    """
    Represents an individual's information, including personal details such as name, surname, gender, employment status,
    job, country, CAP (Postal Code), and address.

    Attributes:
    - name (str): The person's first name.
    - surname (str): The person's last name.
    - gender (str, optional): The person's gender.
    - status (str): The employment status, default is 'employed'.
    - job (str, optional): The person's job title.
    - country (str, optional): The country of residence.
    - cap (str, optional): The CAP (Postal Code).
    - address (str, optional): The residential address.

    Methods:
    - name_update(): Allows the user to update the name attribute interactively.
    - surname_update(): Allows the user to update the surname attribute interactively.
    - status_update(): Allows the user to update the employment status attribute interactively.
    - job_update(): Allows the user to update the job attribute interactively.
    - country_update(): Allows the user to update the country attribute interactively.
    - cap_update(): Allows the user to update the CAP (Postal Code) attribute interactively.
    - address_update(): Allows the user to update the address attribute interactively.
    """
    def __init__(self,
                 name:str,
                 surname:str,
                 gender:str=None,
                 status:str='employed',
                 job:str=None,
                 country:str =None,
                 cap:str=None,
                 address:str=None
                ):
        self.name = str(name)
        self.surname = str(surname)
        self.gender = str(gender)
        self.status = str(status)
        self.job = job
        self.country = country
        self.cap = cap
        self.address = address

    def name_update(self):
        new_name = input('insert new name: ')
        self.name = new_name
        return self.name
    

    def surname_update(self):
        new_surname = input('insert new surname: ')
        self.surname = new_surname
        return self.surname
    
    def status_update(self):
        new_status = input('insert new status: ')
        self.status = new_status
        return self.status
    
    def job_update(self):
        new_job = input('insert new job: ')
        self.job = new_job
        return self.job
    
    def country_update(self):
        new_country = input('insert new country: ')
        self.country = new_country
        return self.country
    
    def cap_update(self):
        new_cap = input('insert new cap: ')
        self.cap = new_cap
        return self.cap
    
    def address_update(self):
        new_address = input('insert new address: ')
        self.address = new_address
        return self.address


class UserUI:
    """
    Handles the Tkinter user interface to interact with the User class. Includes entry widgets for user input, labels
    for attribute descriptions, and buttons to trigger various actions.

    Methods:
    - __init__(self, master): Initializes the Tkinter user interface with labels, entry widgets, and buttons.
    - save_to_excel(self): Retrieves user input from the UI, updates the User instance, reads existing data from an Excel
      file, appends the new data, and saves it back to the file.
    - show_data(self): Displays the existing data in the terminal.
    - edit_data(self): Launches a dialog to edit existing data.
    - edit_data_dialog(self, current_data): Creates a dialog for editing data.
    - on_confirm_edit(self, name_var, surname_var, status_var, dialog): Handles the confirmation of editing data.
    """
    
    def __init__(self, master):
        self.master = master
        self.master.title("User Informations")

        self.User = User(name="", surname="")  # Create an instance of the User class

        # Labels
        title_label = ttk.Label(self.master, text="User Informations",foreground="red")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(self.master, text="Name:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.master, text="Surname:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.master, text="Status:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.master, text="Job:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        # Entry widgets
        self.name_entry = ttk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.surname_entry = ttk.Entry(self.master)
        self.surname_entry.grid(row=2, column=1, padx=5, pady=5)
        self.status_entry = ttk.Entry(self.master)
        self.status_entry.grid(row=3, column=1, padx=5, pady=5)
        self.job_entry = ttk.Entry(self.master)
        self.job_entry.grid(row=4, column=1, padx=5, pady=5)

        # Save button
        ttk.Button(self.master, text="Save to Excel", command=self.save_to_excel).grid(row=5, column=0, columnspan=2, pady=10)

        # Additional buttons for functionalities
        ttk.Button(self.master, text="Visualize Data", command=self.show_data).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(self.master, text="Modify Data", command=self.edit_data).grid(row=7, column=0, columnspan=2, pady=10)

    def save_to_excel(self):
        """
        Saves User information to an Excel file.

        Updates the User instance with user input and appends the data to an existing Excel file or creates a new file.
        """
        # Update User instance with user input
        self.User.name = self.name_entry.get()
        self.User.surname = self.surname_entry.get()
        self.User.status = self.status_entry.get()
        self.User.job = self.job_entry.get()

        # Create a DataFrame with User data
        data = {'Name': [self.User.name],
                'Surname': [self.User.surname],
                'Status': [self.User.status],
                'Job': [self.User.job]}
        
        try:
            existing_data = pd.read_excel('User_data.xlsx')
            df = pd.concat([existing_data, pd.DataFrame(data)], ignore_index=True)
        except FileNotFoundError:
            # If the file doesn't exist, create a new df
            df = pd.DataFrame(data)

        # Save df to Excel with write mode
        with pd.ExcelWriter('User_data.xlsx', engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, index=False, sheet_name='User_List')

        print("Data appended to User_data.xlsx")

    

    def show_data(self):
        """
        Displays User data in a new window UI.
        """
        try:
            existing_data = pd.read_excel('User_data.xlsx')

            # Controlla se la finestra esiste già e distruggila se necessario
            if hasattr(self, 'data_window') and self.data_window.winfo_exists():
                self.data_window.destroy()

            # Crea una nuova finestra per visualizzare i dati
            self.data_window = tk.Toplevel(self.master)
            self.data_window.title("User Data")

            # Crea un widget Text per visualizzare i dati con una griglia
            data_text = scrolledtext.ScrolledText(self.data_window, wrap=tk.WORD, width=50, height=10)
            data_text.grid(row=0, column=0, padx=10, pady=10)

            # Inserisci i dati nel widget Text con una griglia e l'indice
            data_text.insert(tk.END, existing_data.to_string(index=True))

        except FileNotFoundError:
            error_label = ttk.Label(self.master, text="Il file 'User_data.xlsx' non esiste ancora.")
            error_label.grid(row=7, column=0, columnspan=2, pady=10)



    def edit_data(self):
        """
        Edits User data based on user input.
        """
        try:
            existing_data = pd.read_excel('User_data.xlsx')
            selected_data = simpledialog.askinteger("Edit Data", "Enter index to edit:")
            
            if selected_data is not None and 0 <= selected_data < len(existing_data):
                current_data = existing_data.iloc[selected_data]
                updated_data = self.edit_data_dialog(current_data)
                
                # Create a new DataFrame with the updated data
                updated_row = pd.DataFrame([updated_data], columns=existing_data.columns)
                
                # Update the values at the specified index
                existing_data.iloc[selected_data] = updated_row.iloc[0]

                # Save the modified DataFrame to Excel
                existing_data.to_excel('User_data.xlsx', index=False, sheet_name='Sheet1')
                print("Data edited successfully.")
            else:
                print("Invalid index.")
                
        except FileNotFoundError:
            print("The file 'User_data.xlsx' does not exist yet.")



    def edit_data_dialog(self, current_data):
        """
        Displays a dialog for editing User data.

        Parameters:
        - current_data: The current User data to be edited.

        Returns:
        - dict: A dictionary containing the updated User data.
        """

        dialog = tk.Toplevel(self.master)
        dialog.title("Edit Data")

        name_var = tk.StringVar(value=current_data['Name'])
        surname_var = tk.StringVar(value=current_data['Surname'])
        status_var = tk.StringVar(value=current_data['Status'])
        job_var = tk.StringVar(value=current_data['Job'])

        name_entry = ttk.Entry(dialog, textvariable=name_var)
        surname_entry = ttk.Entry(dialog, textvariable=surname_var)
        status_entry = ttk.Entry(dialog, textvariable=status_var)
        job_entry = ttk.Entry(dialog,textvariable=job_var)

        ttk.Label(dialog, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(dialog, text="Surname:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        surname_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(dialog, text="Status:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        status_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(dialog, text="Job:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        job_entry.grid(row=3, column=1, padx=5, pady=5)

        confirm_button = ttk.Button(dialog, text="Confirm Edit", command=lambda: self.on_confirm_edit(name_var, surname_var, status_var,job_var, dialog))
        confirm_button.grid(row=4, column=0, columnspan=2, pady=10)
        dialog.wait_window()
        dict = {
            'Name': name_var.get(),
            'Surname': surname_var.get(),
            'Status': status_var.get(),
            'Job': job_var.get()
        }
        return dict

    
    def on_confirm_edit(self, name_var, surname_var, status_var,job_var, dialog):
        updated_data = {
            'Name': name_var.get(),
            'Surname': surname_var.get(),
            'Status': status_var.get(),
            'Job': job_var.get()
        }

        
        print(updated_data)

        # Destroy the window
        dialog.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = UserUI(root)
    root.mainloop()
