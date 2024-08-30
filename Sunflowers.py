while True:
	harvest_sunflowers()
	
	
	
def plant_through_patch():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
				if can_harvest():
					harvest()
					till()
					if get_ground_type() == Grounds.Soil: 
						trade(Items.Sunflower_Seed)
						plant(Entities.Sunflower)
						move(North)
					elif get_ground_type() == Grounds.Turf:
						till()
						trade(Items.Sunflower_Seed)
						plant(Entities.Sunflower)
						move(North)
				else:
					move(North)
			
		move(East)


def harvest_sunflowers():
	petals = 9

		
	while True:
			if petals < 10:
				clear()
				do_a_flip()
				do_a_flip()
				plant_through_patch()
				petals = 15
				do_a_flip()
				do_a_flip()
				do_a_flip()
				do_a_flip()
				do_a_flip()
			else:
				
				for k in range(get_world_size()):
					for l in range(get_world_size()):
						if measure() == petals and can_harvest():
							harvest()
							move(North)
						else:
							move(North)
					move(East)
					
				petals = petals - 1
				
