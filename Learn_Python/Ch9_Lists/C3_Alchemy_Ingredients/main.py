def check_ingredient_match(recipe, ingredients):
    missing = []
    for i in range(0, len(recipe)):
        if recipe[i] == ingredients[i]:
            missing.append(ingredients[i])
    percentage = 100 * len(ingredients) / len(recipe)
    return percentage, missing
