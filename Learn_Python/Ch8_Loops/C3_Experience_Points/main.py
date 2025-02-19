def calculate_experience_points(level):
    total_xp = 0
    for i in range(1, level):
        print(i)
        total_xp = i * 5 + total_xp
    return total_xp
