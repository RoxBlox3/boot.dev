def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    if energy_available * meters_per_energy >= distance_one_way * 2:
        return True
    else:
        return False
