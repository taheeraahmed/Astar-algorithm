from queue import PriorityQueue
import math
import itertools

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.h_cost = None #the heuristic - estimated distance from current node to end node
        self.g_cost = float("inf") #the distance between the current node and the start node
        self.f_cost = None #the total cost of the node

    def __eq__(self, other):
        return self.position == other.position

def a_star_algorithm(samf, start, end):
    end_node = Node(None, end)
    start_node = Node(None, start)
    
    end_node.g_cost = end_node.f_cost = float("inf")
    end_node.h_cost = 0
    start_node.g_cost = 0
    start_node.h_cost = math.sqrt(((start_node.position[0] - end_node.position[0]) ** 2) + ((start_node.position[1] - end_node.position[1]) ** 2))
    start_node.f_cost = start_node.g_cost + start_node.h_cost
    pathcost = 0 

    open_list = [] #list of nodes available
    closed_list = [] #list of all expanded nodes

    open_list.append(start_node) #first node added to the open list

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        #finding the node in the frontier with lowest f_cost 
        for index, item in enumerate(open_list):
            if item.f_cost < current_node.f_cost:
                current_node = item
                current_index = index

        #move the best node from open_list to closed_list
        open_list.pop(current_index) 
        closed_list.append(current_node)

        #add path if goal is reached
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #returns the path reveresed -> from start_node to end_node

        #generate children
        children = []

        for step in [(0,-1), (0, 1), (-1, 0), (1, 0)]: #the four possible squares nearby a node
            #get the new node position
            new_position = [current_node.position[0] + step[0], current_node.position[1] + step[1]]
            #check that node is inside samf  
            if samf.get_cell_value(new_position) > 0 : 
                #making a new node 
                new_node = Node(current_node, new_position)
                children.append(new_node)

        
        #go through children, calculate their f-values and add them to the open list
        for child in children:

            if child in closed_list: #Don't add child to open list if the note is already in closed
                continue
            
            new_step_cost = samf.get_cell_value(child.position)
            child.g_cost = current_node.g_cost + new_step_cost
            #euclidean distance between the goal position and child position
            child.h_cost = math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))
            child.f_cost = child.g_cost + child.h_cost
            
            

            #want to explore the node with the lowest f-cost
            for openchild in open_list:
                    #if child is in open_list and the g_cost is already lower -> do nothing
                    if openchild == child and openchild.g_cost < child.g_cost:
                        openchild.g_cost = child.g_cost
                        openchild.parent = child.parent
                        continue

            if child not in open_list:
                open_list.append(child)
                
        








    

