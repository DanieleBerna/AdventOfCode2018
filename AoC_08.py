# Advent of Code 2018 - Day 08

def CreateTree(inputList, index):

    # Recursively build a tree structure while parsing the input list of int values
    # The index argument points to the n-th element of the input list corresponding to the beginning of the node header
    # and it's incremented while parsing the list

    node={'children':[],'metadata':[]}
    numChilds = inputList[index]
    index += 1
    numMetadata = inputList[index]

    if numChilds>0:
        index += 1 # if node has childrens, this index corresponds to the header of the first child
        for i in range(numChilds):
            tempNode, index = CreateTree(inputList,index) # recursive call for childrens creation
            node['children'].append(tempNode)
    else:
        index += 1 # if it hasn't childrens, move to the index of the first metadata

    # after have set up children nodes fill metadata
    for _ in range(numMetadata):
        node['metadata'].append(inputList[index])
        index += 1

    return node,index


def SumNodeData(tree):

    # Recursively gets the sum of all tree metadata

    dataSum = sum( tree['metadata'] )
    for c in tree['children']:
        dataSum += SumNodeData(c)
    return dataSum


def GetNodeValue(tree):

    # Gets the value of the root of a tree

    if len(tree['children'])==0: # if there are no children, simply returns the sum of metadata values
        return sum(tree['metadata'])
    else: # if it has childrens, recursively find their values and add them up
        value=0
        for m in tree['metadata']:
            if m>0: # Skip if metadata value is 0
                try:
                    value += GetNodeValue(tree['children'][m-1]) # Avoid to access non-existing nodes
                except:
                    pass
        return value


#testList=[2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


inputList = []
with open("input_d08.txt", "r") as f:
    fileContent = f.read() # Read all file in case values are not on a single line
    inputList = [ int(x) for x in fileContent.split() ]


root=CreateTree(inputList,0)[0]

print "Part1 - Sum of all metadata entries: " + str(SumNodeData(root))
print "Part2 - Value of root node: " + str(GetNodeValue(root))




