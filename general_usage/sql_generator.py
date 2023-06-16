import random

users = 8
cpus = 8

collection = []

while len(collection) <= 60:
    target = [random.randint(1, cpus), random.randint(1, users)]
    if target in collection:
        continue
    collection.append(target)

print('\n'.join([f"INSERT INTO pilihan VALUES ({index}, {x[0]}, {x[1]});" for index, x in enumerate(collection)]))
    
