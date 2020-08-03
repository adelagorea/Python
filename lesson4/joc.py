from random import choices, choice, shuffle

path = 'countries.txt'  
countries = []

def read_file():
    with open(path, 'r') as f:
        return f.read().split('\n')

def make_array(raw):
    array = []
    for item in raw:
        tmp = item.split(",")
        
        array.append({
            "country": tmp[0],
            "capital": tmp[1]
        })
    return array

def make_question(data):
    selected_country = choice(data)
    other_capitals = choices([item['capital'] for item in data if item['country'] != selected_country['country']], k=3)
    return {"selected": selected_country, "other": other_capitals}

def get_answer(items):
    answer = int(input("alege o varianta: "))
    
    if items['true_answer']['capital'] == items['items'][answer-1]:
        print('\nAi raspuns corect!\nCapitala {} este {}.'.format(items['true_answer']['country'], items['true_answer']['capital']))
    else:
        print('\nAi raspuns gresit!\nCapitala {} este {}.'.format(items['true_answer']['country'], items['true_answer']['capital']))

def show_question(selected_items):

    answers = selected_items['other'] + [selected_items['selected']['capital']]
    
    shuffle(answers)       # amestecarea raspunsurilor
    
    print('Care este capitala {} ?'.format(selected_items['selected']['country']))

    for ind, item in enumerate(answers):
        print('{}. {}'.format(ind+1, item))

    get_answer({"true_answer": selected_items['selected'], 'items': answers})



countries = make_array(read_file())

choise_items = make_question(countries)

show_question(choise_items)