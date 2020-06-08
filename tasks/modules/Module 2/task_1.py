
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


def add_to_inventory(inventory, added_items):
    excluded_items = ['chewed gum', 'rubbish', 'used tissue']
    skipped_items = {}
    num_of_added_items = 0

    # Update inventory or exclude items
    for added_item in added_items:
        if added_item not in excluded_items:
            inventory[added_item] = inventory.get(added_item, 0) + 1
            num_of_added_items += 1
        else:
            skipped_items[added_item] = skipped_items.get(added_item, 0) + 1

    # Print results
    print(f'Added {num_of_added_items} items to the inventory')
    print('Skipped:')
    for item_name, item_num in skipped_items.items():
        print(item_num, item_name)

    return inventory


if __name__ == '__main__':
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = [
        'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',
        'rubbish', 'chewed gum', 'used tissue']

    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
