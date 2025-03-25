# Функция calculate_pizza принимает словарь ingredients, где ключи — это названия ингредиентов, а значения — их калорийность.
def calculate_pizza(ingredients):
    # Вычисление общего количества калорий:
    # Используется генераторное выражение для суммирования калорийности всех ингредиентов.
    # ingredients.get(ingredient, 0) возвращает калорийность ингредиента, если он есть в словаре, или 0, если его нет.
    calories = sum(ingredients.get(ingredient, 0) for ingredient in ingredients)
    # Вычисление общей стоимости ингредиентов:
    # Используется генераторное выражение для суммирования стоимости всех ингредиентов.
    # ingredients.get(ingredient, 0) возвращает калорийность ингредиента, затем умножаем её на 0.7 (предположим, что это стоимость за единицу калорий).
    cost = sum(ingredients.get(ingredient, 0) * 0.7 for ingredient in ingredients)
    # Возвращение кортежа из двух значений: общее количество калорий и общая стоимость.
    return calories, cost