"""Module2/task1: Includes task of creating sandwich calculator based on user's input."""
import pyinputplus as pyip


# Vars
BREAD_TYPES_AND_PRICES = {'wheat': 4, 'white': 2, 'sourdough': 3}
PROTEIN_TYPES_AND_PRICES = {'chicken': 6, 'turkey': 7, 'ham': 7, 'tofu': 4.85}
CHEESE_TYPES_AND_PRICES = {'cheddar': 5, 'Swiss': 9, 'mozzarella': 7.5}
SAUCE_TYPES_AND_PRICES = {'mayo': 2.5, 'mustard': 2, 'lettuce': 1, 'tomato': 0.75}


def select_bread() -> dict:
    """Selects type of a bread.
        :return {bread_type, bread_price}
    """
    print("What type of bread do you want?")
    declared_bread = pyip.inputMenu([*BREAD_TYPES_AND_PRICES.keys()])
    return {bread: price for bread, price in BREAD_TYPES_AND_PRICES.items()
            if declared_bread == bread}


def select_protein() -> dict:
    """Selects type of protein.
        :return {protein_type, protein_type}
    """
    print("What type of protein do you want?")
    declared_protein = pyip.inputMenu([*PROTEIN_TYPES_AND_PRICES.keys()])
    return {protein: price for protein, price in PROTEIN_TYPES_AND_PRICES.items()
            if declared_protein == protein}


def select_cheese() -> dict:
    """Selects type of a cheese.
        :return {cheese_type, cheese_price}
    """
    if pyip.inputYesNo('Do you want cheese?') == 'no':
        return {}

    print("What type of cheese do you want?")
    declared_cheese = pyip.inputMenu([*CHEESE_TYPES_AND_PRICES.keys()])
    return {cheese: price for cheese, price in CHEESE_TYPES_AND_PRICES.items()
            if declared_cheese == cheese}


def select_sauce() -> dict:
    """Selects type of a sauce.
        :return {sauce_type, sauce_price}
    """
    if pyip.inputYesNo('Do you want sauce?') == 'no':
        return {}

    print("What type of sauce do you want?")
    declared_sauce = pyip.inputMenu([*SAUCE_TYPES_AND_PRICES.keys()])
    return {sauce: price for sauce, price in SAUCE_TYPES_AND_PRICES.items()
            if declared_sauce == sauce}


def select_sandwich_amount() -> int:
    return pyip.inputInt('How many sandwiches do you want?', min=1)


def prepare_sandwich() -> dict:
    """Prepares dict consisting of sandwich data."""
    # Factory approach would be overengineering? :D
    ingredients = [select_bread, select_protein, select_cheese, select_sauce]
    sandwich = {}
    for ingredient in ingredients:
        # TODO: move validation (cheese, sauce) to prepare_sandwich()?
        sandwich.update(ingredient())
    return sandwich


def agregate_order(sandwich: dict):
    """Displays order. Calculates price, lists ingredients.
    :param sandwich: {ingredient: amount}
    """
    sandwich_amount = select_sandwich_amount()  # TODO: outside function scope, provided as param?
    price = round(sandwich_amount * (sum(sandwich.values())), 2)
    print(f"Your sandwich consists of {', '.join(sandwich.keys())}. "
          f"You wanted {sandwich_amount} sandwich{'es' if sandwich_amount > 1 else ''}. "
          f"That's a total of {price} euro.")


if __name__ == '__main__':
    prepared_sandwich = prepare_sandwich()
    agregate_order(prepared_sandwich)
