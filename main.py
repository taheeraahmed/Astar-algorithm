import Map 
from AStar import a_star_algorithm

def main():

    #Task 1
    # Creating an Object of the Map_Obj class
    map1 = Map.Map_Obj(1)
    path = a_star_algorithm(map1, map1.start_pos, map1.goal_pos)
    #Iterating through every element in the path list
    for i in path:
        map1.replace_map_values(i, -1, map1.goal_pos)
    map1.show_map()

    #Task2
    map2 = Map.Map_Obj(2)
    path2 = a_star_algorithm(map2, map2.start_pos, map2.goal_pos)
    for j in path2:
        map2.replace_map_values(j, -1, map2.goal_pos)
    map2.show_map()

    #Task3
    map3 = Map.Map_Obj(3)
    path3 = a_star_algorithm(map3, map3.start_pos, map3.goal_pos)
    for k in path3:
        map3.replace_map_values(k, -1, map3.goal_pos)
    map3.show_map()
    
    #Task4
    map4 = Map.Map_Obj(4)
    path4 = a_star_algorithm(map4, map4.start_pos, map4.goal_pos)
    for l in path4:
        map4.replace_map_values(l, -1, map4.goal_pos)
    map4.show_map()

main()