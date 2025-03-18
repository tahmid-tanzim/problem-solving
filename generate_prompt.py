#!/usr/bin/python3

burger_names = {'famous star with cheese', 'el diablo', 'double angus el diablo', 'double ghost breakfast burger combo lunch', 'big char chile burger', 'the breakfast burger', 'teriyaki double angus burger', 'sourdough star', 'big cheeseburger', 'guacamole angus burger', 'guacamole bacon cheeseburger', 'teriyaki burger', 'ghost burger', 'double guacamole angus burger', 'double cheeseburger', 'french toast dips combo lunch', 'ghost breakfast burger', 'angus ghost burger', 'double angus ghost burger', 'ghost breakfast burger combo lunch', 'western bacon cheeseburger', 'el diablo double', 'double angus big carl', 'jalapeno double cheeseburger', 'teriyaki double burger', 'junior cheeseburger', 'no meat el diablo', 'double angus western bacon cheeseburger', 'double big char chile burger', 'angus western bacon cheeseburger', 'el diablo angus', 'angus spicy western bacon', 'double ghost burger', 'double spicy breakfast burger', 'double ghost breakfast burger', 'double angus famous star', 'triple spicy western bacon cheeseburger', 'spicy breakfast burger combo lunch', 'double sourdough star', 'single big carl', 'teriyaki angus burger', 'the big carl', 'angus famous', 'angus big carl', 'double guacamole bacon cheeseburger', 'double western bacon cheeseburger', 'the really big carl', 'no meat famous star', 'double big char chile angus', 'el diablito double', 'double breakfast burger combo lunch', 'double famous star', 'spicy western bacon cheeseburger', 'double spicy breakfast burger combo lunch', 'double breakfast burger', 'double spicy western bacon cheeseburger', 'big char chile angus', 'monster angus burger', 'spicy breakfast burger', 'california classic double cheeseburger', 'double angus spicy western bacon', 'breakfast burger combo lunch', 'junior burger', 'jalapeno double cheeseburger combo', 'double guacamole bacon cheeseburger combo', 'double big char chile angus combo', 'sourdough star combo', '#6 double angus big carl combo', 'double angus spicy western bacon combo', '20 piece hand breaded chicken tenders combo', 'big char chile angus combo', 'double spicy western bacon cheeseburger combo', 'double angus el diablo combo', 'angus ghost burger combo', 'ghost burger combo', '#6 angus big carl combo', 'el diablo angus combo', '#14 charbroiled bbq chicken sandwich combo', 'triple western bacon combo', 'no meat famous star combo', '#11 hand breaded bacon swiss chicken sandwich combo', 'el diablo double combo', 'santa fe tender wrap combo', 'big cheeseburger combo', '9 piece chicken stars combo', 'double angus western burger combo', '6 piece chicken stars combo', 'hand breaded jalapeno chicken sandwich combo', '#2 super star with cheese combo', 'barbeque tender wrap combo', 'el diablo combo', '#13 charbroiled santa fe chicken sandwich combo', '15 piece hand breaded chicken tenders combo', 'el diablito combo', 'el diablo tender wrap combo', 'double angus ghost burger combo', 'big char chile burger combo', 'teriyaki double burger combo', '2 for 6 tender wrap combo', '#1 famous star combo', '#10 hand breaded chicken sandwich combo', 'the really big carl combo', 'double ghost burger combo', 'teriyaki double angus burger combo', 'angus spicy western bacon combo', '#8 guacamole angus burger combo', '#8 double guacamole angus burger combo', 'angus famous combo', '#6 single big carl combo', 'angus western bacon cheeseburger combo', 'ranch tender wrap combo', '#3 western bacon cheeseburger combo', 'teriyaki burger combo', '#5 california classic double cheeseburger combo', '#4 double western bacon cheeseburger combo', 'guacamole bacon cheeseburger combo', 'teriyaki angus burger combo', 'no meat el diablo combo', '#12 charbroiled chicken club sandwich combo', '5 piece hand breaded chicken tenders combo', 'double sourdough star combo', '#6 the big carl combo', 'spicy western bacon cheeseburger combo', 'double big char chile burger combo', '10 piece hand breaded chicken tenders combo', 'teriyaki chicken sandwich combo', 'double cheeseburger combo', 'spicy chicken sandwich combo', '3 piece hand breaded chicken tenders combo', 'double angus famous combo', 'monster thickburger combo'}


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


def get_burgers():
    burger_attributes = dict()
    burger_patty_options = {"single", "double", "triple", "angus", "double angus", "spicy", "double spicy", "no meat"}
    burger_combo_size = {"small combo", "medium combo", "large combo", "combo"}
    burger_mods = set()

    valid_burger_names = {
        "guacamole bacon cheeseburger",
        "jalapeno cheeseburger",
        "california classic cheeseburger",
        "western bacon cheeseburger",
        "junior cheeseburger",
        "big cheeseburger",
        # "cheeseburger",
        "thickburger",
        "famous star",
        "super star",
        "sourdough star",
        "big carl",
        "el diablo",
        "burger",  # teriyaki burger
    }

    join_attribute_words = {
        "no meat",
        "with cheese",
        "big char chile",
        "the really",
    }

    for burger_name in burger_names:
        for valid_burger_name in valid_burger_names:
            if is_all_words_exist_in_string(valid_burger_name.split(' '), burger_name):
                possible_attributes = set()

                # Add Burger Attributes
                for join_attribute_word in join_attribute_words:
                    if join_attribute_word in burger_name:
                        possible_attributes.update([join_attribute_word])
                        burger_name = burger_name.replace(join_attribute_word, "")

                possible_attributes.update(set(burger_name.split(' ')) - set(valid_burger_name.split(' ')))
                possible_attributes -= valid_burger_names
                possible_attributes -= burger_patty_options
                possible_attributes -= burger_combo_size
                possible_attributes = set([i for i in possible_attributes if i])
                print("Burger Name: \n", burger_name, '\n', valid_burger_name, '\n', possible_attributes, end='\n\n')
                if valid_burger_name not in burger_attributes:
                    burger_attributes[valid_burger_name] = set()
                burger_attributes[valid_burger_name].update(possible_attributes)

    burger_attributes_string = str()
    for key, value in burger_attributes.items():
        burger_attributes_string += f"\n{key}: {list(value)}"
    print(burger_attributes_string)


    # for cat_id in burger_cat_ids:
    #     item_ids = self.menu_dict.prp_id_to_category.get(cat_id, {}).get(
    #         "menuItems", []
    #     )
    #
    #     for item_id in item_ids:
    #         full_item_name = self.get_name(
    #             self.menu_dict.prp_id_to_menu_item, item_id
    #         )
    #         item_name = self.sanitize_abbreviated_words(full_item_name)
    #         ai_friendly_name = self.ai_friendly_item_names.get(item_name, item_name)
    #         burger_names.add(
    #             f"{item_name}|{ai_friendly_name}"
    #             if ai_friendly_name != item_name
    #             else ai_friendly_name
    #         )
    #
    #     # Burger Mods
    #     for item_id in item_ids:
    #         mod_groups = self.get_entity_to_child_map(item_id)
    #         if len(mod_groups) == 0:
    #             logger.info(
    #                 f"No mod-groups found for Burger item id: {item_id}"
    #             )
    #             continue
    #
    #         if len(mod_groups) > 0:
    #             for mod_group in mod_groups:
    #                 option_items = self.get_child_items(
    #                     self.menu_dict.prp_id_to_mod_group, mod_group
    #                 )
    #                 burger_mods.update(option_items)
    print("\nPRVA_5498 burger_mods: ", burger_mods, end="\n")
    # return list(burger_names), list(burger_attributes), list(burger_patty_options), list(burger_combo_size), list(
    #     burger_mods), burger_cat_ids


if __name__ == "__main__":
    get_burgers()


"""
Drink: Medium Cherry Coke
Drink: Medium Minute Maid Light Lemonade
Drink: Dasani Water Bottle
Drink: Small Doctor Pepper
Drink: Medium Decaf Coffee
Drink: Kids Diet Coke
Drink: Large Cherry Coke
Drink: Small FUZE Raspberry Iced Tea
Drink: Salted Caramel Pretzel Shake
Drink: Kids Diet Doctor Pepper
Drink: Kids FUZE Raspberry Iced Tea
Drink: Hand Crafted Lemonade
Drink: Large Barq's Root Beer
Drink: Large Gold Peak Iced Tea
Drink: Kids Water
Drink: Small Gold Peak Iced Tea Combo
Drink: Small Gold Peak Iced Tea
Drink: Medium Gold Peak Iced Tea Combo
Drink: Medium Gold Peak Iced Tea
Drink: Large Gold Peak Iced Tea Combo
Drink: Kids Gold Peak Iced Tea Combo
Drink: Kids Gold Peak Iced Tea
Drink: Vanilla Shake Combo
Drink: Vanilla Shake
Drink: Chocolate Shake Combo
Drink: Chocolate Shake
Drink: Strawberry Shake Combo
Drink: Oreo Shake Combo
Drink: Oreo Shake
Drink: Small Fanta Strawberry
Drink: Large Fanta Strawberry Combo
Drink: Small Minute Maid Light Lemonade Combo
Drink: Small Minute Maid Light Lemonade
Drink: Strawberry Shake
Drink: Small Fanta Strawberry Combo
Drink: Large Fanta Strawberry
Drink: Medium Minute Maid Light Lemonade Combo
Drink: Large Minute Maid Light Lemonade Combo
Drink: Large Minute Maid Light Lemonade
Drink: Kids Minute Maid Light Lemonade Combo
Drink: Kids Minute Maid Light Lemonade
Drink: Dasani Water Bottle Combo
Drink: Kids Coke Combo
Drink: Large FUZE Raspberry Iced Tea Combo
Drink: Small Water Combo
Drink: Medium Coke Combo
Drink: Small Coffee Combo
Drink: Small Cherry Coke Combo
Drink: Kids Fanta Orange Combo
Drink: Medium Diet Doctor Pepper Combo
Drink: Large Doctor Pepper Combo
Drink: Kids Diet Coke Combo
Drink: Large Coffee Combo
Drink: Medium Water Combo
Drink: Medium Diet Coke Combo
Drink: Kids Fanta Strawberry Combo
Drink: Kids FUZE Raspberry Iced Tea Combo
Drink: Large Decaf Coffee Combo
Drink: Medium Fanta Strawberry Combo
Drink: Small Diet Doctor Pepper Combo
Drink: Small Coke Combo
Drink: Small Sprite Combo
Drink: Large Barq's Root Beer Combo
Drink: Downgrade Large Drink
Drink: Large Diet Doctor Pepper Combo
Drink: Medium Cherry Coke Combo
Drink: Large Hi-C Flashin Fruit Punch Combo
Drink: Kids Barq's Root Beer Combo
Drink: Small Barq's Root Beer Combo
Drink: Small Fanta Orange Combo
Drink: Medium Sprite Combo
Drink: Medium Fanta Orange Combo
Drink: Large Coke Combo
Drink: Large Cherry Coke Combo
Drink: Hand Crafted Strawberry Lemonade combo
Drink: Medium Doctor Pepper Combo
Drink: Small Coke Zero Combo
Drink: Kids Doctor Pepper Combo
Drink: Medium Barq's Root Beer Combo
Drink: 1 Percent Milk Combo
Drink: Medium Decaf Coffee Combo
Drink: Medium Hi-C Flashin Fruit Punch Combo
Drink: Upgrade Medium Drink
Drink: Chocolate Milk Combo
Drink: Kids Coke Zero Combo
Drink: Large Diet Coke Combo
Drink: Large Powerade Mountain Blast Combo
Drink: Kids Water Combo
Drink: Kids Hi-C Flashin Fruit Punch Combo
Drink: Small Decaf Coffee Combo
Drink: Medium Fanta Strawberry
Drink: Small Powerade Mountain Blast Combo
Drink: Hand Crafted Lemonade combo
Drink: Kids Sprite Combo
Drink: Medium Powerade Mountain Blast Combo
Drink: Large Coke Zero Combo
Drink: Kids Cherry Coke Combo
Drink: Simply Orange Juice combo
Drink: Medium Coffee Combo
Drink: Medium Coke Zero Combo
Drink: Small Diet Coke Combo
Drink: Large Fanta Orange Combo
Drink: Large Water Combo
Drink: Small FUZE Raspberry Iced Tea Combo
Drink: Small Doctor Pepper Combo
Drink: Large Sprite Combo
Drink: Upgrade Small Drink
Drink: Kids Diet Doctor Pepper Combo
Drink: Medium Fuze Raspberry Iced Tea Combo
Drink: Kids Powerade Mountain Blast Combo
Drink: Small Hi-C Flashin Fruit Punch Combo
Drink: Small Water
Drink: Kids Coke Zero
Drink: Kids Barq's Root Beer
Drink: Large Water
Drink: Large Sprite
Drink: Large Powerade Mountain Blast
Drink: Medium Coke
Drink: Medium Doctor Pepper
Drink: Medium FUZE Raspberry Iced Tea
Drink: Small Hi-C Flashin Fruit Punch
Drink: Small Sprite
Drink: Medium Water
Drink: Large Decaf Coffee
Drink: Medium Diet Coke
Drink: Medium Diet Doctor Pepper
Drink: Small Coke
Drink: Small Barq's Root Beer
Drink: Small Decaf Coffee
Drink: Medium Sprite
Drink: Medium Hi-C Flashin Fruit Punch
Drink: Medium Coke Zero
Drink: Medium Fanta Orange
Drink: Medium Powerade Mountain Blast
Drink: Kid Drink
Drink: Chocolate Milk
Drink: Large Drink
Drink: Medium Coffee
Drink: Small Cherry Coke
Drink: Small Diet Doctor Pepper
Drink: Salted Caramel Pretzel Shake Combo
Drink: Kid Coke
Drink: Kids Doctor Pepper
Drink: Kids Fanta Strawberry
Drink: Simply Orange Juice
Drink: Large Diet Coke
Drink: Large Diet Doctor Pepper
Drink: Large Hi-C Flashin Fruit Punch
Drink: Small Coffee
Drink: Small Coke Zero
Drink: Small Fanta Orange
Drink: Large Coffee
Drink: 1 Percent Milk
Drink: Medium Drink
Drink: Large Coke Zero
Drink: Large Fanta Orange
Drink: Hand Crafted Strawberry Lemonade
Drink: Kids Sprite
Drink: Kids Powerade Mountain Blast
Drink: Large Coke
Drink: Large Doctor Pepper
Drink: Medium Barq's Root Beer
Drink: Small Diet Coke
Drink: Kids Cherry Coke
Drink: Kids Hi-C Flashin Fruit Punch
Drink: Kids Fanta Orange
Drink: Large FUZE Raspberry Iced Tea
Drink: Small Drink
Drink: Small Powerade Mountain Blast
Drink: Value Coke
Drink: Value Diet Coke
Drink: Value Doctor Pepper
Drink: Value Diet Doctor Pepper
Drink: Value Cherry Coke
Drink: Value Orange Soda
Drink: Value Lemonade
Drink: Value Powerade
Drink: Value Coke Zero
Drink: Value Sprite
Drink: Value Water
Drink: Value Root Beer
Drink: Value Ice Tea
Drink: Value Raspberry tea
Drink: Value Fanta Strawberry
Drink: Value Fruit Punch
Drink: Value Drink
Drink: Value Orange Soda
Drink: Value Lemonade
Drink: Value Powerade
Drink: Value Coke Zero
Drink: Value Sprite
Drink: Value Root Beer
Drink: Value Ice Tea
Drink: Value Raspberry tea
Drink: Value Fanta Strawberry
Drink: Value Fruit Punch
Drink: Value Doctor Pepper
Drink: Value Diet Doctor Pepper
Drink: Value Cherry Coke
Drink: Value Diet Coke
Drink: Value Coke


Core Item: Ranch Tender Wrap
Core Item: Ranch Tender Wrap 1
Core Item: Ranch Tender Wrap 2
Core Item: Barbeque Tender Wrap
Core Item: Barbeque Tender Wrap 1
Core Item: Barbeque Tender Wrap 2
Core Item: Santa fe Tender Wrap
Core Item: Santa fe Tender Wrap 1
Core Item: Santa fe Tender Wrap 2
Core Item: 2 for 6 tender wraps
Core Item: Small 2 for 6 tender wrap Combo
Core Item: Medium 2 for 6 tender wrap Combo
Core Item: Large 2 for 6 tender wrap Combo
Core Item: 2 for 6 tender wrap combo
Core Item: Small Ranch Tender Wrap Combo
Core Item: Medium Ranch Tender Wrap Combo
Core Item: Large Ranch Tender Wrap Combo
Core Item: Ranch Tender Wrap Combo
Core Item: Small Barbeque Tender Wrap Combo
Core Item: Medium Barbeque Tender Wrap Combo
Core Item: Large Barbeque Tender Wrap Combo
Core Item: Barbeque Tender Wrap combo
Core Item: Small Santa fe Tender Wrap Combo
Core Item: Medium Santa fe Tender Wrap Combo
Core Item: Large Santa fe Tender Wrap Combo
Core Item: Santa fe Tender Wrap Combo
Core Item: Small Double Sourdough Star Combo
Core Item: Small Famous Star with Cheese Combo
Core Item: Panko-Breaded Fish Sandwich Combo
Core Item: Big Char Chile Burger
Core Item: Egg Biscuit
Core Item: 6 Piece Jalapeno Poppers
Core Item: Medium Double Guacamole Angus Burger Combo
Core Item: All Star Meal 15
Core Item: Double Cheeseburger Combo
Core Item: Small El Diablito Double Combo
Core Item: Big Char Chile Angus Combo
Core Item: Small Hand Breaded Jalapeno Chicken Sandwich Combo
Core Item: Medium Spicy Chicken Sandwich Combo
Core Item: Small Charbroiled BBQ Chicken Sandwich Combo
Core Item: Small Big Hamburger Combo
Core Item: Medium Spicy Western Bacon Cheeseburger Combo
Core Item: Small Jalapeno Double Cheeseburger Combo
Core Item: El Diablito Combo
Core Item: Medium Double Big Char Chile Burger Combo
Core Item: Junior CheeseBurger
Core Item: Junior Burger
Core Item: Small Breakfast Burger Combo
Core Item: Medium Breakfast Burger Combo
Core Item: Medium Double Breakfast Burger Combo lunch
Core Item: Small Breakfast Burger Combo lunch
Core Item: Medium Double Western Bacon Cheeseburger Combo
Core Item: Small California Classic Double Cheeseburger Combo
Core Item: Medium 2 for 6 Crispy Fish Sandwich Combo
Core Item: Double Big Char Chile Burger
Core Item: The Breakfast Burger
Core Item: Large Breakfast Burger Combo lunch
Core Item: Large Breakfast Burger Combo
Core Item: Large Double Breakfast Burger Combo lunch
Core Item: Large Double Breakfast Burger Combo
Core Item: Double Breakfast Burger
Core Item: Small Double Breakfast Burger Combo
Core Item: Medium Double Breakfast Burger Combo
Core Item: Small Double Breakfast Burger Combo lunch
Core Item: Large Chocolate Chip Cookie
Core Item: Double Big Char Chile Angus Combo
Core Item: Big Char Chile Burger Combo
Core Item: #4 Double Western Bacon Cheeseburger Combo
Core Item: Double Western Bacon Cheeseburger
Core Item: Bacon Grilled Cheese Breakfast Sandwich
Core Item: Small Bacon Grilled Cheese Breakfast Sandwich Combo
Core Item: Large Bacon Grilled Cheese Breakfast Sandwich Combo
Core Item: Medium 5 Piece Hand Breaded Chicken Tenders Combo
Core Item: Large Loaded Breakfast Burrito Combo
Core Item: Large Big Hamburger Combo
Core Item: Large Super Star with Cheese Combo
Core Item: Medium Breakfast Burger Combo lunch
Core Item: Double Big Char Chile Burger Combo
Core Item: Medium Bacon Grilled Cheese Breakfast Sandwich Combo
Core Item: Medium 3 Piece Hand Breaded Chicken Tenders Combo
Core Item: Large 3 Piece Hand Breaded Chicken Tenders Combo
Core Item: Large 5 Piece Hand Breaded Chicken Tenders Combo
Core Item: Medium Jalapeno Burger Combo
Core Item: Large Jalapeno Burger Combo
Core Item: Jalapeno Burger Combo
Core Item: Medium 10 Piece Hand Breaded Chicken Tenders
Core Item: Large Bacon Egg and Cheese Burrito Combo
Core Item: Small Jalapeno Burger Combo
Core Item: large 10 Piece Hand Breaded Chicken Tenders
Core Item: 9 Piece Chicken Stars Kids Meal
Core Item: Loaded Breakfast Burrito
Core Item: Charbroiled Santa Fe Chicken Sandwich
Core Item: #13 Charbroiled Santa Fe Chicken Sandwich Combo
Core Item: Charbroiled BBQ Chicken Sandwich
Core Item: #14 Charbroiled BBQ Chicken Sandwich Combo
Core Item: Bacon Egg and Cheese Biscuit 1
Core Item: Bacon Egg and Cheese Biscuit 2
Core Item: Medium All Star Meal #15 Combo
Core Item: All Star Meal #15
Core Item: Large All Star Meal #15 Combo
Core Item: Medium All Star Meal #16 combo
Core Item: Large All Star Meal #16 combo
Core Item: Small All Star Meal #16 combo
Core Item: 10 Piece Hand Breaded Chicken Tenders Combo
Core Item: 5 Piece Hand Breaded Chicken Tenders Combo
Core Item: 3 Piece Hand Breaded Chicken Tenders Combo
Core Item: Medium Hand Breaded Jalapeno Chicken Sandwich Combo
Core Item: Hand Breaded Jalapeno Chicken Sandwich Combo
Core Item: Spicy Chicken Sandwich Combo
Core Item: Large Spicy Chicken Sandwich Combo
Core Item: Medium 6 Piece - Chicken Stars Combo
Core Item: Large 6 Piece - Chicken Stars Combo
Core Item: Medium 9 Piece - Chicken Stars Combo
Core Item: Double Jalapeno Angus Burger Combo
Core Item: Large 9 Piece - Chicken Stars Combo
Core Item: 9 Piece Chicken Stars Combo
Core Item: Double Guacamole Angus Burger Combo
Core Item: 6 Piece Chicken Stars Combo
Core Item: Double Original Angus Burger Combo
Core Item: The Really Big Carl Combo
Core Item: Medium 2 for 5 Breakfast Mix and Match Combo
Core Item: Small 2 for 5 Breakfast Mix and Match Combo
Core Item: 2 for 5 Breakfast Mix and Match Combo
Core Item: Large 2 for 5 Breakfast Mix and Match Combo
Core Item: 2 for 5 Breakfast Mix and Match
Core Item: Bacon Egg and Cheese Burrito 2
Core Item: Sourdough Star
Core Item: Guacamole Angus Burger
Core Item: Double Guacamole Bacon Cheeseburger
Core Item: Jalapeno Double Cheeseburger
Core Item: Cheeseburger Kids Meal
Core Item: Sausage Egg and Cheese Biscuit 2
Core Item: Large Guacamole Bacon Cheeseburger Combo
Core Item: Bacon Egg and Cheese Burrito Combo
Core Item: The Really Big Carl
Core Item: El Diablo Angus
Core Item: Double Sourdough Star
Core Item: Extra Poppers
Core Item: El Diablo Double
Core Item: Double Cheeseburger
Core Item: Sausage Grilled Cheese Breakfast Sandwich 1
Core Item: Large Egg Biscuit Combo
Core Item: Large Double Guacamole Bacon Cheeseburger Combo
Core Item: Large Famous Star with Cheese Combo
Core Item: 3 Piece Hand Breaded Chicken Tenders
Core Item: Large Jalapeno Double Cheeseburger Combo
Core Item: Double Cheeseburger ASM
Core Item: Large Sausage Grilled Cheese Sandwich Combo
Core Item: Large Hand Breaded Chicken Sandwich Combo
Core Item: Large Double Big Char Chile Burger Combo
Core Item: Sausage Grilled Cheese Sandwich Combo
Core Item: Jalapeno Angus Burger
Core Item: Big Cheeseburger
Core Item: 2 piece Chicken Tender Kids Meal
Core Item: Sausage Egg and Cheese Biscuit 1
Core Item: Large Double Cheeseburger Combo
Core Item: 1 Piece Chicken Star
Core Item: Small Bacon Egg and Cheese Burrito Combo
Core Item: Medium Bacon Biscuit Combo
Core Item: Guacamole Bacon Cheeseburger
Core Item: Bacon Grilled Cheese Breakfast Sandwich 2
Core Item: Large Sausage Egg and Cheese Biscuit Combo
Core Item: Large Western Bacon Cheeseburger Combo
Core Item: Large Double Jalapeno Angus Burger Combo
Core Item: Large El Diablo Double Combo
Core Item: 10 Piece Hand Breaded Chicken Tenders
Core Item: Sausage Egg and Cheese Biscuit Combo
Core Item: Famous Star with Cheese
Core Item: California Classic Double Cheeseburger
Core Item: Large El Diablito Double Combo
Core Item: Large California Classic Double Cheeseburger Combo
Core Item: Medium Sausage Breakfast Burrito Combo
Core Item: Small Sausage Grilled Cheese Sandwich Combo
Core Item: Large Bacon Biscuit Combo
Core Item: Large Hand Breaded Chicken Biscuit Combo
Core Item: Large Big Cheeseburger Combo
Core Item: Spicy Chicken Sandwich 2
Core Item: 6 Piece - Chicken Stars
Core Item: 20 Piece Hand Breaded Chicken Tenders
Core Item: Small Sausage Egg and Cheese Biscuit Combo
Core Item: Double Guacamole Angus Burger
Core Item: 6 Piece Chicken Stars Kids Meal
Core Item: 6 Piece Jalapeno Poppers Combo
Core Item: 9 Piece Jalapeno Poppers Combo
Core Item: Large Bacon Egg and Cheese Biscuit Combo
Core Item: Large Sourdough Star Combo
Core Item: Large Angus Western Bacon Cheeseburger Combo
Core Item: Large Charbroiled Chicken Club Sandwich Combo
Core Item: Large Crispy Fish Sandwich Combo
Core Item: Large Double Big Char Chile Angus Combo
Core Item: Medium Steak and Egg Burrito Combo
Core Item: Small Biscuit Combo
Core Item: Double Spicy Western Bacon Cheeseburger
Core Item: Hamburger Kids Meal
Core Item: Bacon Egg and Cheese Burrito 1
Core Item: Large Charbroiled Santa Fe Chicken Sandwich Combo
Core Item: Large The Really Big Carl Combo
Core Item: 5 Piece Hand Breaded Chicken Tenders
Core Item: Spicy Western Bacon Cheeseburger
Core Item: The Big Carl
Core Item: Large Sausage Breakfast Burrito Combo
Core Item: Large Spicy Western Bacon Cheeseburger Combo
Core Item: Large Charbroiled BBQ Chicken Sandwich Combo
Core Item: Large Big Char Chile Burger Combo
Core Item: Hand Breaded Chicken Sandwich
Core Item: Medium Bacon Egg and Cheese Burrito Combo
Core Item: Small Sausage Breakfast Burrito Combo
Core Item: Small Bacon Biscuit Combo
Core Item: Medium Bacon Egg and Cheese Biscuit Combo
Core Item: Medium Loaded Breakfast Burrito Combo
Core Item: Small Monster Biscuit Combo
Core Item: Double Original Angus Burger
Core Item: El Diablito Double
Core Item: Bacon Grilled Cheese Breakfast Sandwich1
Core Item: Large Original Angus Burger Combo
Core Item: Large Monster Biscuit Combo
Core Item: Large Steak and Egg Burrito Combo
Core Item: Large Double Original Angus Burger Combo
Core Item: Spicy Chicken Sandwich
Core Item: Medium Egg Biscuit Combo
Core Item: Sausage Breakfast Burrito Combo
Core Item: Angus Western Bacon Cheeseburger
Core Item: Large 2 for 6 Crispy Fish Sandwich Combo
Core Item: Large Hand Breaded Bacon Swiss Chicken Sandwich Combo
Core Item: 15 Piece Hand Breaded Chicken Tenders
Core Item: Hand Breaded Bacon Swiss Chicken Sandwich
Core Item: Egg Biscuit Combo
Core Item: Light Poppers
Core Item: 4 Piece Chicken Stars Kids Meal
Core Item: Large Jalapeno Angus Burger Combo
Core Item: Large El Diablo Combo
Core Item: Spicy Chicken Sandwich ASM
Core Item: Large Big Char Chile Angus Combo
Core Item: Charbroiled Chicken Club Sandwich
Core Item: Small Egg Biscuit Combo
Core Item: Double Breakfast Burger Combo
Core Item: Steak and Egg Burrito Combo
Core Item: Bacon Egg and Cheese Biscuit Combo
Core Item: Loaded Breakfast Burrito Combo
Core Item: Jalapeno Burger
Core Item: Large Big Carl Combo
Core Item: Large Biscuit Combo
Core Item: Crispy Fish Sandwich 2
Core Item: Medium Sausage Egg and Cheese Biscuit Combo
Core Item: Small Steak and Egg Burrito Combo
Core Item: Small Loaded Breakfast Burrito Combo
Core Item: Big Hamburger
Core Item: Original Angus Burger
Core Item: Western Bacon Cheeseburger
Core Item: Sausage Grilled Cheese Breakfast Sandwich 2
Core Item: Large Double Guacamole Angus Burger Combo
Core Item: Hand Breaded Jalapeno Chicken Sandwich
Core Item: Double Jalapeno Angus Burger
Core Item: El Diablo
Core Item: Bacon Biscuit Combo
Core Item: Large Double Sourdough Star Combo
Core Item: Large Double Western Bacon Cheeseburger Combo
Core Item: Crispy Fish Sandwich 1
Core Item: Spicy Chicken Sandwich 1
Core Item: Medium Sausage Grilled Cheese Sandwich Combo
Core Item: Small Bacon Egg and Cheese Biscuit Combo
Core Item: No Poppers
Core Item: Large Double Spicy Western Bacon Cheeseburger Combo
Core Item: Large El Diablo Angus Combo
Core Item: Large Hand Breaded Jalapeno Chicken Sandwich Combo
Core Item: 9 Piece - Chicken Stars
Core Item: 1 Piece Hand Breaded Chicken Tender
Core Item: Breakfast Burger Combo
Core Item: Monster Biscuit Combo
Core Item: Medium Monster Biscuit Combo
Core Item: Small Hand Breaded Chicken Biscuit Combo
Core Item: Medium Hand Breaded Chicken Biscuit Combo
Core Item: Large Guacamole Angus Burger Combo
Core Item: 3 Piece Tenders
Core Item: Biscuit Combo
Core Item: Medium Biscuit Combo
Core Item: Hand Breaded Chicken Biscuit Combo
Core Item: Bacon Grilled Cheese Sandwich Combo
Core Item: 2 Chocolate Chip Cookie
Core Item: 1 Chocolate Chip Cookie
Core Item: Medium Charbroiled Chicken Club Sandwich Combo
Core Item: 15 Piece Hand Breaded Chicken Tenders Combo
Core Item: Small Spicy Chicken Sandwich Combo
Core Item: Small 6 Piece - Chicken Stars Combo
Core Item: #8 Guacamole Angus Burger Combo
Core Item: Small Double Western Bacon Cheeseburger Combo
Core Item: Small Double Guacamole Angus Burger Combo
Core Item: Medium Angus Western Bacon Cheeseburger Combo
Core Item: Medium Double Spicy Western Bacon Cheeseburger Combo
Core Item: Small Spicy Western Bacon Cheeseburger Combo
Core Item: Medium Super Star with Cheese Combo
Core Item: Double Guacamole Bacon Cheeseburger Combo
Core Item: Big Cheeseburger Combo
Core Item: Medium Crispy Fish Sandwich Combo
Core Item: 2 for 6 Panko-Breaded Fish Sandwich Combo
Core Item: Double Big Char Chile Angus
Core Item: Small Double Big Char Chile Burger Combo
Core Item: Medium Double Big Char Chile Angus Combo
Core Item: #12 Charbroiled Chicken Club Sandwich Combo
Core Item: 9 Piece Jalapeno Poppers
Core Item: Angus Western Bacon Cheeseburger Combo
Core Item: Double Spicy Western Bacon Cheeseburger Combo
Core Item: #2 Super Star with Cheese Combo
Core Item: Medium El Diablito Double Combo
Core Item: Small Jalapeno Angus Burger Combo
Core Item: Add Poppers
Core Item: Bacon Egg and Cheese Biscuit
Core Item: Monster Biscuit
Core Item: Biscuit
Core Item: Medium Hand Breaded Chicken Sandwich Combo
Core Item: Breakfast Burger Combo lunch
Core Item: Medium Western Bacon Cheeseburger Combo
Core Item: Small Sourdough Star Combo
Core Item: Big Hamburger Combo
Core Item: #5 California Classic Double Cheeseburger Combo
Core Item: Jalapeno Double Cheeseburger Combo
Core Item: Medium Guacamole Bacon Cheeseburger Combo
Core Item: Small El Diablo Double Combo
Core Item: Small Crispy Fish Sandwich Combo
Core Item: Sausage Egg and Cheese Biscuit
Core Item: Sausage Breakfast Burrito
Core Item: Hand Breaded Chicken Biscuit
Core Item: Small 20 Piece Hand Breaded Chicken Tenders Combo
Core Item: Small Hand Breaded Chicken Sandwich Combo
Core Item: Double Breakfast Burger Combo lunch
Core Item: Small Western Bacon Cheeseburger Combo
Core Item: Spicy Western Bacon Cheeseburger Combo
Core Item: Medium Jalapeno Angus Burger Combo
Core Item: Small Guacamole Bacon Cheeseburger Combo
Core Item: Crispy Fish Sandwich
Core Item: Bacon Egg and Cheese Burrito
Core Item: 6 Biscuits
Core Item: Sausage Grilled Cheese Breakfast Sandwich
Core Item: Steak and Egg Burrito
Core Item: Medium Hand Breaded Bacon Swiss Chicken Sandwich Combo
Core Item: Small Charbroiled Chicken Club Sandwich Combo
Core Item: Sourdough Star Combo
Core Item: Small Angus Western Bacon Cheeseburger Combo
Core Item: Medium Double Cheeseburger Combo
Core Item: Medium El Diablo Combo
Core Item: El Diablo Double Combo
Core Item: Medium El Diablo Angus Combo
Core Item: Medium The Really Big Carl Combo
Core Item: Small Double Spicy Western Bacon Cheeseburger Combo
Core Item: Small Super Star with Cheese Combo
Core Item: Big Char Chile Angus
Core Item: Medium Big Char Chile Burger Combo
Core Item: Small Double Big Char Chile Angus Combo
Core Item: Small 9 Piece - Chicken Stars Combo
Core Item: Small 15 Piece Hand Breaded Chicken Tenders Combo
Core Item: #6 The Big Carl Combo
Core Item: Medium Sourdough Star Combo
Core Item: Small Guacamole Angus Burger Combo
Core Item: #7 Original Angus Burger Combo
Core Item: Double Sourdough Star Combo
Core Item: #1 Famous Star Combo
Core Item: Medium Double Guacamole Bacon Cheeseburger Combo
Core Item: Small Big Cheeseburger Combo
Core Item: Medium El Diablo Double Combo
Core Item: Small 2 for 6 Crispy Fish Sandwich Combo
Core Item: 2 for 6 Crispy Fish Sandwich
Core Item: Small El Diablo Angus Combo
Core Item: Medium Original Angus Burger Combo
Core Item: Medium Double Original Angus Burger Combo
Core Item: Medium Famous Star with Cheese Combo
Core Item: Medium Double Jalapeno Angus Burger Combo
Core Item: Small Big Char Chile Burger Combo
Core Item: Medium Big Char Chile Angus Combo
Core Item: Small Charbroiled Santa Fe Chicken Sandwich Combo
Core Item: Medium Charbroiled BBQ Chicken Sandwich Combo
Core Item: Small 3 Piece Hand Breaded Chicken Tenders Combo
Core Item: Small Original Angus Burger Combo
Core Item: Medium California Classic Double Cheeseburger Combo
Core Item: Small Double Original Angus Burger Combo
Core Item: Small Double Jalapeno Angus Burger Combo
Core Item: Small Double Guacamole Bacon Cheeseburger Combo
Core Item: #9 Jalapeno Angus Burger Combo
Core Item: Small Big Char Chile Angus Combo
Core Item: #11 Hand Breaded Bacon Swiss Chicken Sandwich Combo
Core Item: 20 Piece Hand Breaded Chicken Tenders Combo
Core Item: #3 Western Bacon Cheeseburger Combo
Core Item: Medium Guacamole Angus Burger Combo
Core Item: El Diablo Angus Combo
Core Item: El Diablo Combo
Core Item: Medium Big Cheeseburger Combo
Core Item: 6 piece poppers
Core Item: 12 Biscuits
Core Item: Small Hand Breaded Bacon Swiss Chicken Sandwich Combo
Core Item: #10 Hand Breaded Chicken Sandwich Combo
Core Item: Medium Big Carl Combo
Core Item: Small The Really Big Carl Combo
Core Item: Medium Double Sourdough Star Combo
Core Item: Small Double Cheeseburger Combo
Core Item: Small El Diablo Combo
Core Item: Guacamole Bacon Cheeseburger Combo
Core Item: Bacon Biscuit
Core Item: Small 5 Piece Hand Breaded Chicken Tenders Combo
Core Item: Medium Charbroiled Santa Fe Chicken Sandwich Combo
Core Item: Small 10 Piece Hand Breaded Chicken Tenders
Core Item: All Star Meal 16
Core Item: Small Big Carl Combo
Core Item: Medium Big Hamburger Combo
Core Item: Medium Jalapeno Double Cheeseburger Combo
Core Item: Angus Spicy Western Bacon
Core Item: Double Angus Spicy Western Bacon
Core Item: Spicy Breakfast Burger
Core Item: Double Spicy Breakfast Burger
Core Item: Triple Spicy Western Bacon Cheeseburger
Core Item: Small Spicy Breakfast Burger Combo
Core Item: Medium Spicy Breakfast Burger Combo
Core Item: Large Spicy Breakfast Burger Combo
Core Item: Small Spicy Breakfast Burger Combo lunch
Core Item: Medium Spicy Breakfast Burger Combo Lunch
Core Item: Large Spicy Breakfast Burger Combo lunch
Core Item: Spicy Breakfast burger Combo
Core Item: Spicy Breakfast burger Combo Lunch
Core Item: Small Double Spicy Breakfast Burger Combo
Core Item: Medium Double Spicy Breakfast Burger Combo
Core Item: Large Double Spicy Breakfast Burger Combo
Core Item: Small Double Spicy Breakfast Burger Combo lunch
Core Item: Medium Double Spicy Breakfast Burger Combo lunch
Core Item: Large Double Spicy Breakfast Burger Combo lunch
Core Item: Double Spicy Breakfast Burger Combo
Core Item: Double Spicy Breakfast Burger Combo Lunch
Core Item: Small Triple Spicy Western Bacon Cheeseburger Combo
Core Item: Medium Triple Spicy Western Bacon Cheeseburger Combo
Core Item: Large Triple Spicy Western Bacon Cheeseburger Combo
Core Item: Triple Western Bacon Combo
Core Item: Small Angus Spicy Western Bacon Combo
Core Item: medium Angus Spicy Western Bacon Combo
Core Item: Large Angus Spicy Western Bacon Combo
Core Item: Small Double Angus Spicy Western Bacon combo
Core Item: Medium Double Angus Spicy Western Bacon combo
Core Item: Large Double Angus Spicy Western Bacon combo
Core Item: Angus Spicy Western Bacon Combo
Core Item: Double Angus Spicy Western Bacon Combo
Core Item: Angus Famous
Core Item: Small Angus Famous Combo
Core Item: Medium Angus Famous Combo
Core Item: Large Angus Famous Combo
Core Item: Double Famous Star
Core Item: Double Angus Famous Star
Core Item: Small Double Angus Famous Star Combo
Core Item: Medium Double Angus Famous Star Combo
Core Item: Large Double Angus Famous Star Combo
Core Item: No Meat Famous Star
Core Item: Small No Meat Famous Star Combo
Core Item: Medium No Meat Famous Star Combo
Core Item: Large No Meat Famous Star Combo
Core Item: Single Big Carl
Core Item: Small Single Big Carl Combo
Core Item: Medium Single Big Carl Combo
Core Item: Large Single Big Carl Combo
Core Item: Angus Big Carl
Core Item: Small Angus Big Carl Combo
Core Item: Medium Angus Big Carl Combo
Core Item: Large Angus Big Carl Combo
Core Item: Double Angus Big Carl
Core Item: Small Double Angus Big Carl Combo
Core Item: Medium Double Angus Big Carl Combo
Core Item: Large Double Angus Big Carl Combo
Core Item: Double Angus Western Bacon Cheeseburger
Core Item: Small Double Angus Western Bacon Cheeseburger Combo
Core Item: Medium Double Angus Western Bacon Cheeseburger Combo
Core Item: Large Double Angus Western Bacon Cheeseburger Combo
Core Item: Double angus el diablo
Core Item: Small Double angus el diablo Combo
Core Item: Medium Double angus el diablo Combo
Core Item: Large Double angus el diablo Combo
Core Item: No Meat El Diablo
Core Item: Small No Meat El Diablo Combo
Core Item: medium No Meat El Diablo Combo
Core Item: Large No Meat El Diablo Combo
Core Item: El Diablo Tender wrap
Core Item: El Diablo Tender wrap 1
Core Item: El Diablo Tender wrap 2
Core Item: Small El Diablo Tender wrap Combo
Core Item: Medium El Diablo Tender wrap Combo
Core Item: Large El Diablo Tender wrap Combo
Core Item: El Diablo Tender Wrap Combo
Core Item: Double Angus El Diablo Combo
Core Item: No Meat El Diablo Combo
Core Item: Angus Famous Combo
Core Item: Double Angus Famous Combo
Core Item: No Meat Famous Star Combo
Core Item: Single Big Carl Combo
Core Item: Angus Big Carl Combo
Core Item: Double Angus Big Carl Combo
Core Item: Double Angus Western Burger Combo
Core Item: Monster ThickBurger Combo
Core Item: Large Monster ThickBurger Combo
Core Item: Medium Monster ThickBurger Combo
Core Item: Small Monster ThickBurger Combo
Core Item: Monster Angus Burger
Core Item: 6 Piece - Spicy Chicken Stars
Core Item: Small 6 Piece - Spicy Chicken Stars Combo
Core Item: Medium 6 Piece - Spicy Chicken Stars Combo
Core Item: Large 6 Piece - Spicy Chicken Stars Combo
Core Item: 6 Piece - Spicy Chicken Stars Combo
Core Item: Bacon Cheese Junior
Core Item: Small Bacon Cheese Junior Combo
Core Item: Medium Bacon Cheese Junior Combo
Core Item: Large Bacon Cheese Junior Combo
Core Item: Bacon Cheese Junior Combo
Core Item: Bacon Double Cheese Junior
Core Item: Small Bacon Double Cheese Junior Combo
Core Item: Medium Bacon Double Cheese Junior Combo
Core Item: Large Bacon Double Cheese Junior Combo
Core Item: Bacon Double Cheese Junior Combo
Core Item: Cali Junior
Core Item: Small Cali Junior Combo
Core Item: Medium Cali Junior Combo
Core Item: Large Cali Junior Combo
Core Item: Cali Junior Combo
Core Item: Jalapeno junior
Core Item: Small Jalapeno junior Combo
Core Item: Medium Jalapeno junior Combo
Core Item: Large Jalapeno junior Combo
Core Item: Jalapeno junior Combo
Core Item: Guacamole Junior
Core Item: Small Guacamole Junior Combo
Core Item: Medium Guacamole Junior Combo
Core Item: Large Guacamole Junior Combo
Core Item: Guacamole Junior Combo
Core Item: Double Guacamole Junior
Core Item: Small Double Guacamole Junior Combo
Core Item: Medium Double Guacamole Junior Combo
Core Item: Large Double Guacamole Junior Combo
Core Item: Double Guacamole Junior Combo
Core Item: Teriyaki burger
Core Item: Teriyaki Double Burger
Core Item: Teriyaki Double Burger Combo
Core Item: Small Teriyaki Double Burger Combo
Core Item: Medium Teriyaki Double Burger Combo
Core Item: Large Teriyaki Double Burger Combo
Core Item: Teriyaki burger Combo
Core Item: Large Teriyaki burger Combo
Core Item: Medium Teriyaki burger Combo
Core Item: Small Teriyaki burger Combo
Core Item: Teriyaki angus burger
Core Item: Teriyaki angus burger Combo
Core Item: Small Teriyaki angus burger Combo
Core Item: Medium Teriyaki angus burger Combo
Core Item: Large Teriyaki angus burger Combo
Core Item: Teriyaki Double angus burger
Core Item: Small Teriyaki Double angus burger Combo
Core Item: Medium Teriyaki Double angus burger Combo
Core Item: Large Teriyaki Double angus burger Combo
Core Item: Teriyaki Double angus burger Combo
Core Item: Teriyaki chicken sandwich
Core Item: Small Teriyaki chicken sandwich combo
Core Item: Medium Teriyaki chicken sandwich combo
Core Item: Large Teriyaki chicken sandwich combo
Core Item: Teriyaki chicken sandwich combo
Core Item: Ghost Breakfast Burger
Core Item: Small Ghost Breakfast Burger combo lunch
Core Item: Medium Ghost Breakfast Burger combo lunch
Core Item: Large Ghost Breakfast Burger combo lunch
Core Item: Ghost Breakfast Burger combo lunch
Core Item: Small Ghost Breakfast Burger combo
Core Item: Medium Ghost Breakfast Burger combo
Core Item: Large Ghost Breakfast Burger combo
Core Item: Ghost Breakfast Burger combo
Core Item: Double Ghost Breakfast Burger
Core Item: Small Double Ghost Breakfast Burger combo lunch
Core Item: Medium Double Ghost Breakfast Burger combo lunch
Core Item: Large Double Ghost Breakfast Burger combo lunch
Core Item: Double Ghost Breakfast Burger combo lunch
Core Item: Double Ghost Breakfast Burger combo
Core Item: Small Double Ghost Breakfast Burger combo
Core Item: Medium Double Ghost Breakfast Burger combo
Core Item: Large Double Ghost Breakfast Burger combo
Core Item: Ghost Burger
Core Item: Small Ghost Burger Combo
Core Item: Medium Ghost Burger Combo
Core Item: Large Ghost Burger Combo
Core Item: Ghost Burger Combo
Core Item: Double Ghost Burger
Core Item: Small double Ghost Burger Combo
Core Item: Medium Double Ghost Burger Combo
Core Item: Large double Ghost Burger Combo
Core Item: Double Ghost Burger Combo
Core Item: Angus Ghost Burger
Core Item: Small Angus Ghost Burger Combo
Core Item: Medium Angus Ghost Burger Combo
Core Item: Large Angus Ghost Burger Combo
Core Item: Angus Ghost Burger Combo
Core Item: Double Angus Ghost Burger
Core Item: Small Double Angus Ghost Burger Combo
Core Item: Medium double Angus Ghost Burger Combo
Core Item: Large Double Angus Ghost Burger Combo
Core Item: Double Angus Ghost Burger Combo


Modifier + Sides: No Jalapenos
Modifier + Sides: No Hash Rounds
Modifier + Sides: no small bun
Modifier + Sides: Ketchup packet
Modifier + Sides: no third pound burger patty
Modifier + Sides: Add Barbeque Sauce
Modifier + Sides: No Tender
Modifier + Sides: Add Tender
Modifier + Sides: Extra Tender
Modifier + Sides: Add Dill Ranch
Modifier + Sides: no Dill Ranch
Modifier + Sides: Extra Dill Ranch
Modifier + Sides: Dill Ranch
Modifier + Sides: Light Dill Ranch
Modifier + Sides: light Shredded Cheese
Modifier + Sides: Sweet and Bold Barbeque Cup
Modifier + Sides: Add Fiery Sauce
Modifier + Sides: Syrup
Modifier + Sides: sourdough
Modifier + Sides: Fried Zucchini Combo
Modifier + Sides: Fried Zucchini
Modifier + Sides: Potato bun
Modifier + Sides: Large bun
Modifier + Sides: Light Ketchup
Modifier + Sides: Light Mustard
Modifier + Sides: Light Onions
Modifier + Sides: light Pickles
Modifier + Sides: Light Mayo
Modifier + Sides: light special sauce
Modifier + Sides: light barbeque sauce
Modifier + Sides: light classic sauce
Modifier + Sides: Waffle Fries Combo
Modifier + Sides: Onion Rings Combo
Modifier + Sides: Onion Rings
Modifier + Sides: Sugar Packet
Modifier + Sides: Splenda packet
Modifier + Sides: Sweet n Low
Modifier + Sides: Creamer
Modifier + Sides: Extra Salsa
Modifier + Sides: Bag Fry side
Modifier + Sides: Bag Fry
Modifier + Sides: Chocolate Cake
Modifier + Sides: Charbroiled Chicken Patty
Modifier + Sides: Hand Breaded Chicken Patty
Modifier + Sides: Angus Patty
Modifier + Sides: Large Patty
Modifier + Sides: Small Patty
Modifier + Sides: Spicy Chicken Patty
Modifier + Sides: side of small patty
Modifier + Sides: side of Large patty
Modifier + Sides: No Mustard
Modifier + Sides: No Pickles
Modifier + Sides: Add Onions
Modifier + Sides: Add Mustard
Modifier + Sides: No Small burger patty
Modifier + Sides: Add Steak Strips
Modifier + Sides: Add Tomato
Modifier + Sides: Add Mayo
Modifier + Sides: Add Pepper Jack Cheese
Modifier + Sides: Add Swiss Cheese
Modifier + Sides: Add Sausage
Modifier + Sides: Add Salsa
Modifier + Sides: Plain
Modifier + Sides: Add Special Sauce
Modifier + Sides: Add Santa Fe Sauce
Modifier + Sides: Add Third Pound Patty
Modifier + Sides: Add Hand Breaded Chicken Filet
Modifier + Sides: Lettuce Wrap
Modifier + Sides: Add Onion Rings
Modifier + Sides: Add Two Slices American Cheese
Modifier + Sides: Add green chili
Modifier + Sides: Extra Bacon
Modifier + Sides: Extra Ketchup
Modifier + Sides: Extra Swiss Cheese
Modifier + Sides: Extra Sausage
Modifier + Sides: Extra Small Patty
Modifier + Sides: No Egg
Modifier + Sides: Extra Fiery Sauce
Modifier + Sides: Extra Whip Cream
Modifier + Sides: No Ketchup
Modifier + Sides: Add Ketchup
Modifier + Sides: Add Pickles
Modifier + Sides: No Small American Cheese
Modifier + Sides: Add Lettuce
Modifier + Sides: Add Guacamole
Modifier + Sides: Add Egg
Modifier + Sides: Add Hash Rounds
Modifier + Sides: Add Shredded Cheese
Modifier + Sides: Add Bacon Bits
Modifier + Sides: Add Classic Sauce
Modifier + Sides: Add One Slice American Cheese
Modifier + Sides: Add Quarter Pound Patty
Modifier + Sides: Add Bacon
Modifier + Sides: Add Jalapenos
Modifier + Sides: Add Grill Onions
Modifier + Sides: Add Small Patty
Modifier + Sides: Add Charred Chile
Modifier + Sides: Extra Jalapenos
Modifier + Sides: Extra Pepper Jack Cheese
Modifier + Sides: Extra Egg
Modifier + Sides: Extra Onion Rings
Modifier + Sides: Extra Grill Chicken Patty
Modifier + Sides: No Bacon
Modifier + Sides: No Ice
Modifier + Sides: no salt
Modifier + Sides: Barbeque Sauce Cup
Modifier + Sides: Small Fries Combo
Modifier + Sides: Extra Powdered Sugar
Modifier + Sides: Extra Lettuce
Modifier + Sides: Extra Grilled Onions
Modifier + Sides: Extra Quarter Pound Patty
Modifier + Sides: No Mayo
Modifier + Sides: Light Ice
Modifier + Sides: Buttermilk Ranch Cup
Modifier + Sides: no spicy chicken patty
Modifier + Sides: Extra Tartar Sauce
Modifier + Sides: Large French Toast Dips Combo lunch
Modifier + Sides: no 1/3 patty
Modifier + Sides: Extra Third Pound Patty
Modifier + Sides: No Onion Rings
Modifier + Sides: Extra Beef Patty
Modifier + Sides: No Tomato
Modifier + Sides: Extra 1/3 Patty
Modifier + Sides: Medium Fries Combo
Modifier + Sides: No Salsa
Modifier + Sides: No Syrup
Modifier + Sides: Extra Guacamole
Modifier + Sides: No Grilled Onions
Modifier + Sides: No Fiery Sauce
Modifier + Sides: Buffalo Sauce Cup
Modifier + Sides: light salt
Modifier + Sides: Light Powdered Sugar
Modifier + Sides: Light Lettuce
Modifier + Sides: Extra Shredded Cheese
Modifier + Sides: Extra Onions
Modifier + Sides: No Large American Cheese
Modifier + Sides: Extra Ice
Modifier + Sides: extra salt
Modifier + Sides: Honey Mustard Cup
Modifier + Sides: No Tartar Sauce
Modifier + Sides: Light tomato
Modifier + Sides: Extra Bacon Bits
Modifier + Sides: Extra Pickles
Modifier + Sides: Extra 1/4 Patty
Modifier + Sides: No Classic Sauce
Modifier + Sides: No Santa Fe Sauce
Modifier + Sides: add lemon
Modifier + Sides: Kids Fries
Modifier + Sides: Add Equal
Modifier + Sides: Medium French Toast Dips Combo
Modifier + Sides: No Sausage
Modifier + Sides: Extra Steak Strips
Modifier + Sides: Extra Hash Rounds
Modifier + Sides: No Guacamole
Modifier + Sides: no Large bun
Modifier + Sides: Medium Hash Rounds Combo
Modifier + Sides: Add Creamer
Modifier + Sides: Extra Barbeque Sauce
Modifier + Sides: No Potato Bun
Modifier + Sides: Extra Third Pound Beef Patty
Modifier + Sides: Add Sweet and Low
Modifier + Sides: No Shredded Cheese
Modifier + Sides: Extra Tomato
Modifier + Sides: Extra Classic Sauce
Modifier + Sides: No Whip Cream
Modifier + Sides: Large Fries Combo
Modifier + Sides: Add Splenda
Modifier + Sides: no green chili
Modifier + Sides: Extra Mustard
Modifier + Sides: Extra American Cheese 2 Slices
Modifier + Sides: no quarter pound burger patty
Modifier + Sides: Extra American Cheese 1 Slice
Modifier + Sides: Extra Charred Chile
Modifier + Sides: No Onions
Modifier + Sides: Light Fiery Sauce
Modifier + Sides: Fiery Sauce Cup
Modifier + Sides: Large French Toast Dips Combo
Modifier + Sides: No Pepper Jack Cheese
Modifier + Sides: Light Whip Cream
Modifier + Sides: Add Small American Cheese
Modifier + Sides: No Butter
Modifier + Sides: light jalapenos
Modifier + Sides: Mustard packet
Modifier + Sides: Strawberry Cheesecake
Modifier + Sides: House Dressing
Modifier + Sides: Large Hash Rounds Combo
Modifier + Sides: Light Santa Fe Sauce
Modifier + Sides: Extra Special Sauce
Modifier + Sides: No Special Sauce
Modifier + Sides: no 1/4 patty
Modifier + Sides: Add Sugar
Modifier + Sides: Add Ice
Modifier + Sides: No Charbroiled chicken patty
Modifier + Sides: French Toast Dips Combo
Modifier + Sides: Extra Mayo
Modifier + Sides: Extra Santa Fe Sauce
Modifier + Sides: No Barbeque Sauce
Modifier + Sides: Kids Fries Combo
Modifier + Sides: No Powdered Sugar
Modifier + Sides: No Charred Chile
Modifier + Sides: Small French Toast Dips Combo
Modifier + Sides: Extra Hand Breaded Chicken Filet
Modifier + Sides: No Lettuce
Modifier + Sides: Extra Large American Cheese
Modifier + Sides: No Sauce
Modifier + Sides: Small Hash Rounds Combo
Modifier + Sides: No Swiss Cheese
Modifier + Sides: No Hand Breaded Chicken Fillet
Modifier + Sides: Small Hash Rounds
Modifier + Sides: Waffle Fries
Modifier + Sides: Stars For Hero's
Modifier + Sides: Medium Hash Rounds
Modifier + Sides: Large Fries
Modifier + Sides: Small fries 1
Modifier + Sides: Large Hash Rounds
Modifier + Sides: French Toast Dips
Modifier + Sides: Onion rings 1
Modifier + Sides: Medium French Toast Dips Combo lunch
Modifier + Sides: French Toast Dips Combo lunch
Modifier + Sides: Small Fries
Modifier + Sides: Small French Toast Dips Combo lunch
Modifier + Sides: no bacon bits
Modifier + Sides: Medium Fries
Modifier + Sides: Side Fish Patty
Modifier + Sides: No fish
Modifier + Sides: add fish
Modifier + Sides: extra fish
Modifier + Sides: Light Tartar sauce
Modifier + Sides: add tartar sauce
Modifier + Sides: side of Tartar sauce
Modifier + Sides: light barbeque
Modifier + Sides: Light Mustard
Modifier + Sides: Light pickles
Modifier + Sides: Potato Bun
Modifier + Sides: Add 1 Tender
Modifier + Sides: light ketchup
Modifier + Sides: Light onions
Modifier + Sides: Light Mayo
Modifier + Sides: light chile strip
Modifier + Sides: Large Bun
Modifier + Sides: extra Tender
Modifier + Sides: Extra chile strip
Modifier + Sides: extra Dill Ranch
Modifier + Sides: No fried zucchini
Modifier + Sides: Add fried zucchini
Modifier + Sides: Light fried zucchini
Modifier + Sides: Extra fried zucchini
Modifier + Sides: El diablo loaded fries
Modifier + Sides: El diablo loaded fries Combo
Modifier + Sides: Add Teriyaki
Modifier + Sides: add pineapple
Modifier + Sides: No Teriyaki
Modifier + Sides: extra pineapple
Modifier + Sides: no pineapple
Modifier + Sides: Extra Teriyaki
Modifier + Sides: Light Teriyaki
Modifier + Sides: Side Pineapple
Modifier + Sides: Cut in half
Modifier + Sides: Light Bacon Bits
Modifier + Sides: Light salsa
Modifier + Sides: Light Guacamole
Modifier + Sides: side of bacon
Modifier + Sides: side of bacon bits
Modifier + Sides: side of salsa
Modifier + Sides: Side of guacamole
Modifier + Sides: Guacamole Bacon Loaded Fries
Modifier + Sides: Guacamole Bacon Loaded Fries combo
Modifier + Sides: Add Ghost Cheese
Modifier + Sides: Extra Ghost Cheese
Modifier + Sides: No Ghost Cheese
Modifier + Sides: add Ghost Sauce
Modifier + Sides: extra Ghost Sauce
Modifier + Sides: light Ghost Sauce
Modifier + Sides: No Ghost Sauce
Modifier + Sides: Ghost sauce on the side
"""