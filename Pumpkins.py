def harvest_pumpkins():
	b = 1
	while True:
		for i in range(get_world_size()):
			for i in range(get_world_size()):
				a = 1
				
				if can_harvest() and get_ground_type() == Grounds.Soil:
					move(North)
				else:
					b = 0
					if get_ground_type() == Grounds.Soil:
						trade(Items.Pumpkin_Seed)
						plant(Entities.Pumpkin)
						move(North)
						a = 0
					elif get_ground_type() == Grounds.Turf:
						till()
						trade(Items.Pumpkin_Seed)
						plant(Entities.Pumpkin)
						move(North)
						a = 0
					else:
						move(North)
						a = 0
			move(East)
		if a == 1 and can_harvest() and b == 1:
				do_a_flip()
				do_a_flip()
				harvest()
				till()
				trade(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)
				move(North)
		else:
			b += 1
		

