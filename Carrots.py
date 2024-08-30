def harvest_carrots():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			till()
			if get_ground_type() == Grounds.Soil: 
				trade(Items.Carrot_Seed)
				plant(Entities.Carrots)
				move(North)
			elif get_ground_type() == Grounds.Turf:
				till()
				trade(Items.Carrot_Seed)
				plant(Entities.Carrots)
				move(North)
		else:
			move(North)

	move(East)
