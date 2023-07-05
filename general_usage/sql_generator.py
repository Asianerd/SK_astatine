import random

names = [
    ["Robert", "John", "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Alexander", "Frank", "Patrick", "Raymond", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Adam", "Nathan", "Henry", "Douglas", "Zachary", "Peter", "Kyle", "Ethan", "Walter", "Noah", "Jeremy", "Christian", "Keith", "Roger", "Terry", "Gerald", "Harold", "Sean", "Austin", "Carl", "Arthur", "Lawrence", "Dylan", "Jesse", "Jordan", "Bryan", "Billy", "Joe", "Bruce", "Gabriel", "Logan", "Albert", "Willie", "Alan", "Juan", "Wayne", "Elijah", "Randy", "Roy", "Vincent", "Ralph", "Eugene", "Russell", "Bobby", "Mason", "Philip", "Louis"],
    ["Youtz", "Malich", "Daughenbaugh", "Strome", "Baltimore", "Dimick", "Chia", "Felch", "Kinderman", "Imler", "Klish", "Rodeheaver", "Thobe", "Lakin", "Wisener", "Ridlehoover", "Kitelinger", "Christianson", "Harkrader", "Harkleroad", "Easterlin", "Courtland", "Hipple", "Van Every", "Goleman", "Biffle", "Pershing", "Dollar", "Governor", "Settlemire", "Sauerbrey", "Crownover", "Rodenbaugh", "Harjo", "Lepley", "Canine"]
    ]

users = 39
cpus = 42

collection = []

"""TODO : MAKE THE PILIHAN TABLE AGAIN"""

while len(collection) <= (0.8 * (39 * 42)):
    target = [random.randint(1, users), random.randint(1, cpus)]
    if target in collection:
        continue
    collection.append(target)

print('\n'.join([f"INSERT INTO pilihan VALUES ({index}, {x[0]}, {x[1]});" for index, x in enumerate(collection)]))

def gen_users(amount, starting_index):
    target_users = []
    while len(target_users) < amount:
        name = [
            random.choice(names[0]),
            random.choice(names[1])
        ]
        if (name in [i['name'] for i in target_users]):
            continue
        
        u = {
            'name': ' '.join(name),
            'username': '_'.join([str(i).lower() for i in name]),
            'password': f"{name[0].lower()[0]}{name[1]}1!"
        }
        
        target_users.append(u)
        
    for i, x in enumerate(target_users):
        print(f"INSERT INTO pelanggan VALUES({i + starting_index}, \'{x['name']}\', \'{x['username']}\', \'{x['password']}\', 0);")
        
#gen_users(30, 10)        
