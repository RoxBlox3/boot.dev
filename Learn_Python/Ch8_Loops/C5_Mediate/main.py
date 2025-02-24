def meditate(mana, max_mana, energy, energy_drinks):
    while mana != max_mana and (energy_drinks > 0 or energy > 0):
        if energy == 0 and energy_drinks > 0:
            energy_drinks -= 1
            energy += 50
            print(energy)
        else:
            mana += 1
            energy -= 1
        print(f"{mana} and energy {energy}")
    return mana, energy, energy_drinks
