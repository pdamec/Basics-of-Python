def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for item_name, item_count in inventory.items():
        print(item_count, item_name)
        item_total += item_count

    print(f'\nTotal number of items: {str(item_total)}\n')
    if 59 < item_total < 70:
        print('CAUTION: Your backpack weighs a lot, your stamina runs out quicker!')
    elif 69 < item_total < 80:
        print('CAUTION: Your equipment is very heavy, you\'re moving slower than usual!')


if __name__ == '__main__':
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    display_inventory(stuff)
