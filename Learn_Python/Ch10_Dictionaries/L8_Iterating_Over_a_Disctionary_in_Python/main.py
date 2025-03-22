def get_most_common_enemy(enemies_dict):
    highest = 0
    for name in enemies_dict:
        if enemies_dict[name] > highest:
            highest = enemies_dict[name]
    return highest
