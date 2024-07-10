#!/usr/bin/python3

def test_task_invalid_eligible(is_order_placed, is_order_changed):
    is_task_invalid_eligible = not is_order_placed and not is_order_changed
    return is_task_invalid_eligible


if __name__ == "__main__":
    # inputs = (
    #     {
    #         "is_order_placed": False,
    #         "is_order_changed": False,
    #         "is_task_invalid_eligible": True
    #     },
    #     {
    #         "is_order_placed": False,
    #         "is_order_changed": True,
    #         "is_task_invalid_eligible": False
    #     },
    #     {
    #         "is_order_placed": True,
    #         "is_order_changed": False,
    #         "is_task_invalid_eligible": False
    #     },
    #     {
    #         "is_order_placed": True,
    #         "is_order_changed": True,
    #         "is_task_invalid_eligible": False
    #     }
    #
    # )
    #
    # # for idx, i in enumerate(inputs):
    # #     o = test_task_invalid_eligible(i['is_order_placed'], i['is_order_changed'])
    # #     print(f'{idx}.\nExpected Output - {i["is_task_invalid_eligible"]}\nOriginal Output - {o}', end='\n\n')
    #
    # a_cat_ids = []
    # menu_tree = {'i': [],
    #              'categories': [{
    #                  'name': 'same',
    #                  'id': 12
    #              },
    #                  {
    #                      'name': "breakfast entrees",
    #                      'id': 100
    #                  }]}
    # # if "categories" in menu_tree:
    # try:
    #     for category in menu_tree["categories"]:
    #         if category["name"].lower() == "breakfast entrees":
    #             a_cat_ids.append(category["id"])
    #             break
    # except KeyError as err:
    #     print(err)
    # print('a_cat_ids', a_cat_ids)

    categories = ['c1', 'c2', 'Desserts', 'c3']
    menuItems = ['mi1', "Apple Turnovers", 'mi2', "2 Apple Turnovers", 'mi3']
    item_specific_rules = ''
    for category in categories:
        if "desserts" in category.lower():
            for item_id in menuItems:
                if "2 apple turnover" in item_id.lower():
                    item_specific_rules += (
                        "Add '2 Apple Turnovers' "
                        "if customer ask for 'two' apple turnover "
                        "else 'Apple Turnover'\n"
                    )
                    break
                else:
                    print('item - ', item_id)
            break
        else:
            print('category - ', category)
    print('item_specific_rules - ', item_specific_rules)


