"""Module2/task1: Includes task of creating sandwich calculator based on user's input."""
from dataclasses import dataclass
import typing
from decimal import Decimal, getcontext

import pyinputplus as pyip


@dataclass
class Ingredient:
    """Dataclass to match product name with it's price and types."""

    name: str
    choices: typing.Dict[str, float]
    required: bool = False

    def __repr__(self):
        return self.name


INGREDIENTS = [
    Ingredient(
        name='bread',
        choices={'wheat': 4, 'white': 2, 'sourdough': 3},
        required=True),
    Ingredient(
        name='protein',
        choices={'chicken': 6, 'turkey': 7, 'ham': 7, 'tofu': 4.85},
        required=True),
    Ingredient(
        name='cheese',
        choices={'cheddar': 5, 'Swiss': 9, 'mozzarella': 7.5}),
    Ingredient(
        name='sauce',
        choices={'mayo': 2.5, 'mustard': 2, 'lettuce': 1, 'tomato': 0.75})
]


IngredientDict = typing.Dict[str, float]
IngredientList = typing.List[Ingredient]


def prepare_sandwich(ingredients: IngredientList) -> IngredientDict:
    """Prepare sandwich data."""
    sandwich = {}
    for ingredient in ingredients:
        if not ingredient.required:
            if pyip.inputYesNo(f'Do you want {ingredient}?') == 'no':
                continue

        print(f"What type of {ingredient} do you want?")
        selected_ingredient = pyip.inputMenu([*ingredient.choices.keys()])
        sandwich.update({selected_ingredient: ingredient.choices[selected_ingredient]})
    return sandwich


def agregate_order(sandwich: IngredientDict):
    """Display order. Calculates price, lists ingredients."""
    sandwich_amount = pyip.inputInt('How many sandwiches do you want?', min=1)
    getcontext().prec = 2
    price = Decimal(sandwich_amount) * Decimal(sum(sandwich.values()))
    print(f"Your sandwich consists of {', '.join(sandwich.keys())}. "
          f"You wanted {sandwich_amount} sandwich{'es' if sandwich_amount > 1 else ''}. "
          f"That's a total of {price} euro.")


if __name__ == '__main__':
    prepared_sandwich = prepare_sandwich(INGREDIENTS)
    agregate_order(prepared_sandwich)
