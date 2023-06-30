from pprint import pprint
from WordCounter import WordCounter

def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def sort_people(people_list, field, direction):
        people_list.sort(key=lambda p: p[field], reverse=(direction == 'desc'))

    sort_people(people_list,"weight", "desc")
    print(people_list)

def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    def filter_males(people_list):
        newList = list(filter(lambda p:p['sex']=='male', people_list))
        return newList
    filtered_list = filter_males(people_list)
    print(filtered_list)

def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    #def calc_bmi(people_list):
        #The double asterisks (**) in Python are used for dictionary unpacking
        #Also known as "keyword argument unpacking."
        #The dictionary unpacking is used to create a new dictionary that includes 
        #All the existing key-value pairs from person as well as an additional key-value pair 
        # bmi = list(map(lambda p:{**p, 'bmi': round(p['weight_kg']/p['height_meters']**2,1)},people_list))
        # return bmi
    #new_people_list = calc_bmi(people_list)   
    #print(new_people_list)
    def transform_person(person):
        retval = {
            'id': person['id'],
            'name': person['name'],
            'weight_kg': person['weight_kg'],
            'height_meters': person['height_meters'],
            'bmi':round(person['weight_kg'] / person['height_meters'] ** 2, 1)
        }
        return retval
    new_people_list = list(map(transform_person,people_list))
    print(new_people_list)

def ex4():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
    def get_people(listPeople):
        newList = [p['name'] for p in listPeople if p['age'] >= 15 ]
        return newList
    newList = get_people(people_list)
    print(newList)

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    # word_counter.count_words()
    print(word_counter.get_word_count()) 
    # print(word_counter.get_shortest_word())
    # print(word_counter.get_longest_word())
ex5()




    
