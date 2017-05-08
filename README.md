This Repository contains followings.

  directory : dictionaries : Saved dictionaries
                             Created via Numpy

              file : followees.npy : Followee of 142 core users
              file : followers.npy : Followers of 142 core users

  directory : graphs : Pre-constructed graphs

              file : edgeGraph.txt : Each line contains an edge information w/in Sehir network
                                     Created via Snap

  directory : visuals : Drawings of graphs

  file : createSave.py : Create a graph using the followers and followees stored in dictionaries
                         Save the constructed graph to graphs directory

  file : loadVisualize.py : Load the pre-contructed graph using createSave.py
                            Visualize it using snap and save to visuals directory

  file : exampleDraw.py : Example about using snap for visualization

  file : getScores.py : A mini application to get real-time information about Twitter users
                        For more information use getScore.py <userName> -help command
