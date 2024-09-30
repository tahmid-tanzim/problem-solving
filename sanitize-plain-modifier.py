#!/usr/bin/python3
import re

# Do not add american cheese with famous star with cheese
discard_modifiers_for_plain_item = {
    """
    If this items ordered as plain then 
    discard the following modifiers.
    """
    'item_names': [
        "big carl",
        "famous star",
        "super star",
        "cheeseburger",
        "cheese burger",
    ],
    'modifiers': [
        ("add", "american", "cheese"),
        ("add", "lettuce"),
    ]
}

"""
Bypass adding cheese & lettuce modifier to the plain item
"""
"""
def sanitize_plain_modifiers(cart):
    updated_cart = list()
    plain_mod_index_list = list()
    for i in range(len(cart)):
        updated_cart.append(cart[i])
        if "- plain" in cart[i].lower():
            plain_mod_index_list.append(i)
    
    if len(plain_mod_index_list) == 0:
        return cart

    for i in plain_mod_index_list:
        j = i - 1
        while j >= 0:
            if re.match("^- ([0-9]+)( |x)", cart[j], re.IGNORECASE):
                plain_item = cart[j]
                if any(
                        item_name
                        for item_name in discard_modifiers_for_plain_item['item_names']
                        if item_name in plain_item.lower()
                ):
                    print('\n\nParent Item', plain_item, j)
                    print('Corresponding Plain Item', cart[i], i)
                    for k in range(j + 1, len(cart)):
                        if re.match("^- ([0-9]+)( |x)", cart[k], re.IGNORECASE):
                            break
                        print('\t child mods:', cart[k], k)
                        for modifier in discard_modifiers_for_plain_item['modifiers']:
                            if is_all_words_exist_in_string(modifier, cart[k]):
                                print('This Mod need to be deleted:', cart[k], k)
                break
            j -= 1
    print('plain_index_list: ', plain_mod_index_list)

    return cart
"""


def sanitize_plain_modifiers(cart):
    """
    Bypass adding cheese & lettuce modifier to the plain item
    """
    updated_cart = list()
    current_main_item = {
        'index': -1,
        'plain_mod_found': False
    }
    for index, current_item in enumerate(cart):
        updated_cart.append(current_item)
        if re.match("^- ([0-9]+)( |x)", current_item, re.IGNORECASE):
            """
            Identify current main item based on quantity number. 
            For e.g. Here first & third item should be considered as main item.
            cart = [
                '- 1 x Famous Star with Cheese',
                ' - Add Onion',
                '- 1 x Double Big Carl'   # current_item && current_main_item
            ]
            """
            current_main_item['index'] = index
            current_main_item['plain_mod_found'] = False
        elif "- plain" in current_item.lower():
            """
            If we already add any discarded modifier under current item then delete it.
            For e.g. Here second item will be deleted.
            cart = [
                '- 1 x Famous Star with Cheese',
                ' - Add American Cheese',
                ' - Plain'   # current_item
            ]
            """
            current_main_item['plain_mod_found'] = True
            mod_index = len(updated_cart) - 1
            while mod_index > current_main_item['index']:
                for modifier in discard_modifiers_for_plain_item['modifiers']:
                    if is_all_words_exist_in_string(modifier, updated_cart[mod_index]):
                        del updated_cart[mod_index]
                mod_index -= 1
            continue
        elif current_main_item['plain_mod_found']:
            """
            If the last item is a discarded modifier then delete it.
            For e.g. Here last item will be deleted.
            cart = [
                '- 1 x Famous Star with Cheese',
                ' - Plain',
                ' - Add American Cheese'  # current_item
            ]
           """
            for modifier in discard_modifiers_for_plain_item['modifiers']:
                if is_all_words_exist_in_string(modifier, current_item):
                    del updated_cart[-1]

    return updated_cart


def is_all_words_exist_in_string(word_list, input_string):
    # Convert the input string to lowercase and split into words
    string_words = input_string.lower().split()

    # Create a list to store matching words
    matching_words = []

    # Check each word in the word list
    for word in word_list:
        # If the word is in the string, add it to matching words
        if word.lower() in string_words:
            matching_words.append(word)

    return len(matching_words) == len(word_list)


if __name__ == "__main__":
    # print(sanitize_plain_modifiers(
    #     cart=[
    #         '- 2 x Famous Star with Cheese',
    #         ' - Plain',
    #         ' - Add Mayonnaise',
    #         ' - Add American Cheese',
    #         ' - Add Lettuce',
    #     ]
    # ))

    # print(sanitize_plain_modifiers(
    #     cart=[
    #         '- 1 x Double Big Carl',
    #         ' - Plain',
    #         ' - Add American Cheese',
    #         ''
    #     ]
    # ))

    print(sanitize_plain_modifiers(
        cart=[
            '- 1 x Famous Star with Cheese',
            ' - Plain',
            ' - Add Mayonnaise',
            ' - Add American Cheese',
            ' - Add Lettuce',
            '- 1x Cheeseburger Kids Meal',
            ' - Kids Fries',
            ' - Plain',
            ' - Add American Cheese',
            '',
            ' - Drink Placeholder',
            '- 1 x Double Big Carl',
            ' - Plain',
            ' - Add Ketchup',
            '',
            '- 1 x Double Famous Star LARGE Combo',
            ' - LARGE Fries',
            ' - LARGE Hand Crafted Lemonade',
            ' - No Special Sauce',
            ' - No Pickles',
            '- 1 x Super Star with Cheese',
            ' - Add Mayonnaise',
            ' - Add Swiss Cheese',
            ' - Plain',
            ' - Add Lettuce',
            ' - Plain',
        ]
    ))

    # print(sanitize_plain_modifiers(
    #     cart=[
    #         '- 1 x Double Famous Star LARGE Combo',
    #         ' - LARGE Fries',
    #         ' - LARGE Hand Crafted Lemonade',
    #         ' - No Special Sauce',
    #         ' - No Pickles',
    #         '- 1 x Cheeseburger Kids Meal',
    #         ' - Kids Fries',
    #         ' - Plain',
    #         ' - Add American Cheese',
    #         '',
    #         ' - Drink Placeholder'
    #     ]
    # ))

    print(sanitize_plain_modifiers(
        cart=[
            '- 1 x Famous Star with Cheese',
            ' - Add Mayonnaise',
            ' - Add American Cheese',
            ' - Add Lettuce',

        ]
    ))


