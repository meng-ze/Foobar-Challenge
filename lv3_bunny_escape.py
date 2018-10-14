# 
# Prepare the Bunnies' Escape
# ===========================

# You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, 
# but oncethey're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape 
# ipods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and deadends that will 
# be a deathtrap for the escaping bunnies. Fortunately, CommanderLambda has put you in charge of a remodeling project that 
# will give you theopportunity to make things a little easier for the bunnies. Unfortunately(again), you can't just remove 
# all obstacles between the bunnies and the escapepods - at most you can remove one wall per escape pod path, both to 
# maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

# You have maps of parts of the space station, each starting at a prison exit andending at the door to an escape pod. 
# The map is represented as a matrix of 0sand 1s, where 0s are passable space and 1s are impassable walls. The door outof
#  the prison is at the top left (0,0) and the door into an escape pod is atthe bottom right (w-1,h-1). 

# Write a function answer(map) that generates the length of the shortest pathfrom the prison door to the escape pod, 
# where you are allowed to remove onewall as part of your remodeling plans. The path length is the total number of nodes 
# you pass through, counting both the entrance and exit nodes. The startingand ending positions are always passable (0). 
# The map will always be solvable,though you may or may not need to remove a wall. The height and width of themap can be 
# from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

# Test cases
# ==========
# Inputs:
#     (int) maze = [[0, 1, 1, 0], 
#                   [0, 0, 0, 1], 
#                   [1, 1, 0, 0], 
#                   [1, 1, 1, 0]]
# Output:
#     (int) 7

# Inputs:
#     (int) maze = [
# [0, 0, 0, 0, 0, 0], 
# [1, 1, 1, 1, 1, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1], 
# [0, 0, 0, 0, 0, 0]]
# Output:
#     (int) 11

def bfs(maze, input_row, input_col):
    has_break_wall = False

    queue = [[input_row, input_col, has_break_wall, 1]]
    while len(queue) != 0:
        coord_row, coord_col, has_break_wall, step = queue.pop(0)

        if coord_row == len(maze)-1 and coord_col == len(maze[0])-1:
            return step

        if maze[coord_row][coord_col] != 0:
            if maze[coord_row][coord_col] == 1 and has_break_wall == False:
                has_break_wall = True
            else:
                continue
        maze[coord_row][coord_col] = -1

        if coord_row > 0:
            queue.append([coord_row-1, coord_col, has_break_wall, step+1])
        if coord_row < len(maze)-1:
            queue.append([coord_row+1, coord_col, has_break_wall, step+1])
        if coord_col > 0:
            queue.append([coord_row, coord_col-1, has_break_wall, step+1])
        if coord_col < len(maze[0])-1:
            queue.append([coord_row, coord_col+1, has_break_wall, step+1])

    return -1
    
def main():
    maze = [[0, 1, 1, 0], [0, 0, 0,1], [1, 1, 0, 0], [1, 1, 1, 0]]
    maze2 = [[0, 0, 0, 0, 0, 0], [1,1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0,0, 0, 0, 0, 0]]
    maze3 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(bfs(maze, 0, 0))
    print(bfs(maze2, 0, 0))
    print(bfs(maze3, 0, 0))

if __name__ == '__main__':
    main()
