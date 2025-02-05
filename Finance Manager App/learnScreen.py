import PySimpleGUI as sg
import menuScreen

# Define the strategies for investing, saving, and managing debt
investing = "-Set clear investment goals\n" \
            "-Diversify your portfolio\n" \
            "-Conduct thorough research\n" \
            "-Consider your risk tolerance\n" \
            "-Have a long-term perspective\n" \
            "-Regularly review and rebalance your portfolio\n" \
            "-Stay disciplined and avoid emotional decision-making\n" \
            "-Consider seeking professional advice."

saving = "-Create a budget and track expenses\n" \
         "-Set specific savings goals\n" \
         "-Pay yourself first by automating savings transfers\n" \
         "-Minimize unnecessary expenses\n" \
         "-Reduce high-interest debt\n" \
         "-Follow the 50/30/20 rule: essentials, discretionary, savings\n" \
         "-Cut unnecessary subscriptions.\n" \
         "-Automate savings transfers\n" \
         "-Save windfalls and bonuses\n" \
         "-Utilize saving apps and tools\n"

debt = "-Create a budget to track income and expenses.\n" \
       "-Prioritize high-interest debt.\n" \
       "-Use the snowball or avalanche method for debt repayment.\n" \
       "-Negotiate lower interest rates with creditors.\n" \
       "-Consider debt consolidation or refinancing.\n" \
       "-Cut expenses and increase income to allocate more towards debt repayment\n" \
       "-Seek professional advice if needed..\n" \
       "-Automate savings transfers\n" \
       "-Avoid taking on new debt.\n" \
       "-Stay organized with payment due dates and progress.\n"


def popUp(info,username):
    # Define the layout of the popup window
    layout = [
        [sg.Button('Back')],
        [sg.Text(info, font=("Helvetica", 12))]
    ]
    window = sg.Window('Finance Strategies', layout, element_justification='center', size=(500, 300))

    # Event loop to process events and keep the window open
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == '-CLOSE-':
            break
        elif event == 'Back':
            window.close()
            learnMenu(username)

    # Close the window
    window.close()


def learnMenu(username):
    layout = [
        [sg.Text('Learn about your finances', justification='center', font=('Helvetica', 20))],
        [sg.Button('Investing Strategies', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))],
        [sg.Button('Saving Strategies', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))],
        [sg.Button('Managing Debt', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))],
        [sg.Button('Back', size=(10, 1), pad=(1, 1), font=('Helvetica', 15))]
    ]

    window = sg.Window('Personal Finance Manager', layout, size=(600, 400), element_justification='center')

    # Event loop to process events and display the window
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Investing Strategies':
            window.close()
            popUp(investing,username)
        elif event == 'Saving Strategies':
            window.close()
            popUp(saving,username)
        elif event == 'Managing Debt':
            window.close()
            popUp(debt,username)
        elif event == 'Back':
            window.close()
            menuScreen.menu(username)

    # Close the window
    window.close()
