# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    ##  run:      python pacman.py -l tinyMaze -p SearchAgent
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    start = problem.getStartState()
    def myDFS(location, res, direction):
        if problem.isGoalState(location):
            return True
        successors = problem.getSuccessors(location)
        for nextLoc in successors:
            pos = nextLoc[0]
            val = pos[0] * 100 + pos[1]
            if val in marked:
                continue
            else:
                marked[val] = 1
            res.append(nextLoc[1])
            if myDFS(pos, res, nextLoc[1]):
                return True

        if direction != None:
            if direction == s:
                res.append(n)
            elif direction == n:
                res.append(s)
            elif direction == e:
                res.append(w)
            else:
                res.append(e)
        return False

    res = []
    marked = {}
    marked[start[0] * 100 + start[1]] = 1
    if myDFS(start, res, None):
           print("reach goal")
    print(res)
    return res
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
################################################################
#Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1
#-----------------------------Q1-------------------------------
#Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1Q1
################################################################
    ##  run: python pacman.py -p SearchAgent -a fn=astar
    
    start=[problem.getStartState(),None,0]
    nextselect=util.PriorityQueue()
    nextselect.push([start,[],0],heuristic(start[0],problem))
    marked=set()
    while not nextselect.isEmpty():
        state=nextselect.pop()
        if(state[0][0] not in marked):
            g=state[2] + state[0][2]
            if state[0][1] is None:
                res=state[1]
            else:
                res=state[1] + [state[0][1]]
            if problem.isGoalState(state[0][0]):
                return res
            successors=problem.getSuccessors(state[0][0])
            for successor in successors:
                f = g+heuristic(successor[0],problem) + successor[2]
                nextselect.push([successor,res,g],f)
            marked.add(state[0][0])
    print "no path"
    return [];

#    util.raiseNotDefined()    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
