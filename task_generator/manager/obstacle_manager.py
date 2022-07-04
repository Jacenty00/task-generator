from task_generator.constants import Constants


class ObstacleManager:
    def __init__(self, namespace, map_manager, environment):
        self.map_manager = map_manager
        self.environment = environment

    def reset_scenario(self, scenario):
        pass

    def reset_random(
            self, 
            dynamic_obstacles=Constants.ObstacleManager.DYNAMIC_OBSTACLES,
            static_obstacles=Constants.ObstacleManager.STATIC_OBSTACLES,
            forbidden_zones=[]
        ):
        self.environment.remove_all_obstacles()

        for _ in range(dynamic_obstacles):
            position = self.map_manager.get_random_pos_on_map(safe_dist=1, forbidden_zones=forbidden_zones)

            self.environment.spawn_random_dynamic_obstacle(position=position)
        
        for _ in range(static_obstacles):
            position = self.map_manager.get_random_pos_on_map(safe_dist=1, forbidden_zones=forbidden_zones)

            self.environment.spawn_random_static_obstacle(position=position)