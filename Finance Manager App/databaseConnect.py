import psycopg2
import PySimpleGUI as sg
import menuScreen

# Function to connect to the PostgreSQL database
def connect_to_db():
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
    - psycopg2 connection object: Connection to the database if successful, otherwise None.
    """
    try:
        conn = psycopg2.connect(
            dbname="finance_Manager_App",
            user="postgres",
            password="duke1088",
            host="localhost",
            port=5432
        )
        return conn
    except Exception as error:
        sg.popup("Error connecting to the database:", error)
        return None

# Function for the start screen
def start_screen():
    """
    Displays the start screen of the Personal Finance Manager application.
    Allows users to sign up, login, or exit the application.
    """
    layout = [
        [sg.Text("Welcome to Personal Finance Manager", font=("Helvetica", 16), justification="center", pad=(0, 20))],
        [sg.Button("Sign Up", size=(15, 1), pad=(0, 10))],
        [sg.Button("Login", size=(15, 1), pad=(0, 10))],
        [sg.Button("Exit", size=(15, 1), pad=(0, 10))]
    ]

    window = sg.Window("Personal Finance Manager", layout, size=(300, 250))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break

        if event == "Sign Up":
            window.close()
            signup()
        elif event == "Login":
            window.close()
            login()

    window.close()

# Function for the sign-up screen
def signup():
    """
    Displays the sign-up screen for new users to create an account.
    """
    layout = [
        [sg.Text("Sign Up", font=("Helvetica", 20), justification="center")],
        [sg.Text("Username"), sg.Input(key="-USERNAME-")],
        [sg.Text("Password"), sg.Input(key="-PASSWORD-", password_char="*")],
        [sg.Button("Sign Up"), sg.Button("Cancel")]
    ]

    window = sg.Window("Sign Up", layout, size=(400, 200))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        username = values["-USERNAME-"]
        password = values["-PASSWORD-"]

        # Perform sign-up processing
        conn = connect_to_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute('INSERT INTO "userInfo" (username, password) VALUES (%s, %s)', (username, password))
                conn.commit()
                sg.popup("Sign Up Successful!")
            except Exception as error:
                sg.popup("Error during sign up:", error)
            finally:
                cur.close()
                conn.close()

        window.close()
        start_screen()
        break

    window.close()

# Function for the login screen
def login():
    """
    Displays the login screen for existing users to log into their account.
    """
    layout = [
        [sg.Text("Login", font=("Helvetica", 20), justification="center")],
        [sg.Text("Username"), sg.Input(key="-USERNAME-")],
        [sg.Text("Password"), sg.Input(key="-PASSWORD-", password_char="*")],
        [sg.Button("Login"), sg.Button("Cancel")]
    ]

    window = sg.Window("Login", layout, size=(400, 200))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break

        userUsername = values["-USERNAME-"]
        userPassword = values["-PASSWORD-"]

        # Perform login validation
        conn = connect_to_db()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute('SELECT username, password FROM "userInfo" WHERE username = %s', (userUsername,))
                record = cur.fetchone()

               
                if record:
                    stored_username, stored_password = record
                    print(f"Debug: Stored Username: {stored_username}, Stored Password: {stored_password}")

                    # Convert the stored password to a string before comparison
                    if str(stored_password) == userPassword:
                        sg.popup("Login Successful!")
                        window.close()
                        menuScreen.menu(stored_username)
                        break
                    else:
                        sg.popup("Invalid username or password. Please try again.")
                else:
                    sg.popup("Invalid username or password. Please try again.")
            except Exception as error:
                sg.popup("Error during login:", error)
            finally:
                cur.close()
                conn.close()

    window.close()
    start_screen()

if __name__ == "__main__":
    start_screen()
