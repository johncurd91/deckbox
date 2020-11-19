import csv


# Search inventory for single card and count
def single_card_search():
    with open('inventory.csv', 'r') as inventory_file:
        csv_reader = csv.DictReader(inventory_file, delimiter=',')

        user_input = input('Enter card name: ')
        card_count = 0
        for row in csv_reader:
            if user_input == row['Name']:
                card_count = int(row['Count'])

        print(f'{card_count} cards named \'{user_input}\' found.')


# Search inventory using decklist for cards owned
def deck_list_search():
    with open('inventory.csv', 'r') as inventory_file:
        csv_reader = csv.DictReader(inventory_file, delimiter=',')
        card_list = [row['Name'] for row in csv_reader]

    with open('decklist.txt', 'r') as decklist_file:
        decklist = decklist_file.readlines()
        decklist_scrubbed = [i[2:].rstrip('\n') for i in decklist]

    cards_owned = [card for card in decklist_scrubbed if card in card_list]
    cards_not_owned = [card for card in decklist_scrubbed if card not in card_list]

    print(f' Cards already owned: {cards_owned}')
    print(f' Missing cards: {cards_not_owned}')


# Calculated total value of cards above minimum price
def total_value_min(conversion, min_price):
    with open('inventory.csv', 'r') as inventory_file:
        csv_reader = csv.DictReader(inventory_file, delimiter=',')

        total_USD = 0
        for row in csv_reader:
            if float(row['Price'][1:]) * conversion >= min_price:
                total_USD += (float(row['Price'][1:])) * int(row['Count'])
        total_GBP = total_USD * conversion

        print(f' Total value of cards above £{min_price}: £{round(total_GBP, 2)}')


total_value_min(0.81, 2)



