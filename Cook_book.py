cook_book = dict()

def add_recip(text):
    end = 'text'
    while end != '':
        recip = text.readline().strip()
        cook_book[recip] = list()
        ingredients_number = int(text.readline())
        while ingredients_number != 0:
            ingredient = dict()
            line = text.readline()
            line_content = line.split(' | ')
            ingredient['ingredient_name'] = line_content[0]
            ingredient['quantity'] = int(line_content[1])
            ingredient['measure'] = line_content[2].strip()
            cook_book[recip].append(ingredient)
            ingredients_number -= 1
        end = text.readline()

with open('recipes.txt', encoding='utf-8') as text:
    add_recip(text)

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    buy_list = dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in buy_list:
                ingredient['quantity'] += buy_list[ingredient['ingredient_name']]['quantity']
            buy_list[ingredient['ingredient_name']] = {
                'measure' : ingredient['measure'],
                'quantity': ingredient['quantity']
            }
    for ingredient in buy_list.values():
        ingredient['quantity'] *= person_count
    return buy_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
