def harvest_trees():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			plant(Entities.Tree)
		move(North)
		move(East)
	move(East)
	move(East)
