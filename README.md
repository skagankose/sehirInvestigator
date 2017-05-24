This Repository contains followings.

  1. directory : dictionaries
  - Saved dictionaries
  - Created via Numpy

  1.1 file : followees.npy : Followee of 142 core users
  1.2 file : followers.npy : Followers of 142 core users

  2. directory : graphs : Pre-constructed graphs
  2.1 file : edgeGraph.txt
  - Each line contains an edge information w/in Sehir network
  - Created via Snap

  3. directory : visuals : Drawings of graphs
  
  4. file : createSave.py
  - Create a graph using the followers and followees stored in dictionaries
  - Save the constructed graph to graphs directory

  5. file : loadVisualize.py
  - Load the pre-contructed graph using createSave.py
  - Visualize it using snap and save to visuals directory

  6. file : exampleDraw.py : Example about using snap for visualization

  7. file : getScores.py
  - A mini application to get real-time information about Twitter users
  - For more information use getScore.py <userName> -help command
