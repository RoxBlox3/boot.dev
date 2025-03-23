def get_most_common_enemy(enemies_dict):
    highest = float("-inf")
    enemy_name = None
    for name in enemies_dict:
        if enemies_dict[name] > highest:
            highest = enemies_dict[name]
            enemy_name = name
    return enemy_name
