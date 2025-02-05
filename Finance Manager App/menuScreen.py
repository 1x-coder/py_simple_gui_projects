import PySimpleGUI as sg
import incomeStatementScreen
import stockScreen
import billManageScreen
import learnScreen



def menu(username):
    # Define the layout for the big screen
    layout = [
        [sg.Text('Welcome to your Financial Manager', justification='center', font=('Helvetica', 20))],
        [sg.Button('Stock Market', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))],
        [sg.Button('Income Statement', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))],
        [sg.Button('Bill Management', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))],
        [sg.Button('Learn', size=(20, 2), pad=(1, 1), font=('Helvetica', 15))]
    ]

    # Create the window
    window = sg.Window('Personal Finance Manager', layout, size=(600, 400), element_justification='center')

    # Event loop to process events and display the window
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Stock Market':
            window.close()
            stockScreen.getInfo(username)

        elif event == 'Income Statement':
            window.close()
            incomeStatementScreen.incomeStatement(username)

        elif event == 'Bill Management':
            window.close()
            billManageScreen.manage(username)
        elif event == 'Learn':
            window.close()
            learnScreen.learnMenu(username)

    # Close the window
    window.close()

