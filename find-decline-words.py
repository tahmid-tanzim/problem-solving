#!/usr/bin/python3

DECLINE_WORDS = [
    "nope",
    "no",
    "now",
    "nothing",
    "nah",
    "no thats it",
    "not today",
    "negative",
    "dont",
    "don't",
    "neither",
]
NON_DECLINE_WORDS = [
    "no egg",
    "no tomato",
    "no cheese",
    "no bacon",
    "no mayonnaise",
    "no onion",
    "no special sauce",
    "no dipping sauce",
    "no sauce",
    "no butter",
    "no meat nachos",
    "no meat taco salad",
]


class EventParser:
    @staticmethod
    def find_decline_words(content: str) -> bool:
        non_decline_word_index = [content.index(w) for w in NON_DECLINE_WORDS if w in content]
        for w in DECLINE_WORDS:
            if w in content:
                decline_word_index = content.index(w)
                # Check if decline_word is not overlapping with non_decline_word
                if decline_word_index not in non_decline_word_index:
                    return True
        return False

    def run(self):
        # OUTPUT = {
        #     'True': 'DECLINE WORD EXIST',
        #     'False': 'NO DECLINE WORD EXIST',
        # }
        inputs = (
            {
                'content': 'Can I get number one with no onions and no cheese',
                'output': 'False'
            },
            {
                'content': 'Can I get number one with no onions',
                'output': 'False'
            },
            {
                'content': 'Can I get number one',
                'output': 'False'
            },
            {
                'content': 'can I get number 2 with no tomato',
                'output': 'False'
            },
            {
                'content': 'no Can I get number one with no onions and no cheese',
                'output': 'True'
            },
            {
                'content': 'no not now thanks can I get number 2 with no tomato',
                'output': 'True'
            },
            {
                'content': 'no thanks can I get number 2 with no tomato',
                'output': 'True'
            },
            {
                'content': 'no. please can I get number 2 with no dipping sauce',
                'output': 'True'
            },
            {
                'content': 'Please no can I get number 2 with no special sauce',
                'output': 'True'
            },
            {
                'content': 'Please no. can I get number 2 with no bacon',
                'output': 'True'
            },
            {
                'content': 'no thats it can I get number 2 with no bacon',
                'output': 'True'
            },
            {
                'content': 'not today can I get number 2 with no bacon',
                'output': 'True'
            },
            {
                'content': 'nothing can I get number 2 with no egg',
                'output': 'True'
            },
            {
                'content': 'nope can I get number 2 with no meat nachos',
                'output': 'True'
            },
            {
                'content': 'now can I get number 2 with no butter',
                'output': 'True'
            },
            {
                'content': 'no thanks can I get number 2',
                'output': 'True'
            },
            {
                'content': 'no thanks can I get number 2',
                'output': 'True'
            },
            {
                'content': 'no. please can I get number 2',
                'output': 'True'
            },
            {
                'content': 'Please no can I get number 2',
                'output': 'True'
            },
            {
                'content': 'Please no. can I get number 2',
                'output': 'True'
            },
            {
                'content': 'no thats it can I get number 2',
                'output': 'True'
            },
            {
                'content': 'not today can I get number 2',
                'output': 'True'
            },
            {
                'content': 'nothing can I get number 2',
                'output': 'True'
            },
            {
                'content': 'nope can I get number 2',
                'output': 'True'
            },
            {
                'content': 'now can I get number 2',
                'output': 'True'
            },
        )

        for i in inputs:
            o = self.find_decline_words(i['content'])
            print(f'Content - {i["content"]}\nExpected Output - {i["output"]}\nOriginal Output - {o}', end='\n\n')


if __name__ == "__main__":
   e1 = EventParser()
   e1.run()
