def regenerate(current_health, max_health, enemy_distance):
    while current_health != max_health and enemy_distance > 3:
        current_health += 1
        print(current_health)
        enemy_distance -= 2
        print(enemy_distance)
    return current_health
