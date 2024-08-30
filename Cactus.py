
def cactus():
	clear()

	def plant_cacti():
		planted_cactus_sizes = {}
		current_row, current_col = 0, 0  # Start at the top-left corner (0, 0)
	
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				current_row, current_col = move_to(current_row, current_col, i, j)
				if get_ground_type() == Grounds.Soil:
					trade(Items.Cactus_Seed)
					plant(Entities.Cactus)
					planted_cactus_sizes[(i, j)] = measure()  # Store the size of the cactus
				elif get_ground_type() == Grounds.Turf:
					till()
					trade(Items.Cactus_Seed)
					plant(Entities.Cactus)
					planted_cactus_sizes[(i, j)] = measure()  # Store the size of the cactus
	
		return planted_cactus_sizes
	
	def move_to(current_row, current_col, target_row, target_col):
		while current_row < target_row:
			move(South)
			current_row += 1
		while current_row > target_row:
			move(North)
			current_row -= 1
	
		while current_col < target_col:
			move(East)
			current_col += 1
		while current_col > target_col:
			move(West)
			current_col -= 1
	
		return current_row, current_col  # Return updated position
	
	def is_sorted(i, j):
		current_size = measure()
	
		# Check North
		if i > 0 and measure(North) > current_size:
			return False
	
		# Check East
		if j < get_world_size() - 1 and measure(East) > current_size:
			return False
	
		# Check South
		if i < get_world_size() - 1 and measure(South) < current_size:
			return False
	
		# Check West
		if j > 0 and measure(West) < current_size:
			return False
	
		return True
	
	def swap_to_sort():
		for _ in range(5):  # Perform 5 passes to sort the field
			current_row, current_col = 0, 0  # Start at the top-left corner
	
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					current_row, current_col = move_to(current_row, current_col, i, j)
	
					# Check and swap with North neighbor if needed (moving larger cacti up)
					if i > 0 and measure(North) < measure():
						swap(North)
	
					# Check and swap with East neighbor if needed (moving larger cacti right)
					if j < get_world_size() - 1 and measure(East) < measure():
						swap(East)
	
	def harvest_cacti():
		current_row, current_col = 0, 0  # Start at the top-left corner
	
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				current_row, current_col = move_to(current_row, current_col, i, j)
				if can_harvest() and is_sorted(i, j):
					harvest()
					break  # Stop once any cactus is harvested, as it will harvest all cacti
	
	# Step 1: Plant the cacti and record their sizes
	planted_cactus_sizes = plant_cacti()
	
	# Step 2: Perform multiple passes to sort the field, moving larger cacti North and East
	swap_to_sort()
	
	# Step 3: Harvest the cacti if they are sorted
	harvest_cacti()
	
	
while True:
	cactus()
	