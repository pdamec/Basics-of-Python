"""Task 1 and 2 of 2nd Module."""


# Globals
# TODO: move globals to separate setting module?
EXCLUDED_ITEMS = ['chewed gum', 'rubbish', 'used tissue']
INVENTORY_LIGHT_WEIGHT = 60
INVENTORY_HEAVY_WEIGHT = 70
INVENTORY_MAX_WEIGHT = 80


def display_inventory(inventory: dict):
    """Display hero's inventory.

    Arguments:
        inventory   -- {item_name: item_num}
    """
    print('Inventory:')
    item_total = 0
    for item_name, item_count in inventory.items():
        print(item_count, item_name)
        item_total += item_count

    # Print weight capacity
    print(f'\nTotal number of items: {str(item_total)}\n')
    if INVENTORY_LIGHT_WEIGHT <= item_total < INVENTORY_HEAVY_WEIGHT:
        print('CAUTION: Your backpack weighs a lot, '
              'your stamina runs out quicker!')
    elif INVENTORY_HEAVY_WEIGHT <= item_total < INVENTORY_MAX_WEIGHT:
        print('CAUTION: Your equipment is very heavy, '
              'you\'re moving slower than usual!')
    elif item_total >= INVENTORY_MAX_WEIGHT:
        print('CAUTION: You are overloaded, can\'t move!')


def add_to_inventory(inventory: dict, added_items) -> dict:
    """Add provided items to inventory object.

    Arguments:
        inventory   -- dict to which we add items: {item_name: item_num}
        added_items -- items that shall be added to the inventory,
                       aside from those stored in EXCLUDED_LIST.

    Returns:
        Updated inventory.
    """
    skipped_items = {}
    num_of_added_items = 0

    # Update inventory or exclude items
    for added_item in added_items:
        if added_item not in EXCLUDED_ITEMS:
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
    # Inventory data
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = [
        'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',
        'rubbish', 'chewed gum', 'used tissue']

    # Execution
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
