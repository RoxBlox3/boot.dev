def check_ingredient_match(recipe, ingredients):
    missing = []
    for i in range(0, len(recipe)):
        value = 0
        for ingredient in range(0, len(ingredients)):
            if recipe[i] != ingredients[ingredient] and value == 0:
                value = 1
                missing.append(recipe[i])
    percentage = 100 * len(missing) / len(recipe)
    return percentage, missing
