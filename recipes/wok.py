def calculate_wok(ingredients):
    calories = sum(ingredients.get(ingredient, 0) for ingredient in ingredients)
    cost = sum(ingredients.get(ingredient, 0) * 0.6 for ingredient in ingredients)
    return calories, cost