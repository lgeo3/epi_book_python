
def _construct_maze(n=10, m=10, empty=50):
    """
    :param n: number of line
    :param m: number of column
    :param empty:
    :return:
    """
    import random
    #random.seed(0)  # for reproductability
    maze = []
    for i in range(n):
        maze.append([])
        for j in range(m):
            val = random.choice([True, True, False])
            #print('%s %s  = val is %s' % (i,j, val))
            maze[i].append(val)
            #pass

    maze[n-1][0] = True  # start
    maze[0][m-1] = True  # end


    return maze


def neighbors(x,y, width, height):

    res = []



    if (y - 1) >= 0:
        res.append((x, y-1))

    if (x+1) < width:
        res.append((x+1, y))

    if (x - 1) >= 0:
        res.append((x-1, y))

    if (y+1) < height:
        res.append((x, y+1))


    return res

def find_path_recursive(maze):


    def _helper_find_path(maze, start_coordinate, end_coordinate, already_visited):

        width = len(maze[0])
        height = len(maze)

        for neighbor in neighbors(start_coordinate[0], start_coordinate[1], width, height):
            if neighbor in already_visited:
                continue

            if maze[neighbor[0]][neighbor[1]] is False:
                continue

            if neighbor == end_coordinate:
                return True, [neighbor]

            already_visited.add(neighbor)

            succes, sub_path = _helper_find_path(maze, neighbor, end_coordinate, already_visited)
            if succes:
                return True, [neighbor] + sub_path

        return False, []


    width = len(maze[0])
    height = len(maze)

    end_node_coordinate = (0, width-1)
    start_node_coordinate = (height-1, 0)
    already_visited = set()
    success, path = _helper_find_path(maze, start_node_coordinate, end_node_coordinate, already_visited)
    return path


def find_path(maze):
    visited = set()
    to_visit = []
    current_path = []

    width = len(maze[0])
    height = len(maze)

    end_node_coordinate = (0, width-1)

    to_visit.append((height-1,0))  # adding start

    while to_visit:  # check for emptyness
        current_node = to_visit.pop(-1)


        #print(current_node)
        if maze[current_node[0]][current_node[1]] is False:
            continue


        if current_node in visited:
            continue

        visited.add(current_node)
        current_path.append(current_node)

        if current_node == end_node_coordinate:
            return current_path

        # we need to check neighboord
        new_neighbors = neighbors(current_node[0], current_node[1], width, height)
        to_visit.extend(new_neighbors)
        #for neighbor in new_neighbors:
            #if not(neighbor in visited):
                #to_visit.append(neighbor)
        #to_visit.extend()

    return []

## TODO: do the find_path with a recursive call.. to handle easily deadendcoorridor..

def test():
    maze = _construct_maze()
    import pylab
    import numpy as np

    #path_found =  find_path(maze)
    #pylab.imshow(a, interpolation='None', alpha=0.4)
    #X,Y = zip(*path_found)
    #for i in range(len(path_found)):
    #    pylab.scatter(Y[i], X[i], alpha=float(i)/len(path_found))

    path_found =  find_path_recursive(maze)
    if path_found:
        pylab.imshow(maze, interpolation='None', alpha=0.4)
        X,Y = zip(*path_found)
        for i in range(len(path_found)):
            pylab.scatter(Y[i], X[i], alpha=float(i)/len(path_found))

        pylab.show()


if __name__ == "__main__":
    test()



