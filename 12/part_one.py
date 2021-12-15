#! /usr/bin/env python3

# just cat the input file and pipe it to this program

class PathMap:


    def __init__(self):
        self.array = []
        self.nameToIndex = {}
        self.indexToName = {}

    def addConnection(self, name1, name2):

        if name1 not in self.nameToIndex:
            index1 = max(self.nameToIndex.values())+1 if self.nameToIndex else 0
            self.nameToIndex[name1] = index1
            self.indexToName[index1] = name1
            for line in self.array:
                line.append(False)
            self.array.append([False for i in range(len(self.array)+1)])

        if name2 not in self.nameToIndex:
            index2 = max(self.nameToIndex.values())+1
            self.nameToIndex[name2] = index2
            self.indexToName[index2] = name2
            for line in self.array:
                line.append(False)
            self.array.append([False for i in range(len(self.array)+1)])

        self.array[self.nameToIndex[name1]][self.nameToIndex[name2]] = True
        self.array[self.nameToIndex[name2]][self.nameToIndex[name1]] = True

    
    def getConnections(self, name):
        line = self.array[self.nameToIndex[name]]
        connections = []
        for i, isConnected in enumerate(line):
            if isConnected:
                connections.append(self.indexToName[i])
        return connections
    
    def __str__(self):
        string = ""
        for name1 in self.nameToIndex:
            index1 = self.nameToIndex[name1]
            string += name1 + ": "
            string += ", ".join([name2 for index2, name2 in enumerate(self.nameToIndex) 
                if self.array[index1][index2]])
            string += '\n'
        return string

    
    def __repr__(self):
        return self.__str__()


    def getPaths(self, paths, currentPath = [], visited = []):

        if currentPath:
            currentNode = currentPath[-1]
        else:
            currentNode = 'start'
            currentPath.append(currentNode)
            visited.append(currentNode)

        for connection in self.getConnections(currentNode):
            if connection == 'end':
                currentPath.append('end')
                paths.append(currentPath)
            elif connection not in visited:
                visitedContinued = visited.copy()
                if connection.islower():
                    visitedContinued.append(connection)
                continuedPath = currentPath.copy() + [connection]
                self.getPaths(paths, continuedPath, visitedContinued)
        return paths


if __name__ == '__main__':
    pathMap = PathMap()
    while True:
        try:
            name1, name2 = input().split('-')
            pathMap.addConnection(name1, name2)
        except EOFError:
            break

    print(len(pathMap.getPaths([])))
