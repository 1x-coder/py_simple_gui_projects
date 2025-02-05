# Python Financial Manager Application

A financial management application designed to help users track and analyze their financial data with real-time stock monitoring using the Alpha Vantage API. It features an intuitive PySimpleGUI interface, a secure PostgreSQL database for personalized data storage, and tools like an income statement generator and bill management system for comprehensive financial planning. 

## Database and SQL Interaction
I created a PostgreSQL database for this project using pgAdmin 4 to securely store user data such as usernames, passwords, and stocks. The application leverages psycopg2 for seamless database connection and interaction, executing key SQL queries for functionalities such as inserting new users during sign-up, validating login credentials, and dynamically managing user stock lists. These queries ensure efficient data retrieval and manipulation.

## API Implementation and API key
This application utilizes the Alpha Vantage API to retrieve real-time stock data and company information. The API is integrated into the code to fetch financial data such as current stock prices, industry descriptions, and company overviews.

API Key Access: The code currently includes my personal API key (9QS4OVT4F4N2BPT1) for demonstration purposes. If you clone this repository, you can use this key. However, note that the API has request limits. If you exceed these limits or want to use your own API key, you can easily generate one for free.

Steps to Generate Your Own API Key:
  1. Visit Alpha Vantage's API signup page.
  2. Register for an account.
  3. Once registered, you'll receive an API key via email.
  4. Replace the existing API key in the code at the marked location in 'stockScreen.py' script.

## Installation
  1. Clone the repository in IDE of choice using: https://github.com/cshevick/Finance_Manager_App.git
  2. Install the required dependencies: pip install pandas alpha_vantage PySimpleGUI psycopg2-binary

## Usage
Once you have cloned the repository, run the 'main.py', which will trigger the application and prompt you to either sign up or log in. For first-time users, click the sign-up button and create a username and password. Then, use both of these to log in. Once logged in, you can navigate the app in many ways, including assessing real stock information by entering the stock ticker symbol, which gives you the current price per share and a brief company description. You can add this stock to your stock list, which you can view on the same screen by clicking the designated button. Users can also interact with a bill management screen, an income statement generator, and a learn feature.

## License
This project is open source and licensed under the MIT License. Feel free to modify and use the code as you need.
