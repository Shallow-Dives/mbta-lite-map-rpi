from map_controller.controller import MapController

if __name__ == "__main__":
    lite_map = MapController()
    while True:
        print("Running controller")
        lite_map.run_controller()
