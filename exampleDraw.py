'''
This example will create following files.
    exampleGraph.png
    exampleGraph.dot
'''

import snap

# Create a graph
exampleGraph = snap.TNGraph.New()

# Add nodes
exampleGraph.AddNode(1)
exampleGraph.AddNode(5)
exampleGraph.AddNode(12)

# Add edges
exampleGraph.AddEdge(1,5)
exampleGraph.AddEdge(5,1)
exampleGraph.AddEdge(5,12)

# Add labels to each node
NIdName = snap.TIntStrH()
NIdName[1] = "1"
NIdName[5] = "5"
NIdName[12] = "12"

# Draw the graph
snap.DrawGViz(exampleGraph, snap.gvlDot, "visuals/exampleGraph.png", "exampleGraph", NIdName)
