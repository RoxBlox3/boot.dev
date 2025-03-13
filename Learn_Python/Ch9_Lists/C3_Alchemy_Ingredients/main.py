def check_ingredient_match(recipe, ingredients):
    missing = []
    for i in range(0, len(recipe)):
        if recipe[i] != ingredients[i]:
            missing.append(recipe[i])
    percentage = 100 * len(missing) / len(recipe)
    return percentage, missing
