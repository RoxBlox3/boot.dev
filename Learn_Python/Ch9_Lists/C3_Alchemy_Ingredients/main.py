def check_ingredient_match(recipe, ingredients):
    missing = []
    for i in range(0, len(recipe)):
        if recipe[i] not in ingredients:
            missing.append(recipe[i])
    percentage = 100 - (len(missing) * 100 / len(recipe))
    return percentage, missing
