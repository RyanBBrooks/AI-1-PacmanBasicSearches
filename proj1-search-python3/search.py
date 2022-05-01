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


def basicPush(fringe,curr,path,problem,heuristic):
    """basic enqueue function, helper method for DFS & BFS"""
    fringe.push([curr, path])

def costPush(fringe,curr,path,problem,heuristic):
    """PriorityQueue enqueue function, helper method for A* & UCS"""
    fringe.push([curr, path], problem.getCostOfActions(path) + heuristic(curr[0],problem))


def generalSearch(problem,fringe,enqueue,heuristic):
    """basic search function, helper method for DFS, A*, UCS & BFS"""
    #the closed set of visited states
    closed = set()

    #the start of the problem converted into node format
    startstate = (problem.getStartState(),None)

    #push start, path
    enqueue(fringe,startstate, [], problem, heuristic)

    while (not fringe.isEmpty()):
        node = (fringe.pop()) #item containing parent and path
        path = node[1] #path to this state
        parent = node[0] #item containing state, dir, etc...
        state = parent[0] #the state

        #if we have found the goal
        if(problem.isGoalState(state)):
            #goal pulled off fringe, return the node's path
            return path

        #if the state has not been explored (not in the closed set)
        if(not closed.issuperset({state})):
            #state not expanded, add node's state to closed set, push children
            closed.add(state)
            for child in problem.getSuccessors(state):
                #child contains state, dir, etc...
                #push child, path + child direction
                childpath = path + [child[1]]
                enqueue(fringe, child, childpath, problem, heuristic)

    #no solution
    return []


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #the fringe data structure (implemented as a Stack)
    fringe = util.Stack()
    return generalSearch(problem,fringe,basicPush,None)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #the fringe data structure (implemented as a Queue)
    fringe = util.Queue()
    return generalSearch(problem,fringe,basicPush,None)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #the fringe data structure (implemented as a PriorityQueue)
    fringe = util.PriorityQueue()
    return generalSearch(problem,fringe,costPush,nullHeuristic)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #the fringe data structure (implemented as a PriorityQueue)
    fringe = util.PriorityQueue()
    return generalSearch(problem,fringe,costPush,heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
