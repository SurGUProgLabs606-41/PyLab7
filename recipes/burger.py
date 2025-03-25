def calculate_burger(ingredients):
    calories = sum(ingredients.get(ingredient, 0) for ingredient in ingredients)
    cost = sum(ingredients.get(ingredient, 0) * 0.5 for ingredient in ingredients)
    return calories, cost