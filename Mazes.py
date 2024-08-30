def restart_maze():
	harvest()
	harvest()
	plant(Entities.Bush)
	
def maze_moving():
    directions = [North, East, South, West]  # Directions in clockwise order
    facing_index = 0  # Start by facing North

    def can_move(facing_direction):
        return move(facing_direction) == True

    while True:
        # Step 1: Try to move right (follow the wall on the right)
        right_index = (facing_index + 1) % 4
        if can_move(directions[right_index]):
            facing_index = right_index  # Turn right

            if get_entity_type() == Entities.Treasure:
                restart_maze()
                break  # Stop once treasure is found

        # Step 2: If right is blocked, try moving forward
        elif can_move(directions[facing_index]):
  # Continue moving forward
            if get_entity_type() == Entities.Treasure:
                restart_maze()
                break  # Stop once treasure is found

        # Step 3: If forward is blocked, try to move left
        else:
            left_index = (facing_index - 1) % 4
            if can_move(directions[left_index]):
                facing_index = left_index  # Turn left
                if get_entity_type() == Entities.Treasure:
                    restart_maze()
                    break  # Stop once treasure is found

            # Step 4: If all else fails, turn around (go back)
            else:
                facing_index = (facing_index + 2) % 4  # Turn around
                if get_entity_type() == Entities.Treasure:
                    restart_naze()
                    break  # Stop once treasure is found
                    
                    
def bushfield():
	harvest()
	plant(Entities.Bush)
	trade(Items.Fertilizer)
	use_item(Items.Fertilizer)
	while True:
		make_maze()
	
def startmaze():
	if can_harvest():
		for l in range(get_world_size()):
			for l in range(get_world_size()):
				trade(Items.Fertilizer)
				use_item(Items.Fertilizer)
				
def make_maze():
	if get_entity_type() == Entities.Treasure or get_entity_type() == Entities.Hedge:
			maze_moving()
	else:
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
		make_maze()


while True:	
	clear()
	bushfield()
	
