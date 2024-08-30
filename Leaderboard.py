def start_leaderboard_challenge():
    timed_reset()  # Start the leaderboard challenge by resetting the game
    
    # Set up the initial position to start harvesting
    for i in range(2):
        for j in range(2):
            if j < 1:  # Move right if not at the end of the row
                move(East)
        if i < 1:  # Move down and return to the start of the row
            move(South)
            move(West)

    # Continuously harvest wheat in a 2x2 grid and unlock "Grass" when available
    while True:
        # Check if Grass unlock is available and unlock it
        if num_unlocked(Unlocks.Grass) == 0:  # Check if Grass is not yet unlocked
            grass_cost = get_cost(Unlocks.Grass)
            if all(num_unlocked(item) >= grass_cost[item] for item in grass_cost):  # Check if we have enough resources
                unlock(Unlocks.Grass)  # Unlock Grass

        # Harvesting loop
        for i in range(2):
            for j in range(2):
                if can_harvest():  # Check if wheat is ready to harvest
                    harvest()  # Harvest the wheat
                if j < 1:  # Move right if not at the end of the row
                    move(East)
            if i < 1:  # Move down and return to the start of the row
                move(South)
                move(West)

start_leaderboard_challenge()

