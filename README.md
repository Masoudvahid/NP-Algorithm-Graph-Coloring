# NP-algorithm-Graph-Coloring
The problem to find chromatic number of a given graph is NP Complete.  
Actually, there is no efficient algorithm available for coloring a graph with 
minimum number of colors as the problem is a known NP Complete problem
There are approximate algorithms to solve the problem though.

The following pictures will show the concept of graph coloring


***

##Algorithms for coloring a graph
There exists some ways for solving this problem  

###Greedy Algorithm  
even though it doesn’t guarantee to use minimum colors,
but it guarantees an upper bound on the number of colors. 
The basic algorithm never uses more than d+1 colors where d
is the maximum degree of a vertex in the given graph.

###adjacency matrix
***what is adjacency matrix?***  
The Adjacency matrix is a simple and straightforward
way of representing a graph G= (V, E) on n = |V| vertices,
labeled 1, 2, …., n, is by using an n by n matrix.

for example:

<img src="https://miro.medium.com/max/1400/1*NrZ7eQOxHxD5B2Li4Di7AQ.jpeg" width="300">  

***Algorithm***
1. Find all the symmetric edges in one representation of (i, j) and (j, i).
2. Give each vertex one color for initialization.
3. For coloring, visit each vertex and check each adjacent vertice connected 
on that vertex if the color is the same as the current vertex and adjacent 
vertex. If the colors are the same, then change the color.
Like the following picture:
<img src="https://miro.medium.com/max/1400/1*E8XiagfQoD1_Kb2d-bTPSA.jpeg" width="300">  


<!-- https://antiguadominic.medium.com/graph-coloring-adjacency-matrix-discrete-math-problem-8bf98295e0d0 -->