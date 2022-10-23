import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: number of additional elevators that you can build
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for
                                                                                                             i in
                                                                                                             input().split()]
elevator_locations = dict()
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    if elevator_floor in elevator_locations:
        elevator_locations[elevator_floor].append(elevator_pos)
    else:
        elevator_locations[elevator_floor] = [elevator_pos]

print(f"elevator_locations: {elevator_locations}", file=sys.stderr, flush=True)

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    # Write an action using print
    print(f"({clone_floor},{clone_pos}) - {direction}", file=sys.stderr, flush=True)

    # if clone_floor == -1 and clone_pos == -1:
    #     print("WAIT")

    # Check nearest Exit
    if clone_floor == exit_floor and (clone_pos < exit_pos and direction == "LEFT") or (
            clone_pos > exit_pos and direction == "RIGHT"):
        print("BLOCK")
    elif clone_floor in elevator_locations:  # Check nearest Elevator
        positions = elevator_locations[clone_floor]
        min_distance_from_clone_pos = None
        selected_elevator_position = -1

        for pos in positions:
            distance = abs(clone_pos - pos)
            if min_distance_from_clone_pos is None or min_distance_from_clone_pos > distance:
                min_distance_from_clone_pos = distance
                selected_elevator_position = pos

        if (clone_pos < selected_elevator_position and direction == "LEFT") or (
                clone_pos > selected_elevator_position and direction == "RIGHT"):
            print("BLOCK")
        else:
            print("WAIT")
    elif clone_floor not in elevator_locations and nb_additional_elevators > 0:
        next_floor = clone_floor + 1
        action = str()
        while next_floor < nb_floors:
            if next_floor == exit_floor and clone_pos == exit_pos:
                elevator_locations[clone_floor] = [clone_pos]
                nb_additional_elevators -= 1
                action = "ELEVATOR"
                break
            elif next_floor == exit_floor and (
                    (clone_pos < exit_pos and direction == "LEFT") or (clone_pos > exit_pos and direction == "RIGHT")):
                action = "BLOCK"
                break
            elif next_floor != exit_floor and next_floor in elevator_locations:
                positions = elevator_locations[next_floor]
                min_distance_from_clone_pos = None
                selected_elevator_position = -1
                for pos in positions:
                    distance = abs(clone_pos - pos)
                    if min_distance_from_clone_pos is None or min_distance_from_clone_pos > distance:
                        min_distance_from_clone_pos = distance
                        selected_elevator_position = pos

                if (clone_pos < selected_elevator_position and direction == "LEFT") or (
                        clone_pos > selected_elevator_position and direction == "RIGHT"):
                    action = "BLOCK"
                else:
                    elevator_locations[clone_floor] = [clone_pos]
                    nb_additional_elevators -= 1
                    action = "ELEVATOR"
                break
            next_floor += 1
        print(action if action != "" else "WAIT")
    elif (clone_pos == 0 and direction == "LEFT") or (clone_pos == width - 1 and direction == "RIGHT"):
        # Check left and right wall
        print("BLOCK")
    else:
        print("WAIT")


