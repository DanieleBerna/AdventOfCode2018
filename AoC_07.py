import string

inputFile = list(open('input_d07.txt').readlines())

def CreateGraphFromInstructions (instructions):

    # Creates a dictionary representing the graph of instructions steps

    graph = {}
    for s in instructions:
        stringParts= s.split(' ')
        step = stringParts[1]
        connectedTo = stringParts[7]

        if step in graph:
            graph[step].append(connectedTo)
        else:
            graph[step]=[connectedTo]
    return graph


def GetValuesOccurrences(dictionary):
    valOccurrences = {}
    values = list([elem for x in dictionary.values() for elem in x])
    counters = list([values.count(v) for v in values])
    for elem in list(set(zip(values,counters))):
        valOccurrences[elem[0]]=elem[1]
    return valOccurrences


def FindStartingNode(graph):

    # Find the only node that is not blocked by some else

    freeNodes = list([ startNode for startNode in graph.keys() if startNode not in list(set([elem for x in graph.values() for elem in x])) ])
    freeNodes.sort()
    return freeNodes


def FindPath(graph,start):

    # Find the correct sequences of steps to be done

    occurrences = GetValuesOccurrences(graph)
    availables=start
    path=''

    # While there are steps to be done...
    while len(path)<=len(graph.keys()):

        # appends the step node to the done path...
        path+=availables[0]
        if availables[0] in graph.keys():
            # for each possible next step, adds to availables list only nodes that are not blocked anymore...
            for connected in graph[availables[0]]:
                # Check if connected tasks can be added to the availables list (only if their occurrence counter reaches 0)
                if occurrences[connected]==1:
                    availables.append(connected)
                occurrences[connected] -= 1

            availables.remove(availables[0])
            availables.sort()
    return path


def GetTaskTime(task):
    return ((string.ascii_uppercase.index(task)+1)+60)


def FindPathWithWorkers(graph,start,numWorkers):

    # Find the correct sequences of steps to be done

    availables = start
    path = ''

    workers= list([ ('',0) for i in range(numWorkers)])
    time=0

    occurrences = GetValuesOccurrences(graph)
    while len(path) <= len(graph.keys()):
        for i in range(len(workers)):
            if workers[i][1] > 0:
                workers[i][1] -= 1

            if workers[i][1]==0:
                if workers[i][0]!='':
                    path+=workers[i][0]

                if workers[i][0] in graph.keys():
                    for connected in graph[workers[i][0]]:
                        # Check if connected tasks can be added to the availables list (only if their occurrence counter reaches 0)
                        if occurrences[connected] == 1:
                            availables.append(connected)
                            availables.sort()
                        occurrences[connected] -= 1
                    workers[i][0] = ''

        # Assign availables tasks to workers
        for i in range(len(workers)):
            if len(availables)>=1 and workers[i][1]==0:
                workers[i] = [availables[0],GetTaskTime(availables[0])]
                availables.remove(availables[0])

        time +=1

    return (path,time-1) # time-1 because the while executes one last useless time...

graph = CreateGraphFromInstructions(inputFile)
startNode = FindStartingNode(graph)

print "Part 1 - Steps order: " + FindPath(graph,startNode[:])
print "Part 2 - Total job time with 5 workers: " + str(FindPathWithWorkers(graph,startNode[:],5)[1])

