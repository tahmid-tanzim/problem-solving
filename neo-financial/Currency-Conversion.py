import json
import csv
from urllib.request import urlopen


class Graph:
    """
    @Title: Neo Financial - Technical Assignment
    @Problem: Currency Conversion
    @Author: Tahmid Tanzim <tahmid.tanzim@gmail.com>
    @GitHub: https://github.com/tahmid-tanzim
    @Date: 2022-04-27
    """

    def __init__(self, items):
        self.fx_rates = dict()              # Adjacency List {'EUR': [('USD', 12.3), ('CAD', 45.6)]}
        self.currency_list = list()         # [{'code': 'EUR', 'name': 'Euro'}]
        self.visited = dict()               # {'EUR': False}
        self.max_exchange_rate = -1.0
        self.best_conversion_path = list()  # ['CAD', 'BRL', 'ARS']
        self.setup(items)

    def addEdge(self, from_currency_code, to_currency_code, from_currency_name, to_currency_name, ex_rate):
        if from_currency_code not in self.fx_rates:
            self.fx_rates[from_currency_code] = list()
            self.currency_list.append({
                "code": from_currency_code,
                "name": from_currency_name
            })
        if to_currency_code not in self.fx_rates:
            self.fx_rates[to_currency_code] = list()
            self.currency_list.append({
                "code": to_currency_code,
                "name": to_currency_name
            })

        # Creating Adjacency List
        self.fx_rates[from_currency_code].append((to_currency_code, ex_rate,))

    def setup(self, items):
        hash_table = dict()
        for item in items:
            self.addEdge(
                item['fromCurrencyCode'],
                item['toCurrencyCode'],
                item['fromCurrencyName'],
                item['toCurrencyName'],
                item['exchangeRate']
            )
            hash_table[f"{item['fromCurrencyCode']}-{item['toCurrencyCode']}"] = item['exchangeRate']

        # Store reversed exchange rate if not provided as an input
        for item in items:
            if f"{item['toCurrencyCode']}-{item['fromCurrencyCode']}" not in hash_table:
                self.addEdge(
                    item['toCurrencyCode'],
                    item['fromCurrencyCode'],
                    item['toCurrencyName'],
                    item['fromCurrencyName'],
                    float(1 / item['exchangeRate'])
                )

    def depthFirstSearch(self, current_currency, target_currency, amount, conversion_path, currency_stack):
        # Mark current currency as visited
        self.visited[current_currency] = True

        # Pre-calculated conversion rate stored in currency_stack
        # Top of the stack is the last calculated conversion rate
        currency_stack.append(currency_stack[-1] * amount)
        conversion_path.append(current_currency)

        # Check if current_currency reached to the destination.
        if current_currency == target_currency:
            # print(currency_stack, conversion_path)
            current_amount = currency_stack[-1]
            if current_amount > self.max_exchange_rate:
                self.max_exchange_rate = current_amount
                self.best_conversion_path = conversion_path.copy()
        else:
            # If current_currency NOT reached to the destination.
            # Then recursively check for all the adjacent NOT visited currency
            for adjacent_currency, rate in self.fx_rates[current_currency]:
                if not self.visited[adjacent_currency]:
                    self.depthFirstSearch(adjacent_currency, target_currency, rate, conversion_path, currency_stack)

        # Reset before return from DFS
        currency_stack.pop()
        conversion_path.pop()
        self.visited[current_currency] = False

    def startPathTraversal(self, original_currency, target_currency, amount):
        # initialize max_exchange_rate & best_conversion_path
        self.max_exchange_rate = -1.0
        self.best_conversion_path = list()

        # initialize visited dictionary
        for currency in self.currency_list:
            code = currency["code"]
            self.visited[code] = False

        self.depthFirstSearch(original_currency, target_currency, amount, conversion_path=[], currency_stack=[1.0])
        return self.max_exchange_rate, " | ".join(self.best_conversion_path),


def generateCSV(row, version):
    # CSV file name with seedId as version number.
    filename = f"Currency-Conversion-Output-{version}.csv"

    # Append a row to the CSV file
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
        file.close()


def getResponse(url):
    response = None
    try:
        response = urlopen(url)
    except Exception as ex:
        print("Sorry!", ex)
        return list()
    else:
        body = response.read()
        return json.loads(body)
    finally:
        if response is not None:
            response.close()


if __name__ == '__main__':
    seedId = 62861
    data = getResponse(f"https://api-coding-challenge.neofinancial.com/currency-conversion?seed={seedId}")
    graph_obj = Graph(data)

    start_currency_code = "CAD"
    start_amount = 100.0

    for currency in graph_obj.currency_list:
        end_currency_code = currency["code"]
        end_currency_name = currency["name"]

        # Ignore operation, if end_currency_code is CAD
        if start_currency_code != end_currency_code:
            best_conversion_rate, pipe_delimited_path = graph_obj.startPathTraversal(
                start_currency_code,
                end_currency_code,
                start_amount
            )

            # Check if any path exist from start_currency_code to end_currency_code
            if best_conversion_rate != -1.0:
                # print(
                #     end_currency_code,
                #     end_currency_name,
                #     best_conversion_rate,
                #     pipe_delimited_path,
                #     end="\n\n"
                # )
                generateCSV([
                    end_currency_code,
                    end_currency_name,
                    best_conversion_rate,
                    pipe_delimited_path
                ], seedId)
