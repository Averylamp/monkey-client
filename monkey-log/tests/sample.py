import monkey

with open('outputs/a', 'w') as f:
    f.write('a\n')
print('a')

monkey.init({'p1': 5, 'p2': 6})

with open('outputs/b', 'w') as f:
    f.write('b\n')
print('b')

while True:
    pass
