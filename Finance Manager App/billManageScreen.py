import PySimpleGUI as sg
import menuScreen


def billCalc(housing, car, insurance, utilities, loans, creditCard, expenses, subscription, income,username):
    # Calculate total due and remaining money
    totalDue = int(housing) + int(car) + int(insurance) + int(utilities) + int(loans) + int(creditCard) + int(
        expenses) + int(subscription)
    remainingMoney = int(income) - totalDue

    # Determine remaining money message based on calculation
    if remainingMoney > 0:
        remainingMoney = f"${remainingMoney}"
    elif remainingMoney == 0:
        remainingMoney = "You have no remaining money"
    else:
        remainingMoney = f"You have ${-remainingMoney} in debt."

    # Define the income statement for display
    billManage = [
        ['Housing', f"${housing}"],
        ['Car', f"${car}"],
        ['Insurance', f"${insurance}"],
        ['Utilities', f"${utilities}"],
        ['Loan Payments', f"${loans}"],
        ['Credit Card', f"${creditCard}"],
        ['Day Expenses', f"${expenses}"],
        ['Subscription', f"${subscription}"],
        ['Total Payment Due', f"${totalDue}"],
        ['Remaining Money', remainingMoney]
    ]

    # Define the layout for the pop-up window
    layout = [
        [sg.Text('Bill Management', font=('Helvetica', 20), justification='center')],
        [sg.Table(values=billManage,
                  headings=['Category', 'Amount'],
                  auto_size_columns=False,
                  col_widths=[30, 30],
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


def manage(username):
    # Define the layout for the management screen
    layout = [
        [sg.Text('Enter the following information:')],
        [sg.Text('Rent/Mortgage per month: $'), sg.Input(key='-housing-')],
        [sg.Text('Car payment per month: $'), sg.Input(key='-car-')],
        [sg.Text('Insurance per month: $'), sg.Input(key='-insurance-')],
        [sg.Text('Utilities per month: $'), sg.Input(key='-utilities-')],
        [sg.Text('Student Loan payments per month: $'), sg.Input(key='-loan-')],
        [sg.Text('Credit Card payments per month: $'), sg.Input(key='-creditCard-')],
        [sg.Text('Day to day expenses per month: $'), sg.Input(key='-expenses-')],
        [sg.Text('Subscription services per month: $'), sg.Input(key='-subscription-')],
        [sg.Text('Monthly Income: $'), sg.Input(key='-income-')],
        [sg.Button('Submit'), sg.Button('Back')],
    ]

    window = sg.Window('Personal Finance Manager', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Back':
            window.close()
            menuScreen.menu(username)
        elif event == 'Submit':
            # Extract values from inputs
            housing = values['-housing-']
            car = values['-car-']
            insurance = values['-insurance-']
            utilities = values['-utilities-']
            loans = values['-loan-']
            creditCard = values['-creditCard-']
            expenses = values['-expenses-']
            subscription = values['-subscription-']
            income = values['-income-']

            window.close()
            billCalc(housing, car, insurance, utilities, loans, creditCard, expenses, subscription, income,username)
