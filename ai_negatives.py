#!/usr/bin/python3

def sort_dictionary_by_value(x) -> dict:
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}


def group_ai_negatives(negatives) -> dict:
    frequency = {}
    item_map = {}
    group = {}
    for item in negatives:
        # Processing item map
        if item not in item_map:
            item_map[item] = set()
        item_map[item].update(negatives[item])
        for child_item in negatives[item]:

            if child_item not in item_map:
                item_map[child_item] = set()
            item_map[child_item].add(item)

        # Processing frequency
        for child_item in [item] + negatives[item]:
            if child_item not in frequency:
                frequency[child_item] = 0
            frequency[child_item] += 1

    frequency = sort_dictionary_by_value(frequency)
    item = next(iter(frequency))

    while frequency[item] > 0:
        item_set = {x for x in item_map[item] if x not in group}
        if len(item_set) > 0:
            group[item] = item_set
        frequency[item] = 0
        for key in item_map[item]:
            frequency[key] -= 1
        frequency = sort_dictionary_by_value(frequency)
        item = next(iter(frequency))

    return group


if __name__ == "__main__":
    # print(group_ai_negatives(
    #     negatives={
    #         'famous star with cheese': ['no meat famous star'],
    #         'no meat famous star': ['single famous star', 'famous star with cheese', 'no meat el diablo'],
    #         'no meat el diablo': ['el diablo', 'single el diablo', 'no meat famous star'],
    #         'el diablo': ['no meat el diablo']
    #     }
    # ))

    # positives_map = {}
    # negatives_map = {}

    # positives_map = {"a": {1, 3}}
    # negatives_map = {}

    # positives_map = {}
    # negatives_map = {"c": {2, 4}}

    positives_map = {"a": {1, 3}}
    negatives_map = {"c": {2, 4}}
    string = ""
    if positives_map or negatives_map:
        if positives_map and negatives_map:
            string += "\nBoth `Positive Items` and `Negative Items` map is a collection of key/value pairs, "
        elif positives_map and not negatives_map:
           string += "\nThe `Positive Items` map is a collection of key/value pairs, "
        elif not positives_map and negatives_map:
           string += "\nThe `Negative Items` map is a collection of key/value pairs, "
        string += f"key is an item name and value is list of item names. "
        print(string)
