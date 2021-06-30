from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import graphviz
import copy


initialState = [[2, 8, 3], 
                [1, 6, 4], 
                [7, 0, 5]]
goalState = [[1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]]
depth = 5
allNodes = []


def Moves(state):
    position = [(index, row.index(0)) for index, row in enumerate(state) if 0 in row]
    # print(position)
    i, j = position[0][0], position[0][1]
    moves = ['up', 'left', 'down', 'right']

    if i == 0:
        moves.remove('up')
    elif i == 2:
        moves.remove('down')
    if j == 0:
        moves.remove('left')
    elif j == 2:
        moves.remove('right')
    # print('moves', moves)
    
    children = []
    for move in moves:
        newState = copy.deepcopy(state)
        if move == 'up':
            # print('up', newState[i][j], newState[i-1][j])
            # print("new", newState)
            newState[i][j], newState[i-1][j] = newState[i-1][j], newState[i][j]
        elif move == 'left':
            # print('left', newState[i][j], newState[i][j-1])
            # print("new", newState)
            newState[i][j], newState[i][j-1] = newState[i][j-1], newState[i][j]
        elif move == 'down':
            newState[i][j], newState[i+1][j] = newState[i+1][j], newState[i][j]
        elif move == 'right':
            newState[i][j], newState[i][j+1] = newState[i][j+1], newState[i][j]
        children.append(newState)
        # print("children", children)
    # print(children)
    return children
    

def FindPath(node):
    path = []
    path.append(node.name)
    while node.parent != None:
        node = node.parent
        path.append(node.name)
    path.reverse()

    print("The path is as follows:")
    for p in path:
        print(p)
    print("\n")


def GenerateTree(node, count):
    if node.name == goalState:
        print("goal reached", node.name, "\n")
        FindPath(node)
        return None
    elif count == depth:
        return None
        
    childNodes = Moves(node.name)

    # for child in childNodes:
    #     childNode.append(Node(child, parent = node))
    #     # Node(child, parent = node)

    # for child in childNode:
    #     GenerateTree(child, count + 1)

    for child in childNodes:
        if child not in allNodes:
            allNodes.append(child)
            GenerateTree(Node(child, parent = node), count + 1)


def main():

    rootNode = Node(initialState)
    allNodes.append(rootNode)
    GenerateTree(rootNode, 0)

    print("The state space tree: \n")
    for pre, fill, node in RenderTree(rootNode):
        print("%s%s" % (pre, node.name))

    DotExporter(rootNode).to_picture("stateSpaceTree.png")


if __name__=='__main__':
    main()
