import PySimpleGUI as sg
import menuScreen


def netIncome(revenue, gains, expenses, losses,username):
    # Calculate net income
    NetIncome = (int(revenue) + int(gains)) - (int(expenses) + int(losses))

    # Define the income statement for display
    income_statement = [
        ['Revenue', f"${revenue}"],
        ['Gains', f"${gains}"],
        ['Expenses', f"${expenses}"],
        ['Losses', f"${losses}"],
        ['Net Income', f"${NetIncome}"]
    ]

    # Define the layout for the pop-up window
    layout = [
        [sg.Text('Income Statement', font=('Helvetica', 20), justification='center')],
        [sg.Table(values=income_statement,
                  headings=['Category', 'Amount'],
                  auto_size_columns=False,
                  col_widths=[20, 10],
                  font=('Helvetica', 16),
                  justification='left')],
        [sg.Button('Back', size=(10, 2), pad=(20, 20), font=('Helvetica', 14))]
    ]

    # Create the pop-up window
    window = sg.Window('Personal Finance Manager', layout)

    # Display the pop-up and wait for a button click
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Back':
            window.close()
            menuScreen.menu(username)

    window.close()


def incomeStatement(username):
    # Define the layout for the input page
    layout = [
        [sg.Text('Enter data to Calculate Income Statement:')],
        [sg.Text("Revenue($)"), sg.Input(size=(60, 30), font=("Helvetica", 20), key='-revenue-')],
        [sg.Text("Gains($)"), sg.Input(size=(60, 30), font=("Helvetica", 20), key='-gains-')],
        [sg.Text("Expenses($)"), sg.Input(size=(60, 30), font=("Helvetica", 20), key='-expenses-')],
        [sg.Text("Losses($)"), sg.Input(size=(60, 30), font=("Helvetica", 20), key='-losses-')],
        [sg.Button('Submit')]
    ]

    # Create the window
    window = sg.Window('Personal Finance Manager', layout, size=(600, 400), element_justification='center')

    # Event loop to process events and display the window
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Submit':
            revenue = values['-revenue-']
            gains = values['-gains-']
            expenses = values['-expenses-']
            losses = values['-losses-']
            netIncome(revenue, gains, expenses, losses,username)
            window.close()

