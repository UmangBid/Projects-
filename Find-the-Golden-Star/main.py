import random
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)

horizontal_val = random.randint(0,2)
vertical_val = random.randint(0,2)
map1[horizontal_val][vertical_val] = "⭐️"
gold_position = str(horizontal_val+1) + str(vertical_val+1)

position = input("What do you think: where is the Golden Star in the map? ")

if gold_position == position:
    print("Congratulations!!! You have found the Golden STAR!")
else:
    horizontal = int(position[0])
    vertical = int(position[1])
    map1[horizontal-1][vertical-1] = "🆇"
    print("Unfortunatly you could find it 🙁")

print_map(map1)