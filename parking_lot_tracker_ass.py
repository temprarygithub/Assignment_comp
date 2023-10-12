class P_Lot:
    def __init__(self):
        self.levels = {
            'A1': {spot: None for spot in range(1, 10)},
            'A2': {spot: None for spot in range(10, 21)}
        }

    def assign_p_space(self, vehicle_num):
        for level, spots in self.levels.items():
            for spot, vehicle in spots.items():
                if vehicle is None:
                    spots[spot] = vehicle_num
                    return {'level': level, 'spot': spot}
        return None  # parking lot is full

    def retrieve_p_spot(self, vehicle_num):
        for level, spots in self.levels.items():
            for spot, vehicle in spots.items():
                if vehicle == vehicle_num:
                    return {'level': level, 'spot': spot}
        return None  # Vehicle not found

def main():
    p_lot_track = P_Lot()

    while True:
        print("\nOptions:")
        print("1. Assign Parking Space")
        print("2. Retrieve Parking Spot")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_num = input("Enter the vehicle num: ")
            result = p_lot_track.assign_p_space(vehicle_num)
            if result:
                print(f"Assigned parking spot: {result['level']} - {result['spot']}")
            else:
                print("Parking lot is full. Unable to assign a spot.")

        elif choice == '2':
            vehicle_num = input("Enter the vehicle num: ")
            result = p_lot_track.retrieve_p_spot(vehicle_num)
            if result:
                print(f"Parking spot for vehicle {vehicle_num}: {result['level']} - {result['spot']}")
            else:
                print(f"Vehicle {vehicle_num} not found in the parking lot.")

        elif choice == '3':
            break

if __name__ == "__main__":
    main()
