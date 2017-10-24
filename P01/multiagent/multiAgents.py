# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
###################################################
#Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4
#--------------------Q4----------------------------
#Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4Q4
###################################################
        numAgents = gameState.getNumAgents()
        def pacMax(gameState, depth):
            legalMoves = gameState.getLegalActions(0)
            if len(legalMoves) == 0 :
                return (self.evaluationFunction(gameState), 0)
            newStates = [gameState.generateSuccessor(0, action) for action in legalMoves]
            scores = [ghostMin(newState, 1, depth - 1) for newState in newStates]
            bestScore = max(scores)
            bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
            chosenIndex = random.choice(bestIndices)
            return (bestScore, chosenIndex)
        def ghostMin(gameState, agentIndex, depth):
            legalMoves = gameState.getLegalActions(agentIndex)
            if len(legalMoves) == 0:
                return self.evaluationFunction(gameState)
            newStates = [gameState.generateSuccessor(agentIndex, action) for action in legalMoves]
            if depth == 1: 
                scores = [self.evaluationFunction(newState) for newState in newStates]
            
            elif not agentIndex == numAgents - 1:
                scores = [ghostMin(gameState, agentIndex + 1, depth - 1) for gameState in newStates]
            else:
                scores = [pacMax(gameState, depth - 1)[0] for gameState in newStates]
            bestScore = min(scores)
            return bestScore
        legalMoves = gameState.getLegalActions(0)
        move = pacMax(gameState, self.depth * numAgents)[1]
        return legalMoves[move]
 
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
#############################################
#Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5
#-------------------Q5-----------------------
#Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5Q5
#############################################
        numAgents = gameState.getNumAgents()
        def pacMax(gameState,alpha,beta,depth):
            legalMoves = gameState.getLegalActions(0)
            if len(legalMoves) == 0 :
                return (self.evaluationFunction(gameState), 0)
            bestScore=-1000
            moves=list(range(len(legalMoves)))
            for i in range(len(legalMoves)):
                action=legalMoves[i]
                newState = gameState.generateSuccessor(0, action) 
                score= ghostMin(newState,1,alpha,beta,depth-1)
                if score>beta:
                    return (score,i)
                if score>bestScore:
                    bestScore=score
                    moves=[i]
                    alpha=max(alpha,score)
                elif score==bestScore:
                    moves+=[i]
            move=random.choice(moves)
            return (bestScore,move)
        def ghostMin(gameState, agentIndex, alpha,beta,depth):
            legalMoves = gameState.getLegalActions(agentIndex)
            if len(legalMoves) == 0:
                return self.evaluationFunction(gameState)
            bestScore=1000
            for action in legalMoves:
                newState = gameState.generateSuccessor(agentIndex,action)
                if depth == 1: 
                    score = self.evaluationFunction(newState)
                elif not agentIndex == numAgents - 1:
                    score = ghostMin(newState, agentIndex+1,alpha,beta,depth-1)
                else:
                    score = pacMax(newState,alpha,beta,depth-1)[0]
                if score<alpha:
                    return score
                if score<bestScore:
                    bestScore=score
                    beta=min(score,beta)
            return bestScore
        legalMoves = gameState.getLegalActions(0)
        move = pacMax(gameState,-1000,1000,self.depth * numAgents)[1]
        return legalMoves[move]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

