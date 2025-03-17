def validate_path(expected_path, character_path):
    character_name = character_path.pop(0)
    right = 0
    for i in range(0, len(expected_path)):
        if expected_path[i] == character_path[i]:
            right += 1
    percentage = right * 100 / len(expected_path)
    return (character_name, percentage)
