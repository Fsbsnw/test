def search(person):    
    people = [{'name': 'bob', 'age': 20}, 
            {'name': 'carry', 'age': 38},
            {'name': 'john', 'age': 7},
            {'name': 'smith', 'age': 17},
            {'name': 'ben', 'age': 27}]
    for i in people:
        if (i['name'] == person):
            print(i['age'])
search('bob')

