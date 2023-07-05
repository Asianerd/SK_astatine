raw = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga aspernatur dolores quasi molestiae deleniti consequatur rem blanditiis aperiam eum, veritatis veniam harum, nulla possimus tenetur iste. Voluptate pariatur eum itaque."

r = [[]]
for index, x in enumerate(raw.split()):
    if (index % 5 == 0):
        r.append([])
    r[-1].append(x)

print('\n'.join([','.join(i) for i in r]))
