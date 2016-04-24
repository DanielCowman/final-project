import requests

# base URL for fixer.io
JSON_URL = 'http://api.fixer.io/latest?base='
# currency table
CURRENCY_TABLE = \
    {
        "USD": 'US Dollar', "GBP": 'Great British Pound', "CAD": 'Canadian dollar', "AUD": 'Australian dollar',
        "BGN": 'Bulgarian lev', "BRL": 'Brazillian real', "CHF": 'Swiss franc', "TRY": 'Turkish lira',
        "CNY": 'Chinese yuan', "CZK": 'Czech koruna', "DKK": 'Danish krone', "HKD": 'Hong Kong dollar',
        "HRK": 'Croatian kuna', "HUF": 'Hungarian forint', "IDR": 'Indonesian rupiah', "ZAR": 'South African rand',
        "ILS": 'Israeli new shekel', "INR": 'Indian rupee', "JPY": 'Japanese yen', "KRW": 'South Korean won',
        "MXN": 'Mexican peso', "MYR": 'Malaysian ringgit', "NOK": 'Norweigian krone', "NZD": 'New Zealand dollar',
        "PHP": 'Phillippine peso', "PLN": 'polish zloty', "RON": 'Romanian new Leu', "RUB": 'Russian ruble',
        "SEK": 'Swedish krona', "SGD": 'Singapore dollar', "THB": 'Thai baht'
    }


def get_user_variables():
    print('Welcome the the currency conversion tool!')
    print('Please locate the countries currency codes from the table below:')
    num = 0

    print("| Code | Country | ")
    # Loops through the currency table and prints the codes with their country
    for code in CURRENCY_TABLE:
        print(code + ": " + CURRENCY_TABLE[code])


def pull_json_data_and_print_result(url):
    # asks the user for the currency codes for both countries that will be used within the program.
    currency_code_from = input("Enter the CURRENCY CODE you would like to convert FROM:")
    currency_code_to = input("Enter the CURRENCY CODE you would like to convert TO:")
    amount_money = input("Enter the AMOUNT of money you would like to convert (Enter integers/numbers only):")

    # crafts the URL
    crafted_url = url + currency_code_from + '&symbols=' + currency_code_to
    # pulls the data from fixer.io and returns it as a dictionary
    response = requests.request("GET", crafted_url).json()
    # find the sum of the money and the current rate of the currency
    converted_total = int(float(amount_money) * float(response["rates"][currency_code_to]))

    print("| FROM: "+ response["base"] + "(" + CURRENCY_TABLE[currency_code_from] + ") | " +
          " TO: " + currency_code_to + "(" + CURRENCY_TABLE[currency_code_to] + ") |")
    print("| DATE: " + response["date"] + "     |  AMOUNT TO CONVERT: " + amount_money + "    |")
    print("| CURRENT RATE: " + str(response["rates"][currency_code_to]) + " |")

    print("You will receive: " + str(converted_total) + " " + CURRENCY_TABLE[currency_code_to])


def main():
    # greet the user and print out the code to country table.
    get_user_variables()
    pull_json_data_and_print_result(JSON_URL)


main()
