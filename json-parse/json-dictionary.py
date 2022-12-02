import json

if __name__ == "__main__":
    # Opening JSON file
    with open('hardware-inventory-metadata-response.json') as json_file:
        data = json.load(json_file)
        # Print the type of data variable
        json_string = "{\"total_fields\":\"" + str(len(data["fields"])) + "\",\"fields\":["
        for item in data["fields"]:
            json_string += "{\"field_label\":\"" + item['field_label'] + "\",\"api_name\":\"" + item['api_name'] + "\"},"
        json_string += "]}"

        with open('hardware-inventory-fields.json', 'w') as outfile:
            outfile.write(json_string)