import numpy as np

class AdjacencyMatrix:
    def __init__(self, matrix=None, n=1):
        """
        Initializes an adjacency matrix with n vertices
        :param n: the number of vertices
        :param matrix: an n x n matrix to make the adjacency matrix
        """
        if matrix is None:
            self.n = n
            self.matrix = np.zeros((n, n))
        else:
            self.matrix = np.array(matrix)
            self.n = self.matrix.shape[0]

    def addEdge(self, v1, v2):
        """
        Adds an edge between v1 and v2
        :param v1: vertex 1
        :param v2: vertex 2
        """
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        """
        Removes an edge between v1 and v2
        :param v1: vertex 1
        :param v2: vertex 2
        :return:
        """
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0

    def __str__(self):
        """
        Prints the adjacency matrix
        """
        return str(self.matrix)

    def getAdjacentVertices(self, v):
        """
        Returns the adjacent vertices of v
        :param v: The vertex to get the adjacent vertices of
        :return: List of adjacent vertices
        """
        adjacentVertices = []
        for i in range(self.n):
            if self.matrix[v][i] == 1:
                adjacentVertices.append(i)
        return adjacentVertices

    def areConnected(self, v1, v2, numSteps=1):
        """
        Returns true if there is a path between v1 and v2 in numVertices steps. numSteps is defaulted to 1.
        :param v1: vertex 1
        :param v2: vertex 2
        :param numSteps: number of steps to get from v1 to v2
        :return: Boolean giving whether there is a path between v1 and v2
        """

        return self.getStepMatrix(numSteps)[v1][v2] != 0

    def shortestDistance(self, v1, v2):
        """
        Returns the shortest distance between v1 and v2
        :param v1: vertex 1
        :param v2: vertex 2
        :return: Shortest number of steps to get from v1 to v2
        """
        if v1 == v2:
            return 0
        for i in range(1, self.n):
            if self.areConnected(v1, v2, i):
                return i
        return -1


    def numPaths(self, v1, v2, numSteps):
        """
        Returns the number of paths from v1 to v2 when going numSteps steps
        :param v1: vertex 1
        :param v2: vertex 2
        :param numSteps: number of steps
        :return: number of paths
        """
        return self.getStepMatrix(numSteps)[v1][v2]

    def getStepMatrix(self, numSteps):
        return np.linalg.matrix_power(self.matrix, numSteps)


def main():
    print("Adjacency Matrix")


if __name__ == "__main__":
    main()
