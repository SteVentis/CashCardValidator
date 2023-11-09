import re


def clear_input_number_from_spaces_and_dashes(number):
    number_without_spaces = re.sub('-', '', number.replace(' ', ''))
    return number_without_spaces


def check_numbers_length(number):
    if len(number) != 16:
        return False
    return True


def check_the_content_of_card_number(number):
    if not number.isnumeric():
        for i in range(len(number)):
            if number[i].isalpha():
                return number[i]
    else:
        return number


def calculate_sum_of_card_numbers(card_number):
    card_digits = list(map(int, card_number))
    odd_places_numbers = card_digits[0:16:2]
    even_places_numbers = card_digits[1:16:2]
    for i in range(len(odd_places_numbers)):
        odd_places_numbers[i] *= 2
        if odd_places_numbers[i] > 9:
            numbers_with_double_digits = list(map(int, f'{odd_places_numbers[i]}'))
            odd_places_numbers[i] = sum(numbers_with_double_digits)
    sum_of_numbers_in_even_places = sum(even_places_numbers)
    sum_of_numbers_in_odd_places = sum(odd_places_numbers)
    total_sum = sum_of_numbers_in_even_places + sum_of_numbers_in_odd_places
    return total_sum


def check_if_card_is_valid(total_sum_of_card_numbers):
    if total_sum_of_card_numbers % 10 == 0:
        return True
    else:
        return False


def card_display_format(card_number):
    card_num = str(card_number)
    formatted_number = '-'.join(card_num[i:i + 4] for i in range(0, len(card_number), 4))
    return formatted_number


def begin_program():
    run = True
    while run:
        card_number = input('Πληκτρολογήστε τον αριθμό της κάρτας: ')
        cleared_number_card = clear_input_number_from_spaces_and_dashes(card_number)
        is_length_numbers_card_right = check_numbers_length(cleared_number_card)
        if is_length_numbers_card_right:
            content_of_card = check_the_content_of_card_number(cleared_number_card)
            if content_of_card.isnumeric():
                total_sum_of_card = calculate_sum_of_card_numbers(cleared_number_card)
                is_valid = check_if_card_is_valid(total_sum_of_card)
                if is_valid:
                    run = False
                    print(f'Ο αριθμός {card_display_format(content_of_card)} είναι ΕΓΚΥΡΟΣ.')
                    print('Τέλος προγράμματος.')
                else:
                    print(f'Ο αριθμός {card_display_format(content_of_card)} είναι ΑΚΥΡΟΣ.')
                    print('Παρακαλώ επαναλάβετε την εισαγωγή.')
            else:
                print(f'Μη επιτρεπτός χαρακτήρας: {content_of_card}')
                print('Παρακαλώ επαναλάβετε την εισαγωγή.')
        else:
            print('Ο αριθμός πρέπει να έχει 16 ψηφία.')
            print('Παρακαλώ επαναλάβετε την εισαγωγή.')


begin_program()
