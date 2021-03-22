aliens = []
for numbers in range(30):
    number_alien = {'color': 'blue',
                    'points' : 5,
                    'speed' : 'medium'
    }
    aliens.append(number_alien)

print(aliens[:5])
print(len(aliens))

print("\n\n\n")

for change in aliens[:5]:
    if change['color']=="blue":
        change['color'] = 'green'
        change['points'] = 15
        change['speed'] = 'slow'
for change in aliens[5:]:
    if change['color']== "blue":
        change['color'] = 'violet'
        change['points'] = 400
        change['speed'] = 'speed'

for a in aliens[:20]:
    print(a)
