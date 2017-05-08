import snap

# Load constructed graph
aGraph = snap.LoadEdgeList(snap.PNGraph,"graphs/graphEdges.txt",0,1)

##  Visualization
# Draw the graph
snap.DrawGViz(aGraph, snap.gvlDot, "visuals/theGraph.png", "theGraph")
