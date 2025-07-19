people = [
    {"name": "Александр", "age": 21},
    {"name": "Мария", "age": 17},
    {"name": "Илья", "age": 25},
    {"name": "Олег", "age": 15},
    {"name": "Елена", "age": 22},
    {"name": "Юля", "age": 19},
    {"name": "Анна", "age": 18}
]

def sort_filt_map_list(people):
    filt = list(filter(lambda p: p['age'] >= 18, people))
    sort_list = sorted(filt, key=lambda pe: len(pe['name']))
    print(sort_list)

sort_filt_map_list(people)
