
import numpy as np
import snap

# Convert given number to 9 Digits
def convert29Digit(number):
    stringNumber = str(number)
    returnNumber = str()
    while len(stringNumber) < 9:
        stringNumber += "0"
    for index in range(9):
        returnNumber += stringNumber[index]
    return int(returnNumber)

# Load followers and followee dictionaries, primarily saved
followerDictionary = np.load('dictionaries/followers.npy').item()
followeeDictionary = np.load('dictionaries/followees.npy').item()

# Initialize an undirected graph
aGraph = snap.TNGraph.New()

# Add Followers to the graph
for userID in followerDictionary:
    user29 = convert29Digit(userID)
    try:
        aGraph.AddNode(user29)
    except:
        pass
    for followerID in followerDictionary[userID]:
        follower29 = convert29Digit(followerID)
        try:
            aGraph.AddNode(follower29)
        except:
            pass
        try:
            aGraph.AddEdge(follower29,user29)
        except:
            pass

# Add Followees to the graph
for userID in followeeDictionary:
    user29 = convert29Digit(userID)
    try:
        aGraph.AddNode(user29)
    except:
        pass
    for followeeID in followerDictionary[userID]:
        followee29 = convert29Digit(followeeID)
        try:
            aGraph.AddNode(followee29)
        except:
            pass
        try:
            aGraph.AddEdge(user29,followee29)
        except:
            pass

'''
# Display information about each node
for aNode in aGraph.Nodes():
    print "node id %d, out-degree %d, in-degree %d" % (aNode.GetId(), aNode.GetOutDeg(), aNode.GetInDeg())
'''

# Save constructed graph
snap.SaveEdgeList(aGraph, "graphs/edgeGraph.txt", "List of edges")

'''
## Future Work
# Develop over the idea:
# Get node higher than degree 1
aSet = set()
for aNode in aGraph.Nodes():
    if aNode.GetOutDeg() > 1 and aNode.GetInDeg() > 1:
        aSet.add(aNode.GetId())
'''
