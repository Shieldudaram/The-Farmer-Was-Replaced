def harvest_bush():
	while True:
			for i in range(get_world_size()):
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					move(North)
				else:
					move(North)
			move(East)
			

