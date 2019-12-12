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
from collections import deque

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
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        # print(scores)
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
        newPos = successorGameState.getPacmanPosition()  # Pacman position after moving
        newFood = successorGameState.getFood()  # remaining food
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]  # remain scared

        "*** YOUR CODE HERE ***"
        # if catch by ghost, run away and return -1
        newFood = newFood.asList()
        ghostPos = [(G.getPosition()[0], G.getPosition()[1]) for G in newGhostStates]
        scared = min(newScaredTimes) > 0

        # if not new ScaredTimes new state is ghost: return lowest value

        if not scared and (newPos in ghostPos):
            return -1.0

        if newPos in currentGameState.getFood().asList():
            return 1

        closestFoodDist = sorted(newFood, key=lambda fDist: util.manhattanDistance(fDist, newPos))
        closestGhostDist = sorted(ghostPos, key=lambda gDist: util.manhattanDistance(gDist, newPos))

        fd = lambda fDis: util.manhattanDistance(fDis, newPos)
        gd = lambda gDis: util.manhattanDistance(gDis, newPos)

        return 1.0 / fd(closestFoodDist[0]) - 1.0 / gd(closestGhostDist[0])



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
    """
    Your minimax agent (question 2)
    """

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

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        self.ghost_indexs = [i for i in range(gameState.getNumAgents())][1:]

        best_score, best_action = self.max_v(gameState, 0)
        return best_action

    def min_v(self, state, depth):
        return self.min_v_helper(state, 0, depth)

    def min_v_helper(self, state, pos, depth):
        t = self.judgeState(state, depth)
        if t[0]:
            return t[1], None  # score, action
        if pos >= len(self.ghost_indexs):
            return self.max_v(state, depth+1)

        best_v = 10 ** 8
        best_action = None
        for action in state.getLegalActions(self.ghost_indexs[pos]):
            new_state = state.generateSuccessor(self.ghost_indexs[pos], action)
            tmp_v, tmp_action = self.min_v_helper(new_state, pos+1, depth)
            if tmp_v < best_v:
                best_v = tmp_v
                best_action = action
        return best_v, best_action

    def max_v(self, state, depth):
        t = self.judgeState(state, depth)
        if t[0]:
            return t[1], None  # score, action

        best_v = -10**8
        best_action = None
        for action in state.getLegalActions(self.index):
            new_state = state.generateSuccessor(self.index, action)
            tmp_v, tmp_action = self.min_v(new_state, depth)
            if tmp_v>best_v:
                best_v = tmp_v
                best_action = action
        return best_v, best_action

    def judgeState(self, state, depth):
        if state.isWin() or state.isLose() or depth == self.depth:
            return True, self.evaluationFunction(state)
        else:
            return False, -1

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        self.ghost_indexs = [i for i in range(gameState.getNumAgents())][1:]

        best_score, best_action = self.max_v(gameState, 0, -10**8, 10**8)  # alpha: maximizer, beta: minimizer
        return best_action

    def min_v(self, state, depth, alpha, beta):
        return self.min_v_helper(state, 0, depth, alpha, beta)

    def min_v_helper(self, state, pos, depth, alpha, beta):
        t = self.judgeState(state, depth)
        if t[0]:
            return t[1], None  # score, action
        if pos >= len(self.ghost_indexs):
            return self.max_v(state, depth+1, alpha, beta)

        best_v = 10 ** 8
        best_action = None
        for action in state.getLegalActions(self.ghost_indexs[pos]):
            new_state = state.generateSuccessor(self.ghost_indexs[pos], action)
            tmp_v, tmp_action = self.min_v_helper(new_state, pos+1, depth, alpha, beta)
            if tmp_v < best_v:
                best_v = tmp_v
                best_action = action
            # pruning or update according to the pos
            # if pos == 0:
            #     # max-min
            #     if best_v<alpha:
            #         return best_v, best_action
            # else:
            #     # if there are tow or more ghost
            #     # min-min means not pruning
            #     pass
            if best_v < alpha:
                return best_v, best_action
            beta = min(best_v, beta)

        return best_v, best_action

    def max_v(self, state, depth, alpha, beta):
        t = self.judgeState(state, depth)
        if t[0]:
            return t[1], None  # score, action

        best_v = -10**8
        best_action = None
        for action in state.getLegalActions(self.index):
            new_state = state.generateSuccessor(self.index, action)
            tmp_v, tmp_action = self.min_v(new_state, depth, alpha, beta)
            if tmp_v>best_v:
                best_v = tmp_v
                best_action = action
            # check pruning or update
            if best_v>beta:
                return best_v, best_action
            alpha = max(alpha, best_v)
        return best_v, best_action

    def judgeState(self, state, depth):
        if state.isWin() or state.isLose() or depth == self.depth:
            return True, self.evaluationFunction(state)
        else:
            return False, -1

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
        self.ghost_indexs = [i for i in range(gameState.getNumAgents())][1:]

        best_score, best_action = self.max_v(gameState, 0)
        return best_action

    def expect_v(self, state, depth):
        return self.expect_v_helper(state, 0, depth)

    def expect_v_helper(self, state, pos, depth):
        t = self.judgeState(state, depth)
        if t[0]:
            return t[1], None  # score, action
        if pos >= len(self.ghost_indexs):
            return self.max_v(state, depth+1)

        expect_value = 0
        c = 0
        for action in state.getLegalActions(self.ghost_indexs[pos]):
            new_state = state.generateSuccessor(self.ghost_indexs[pos], action)
            tmp_v, tmp_action = self.expect_v_helper(new_state, pos+1, depth)
            expect_value += tmp_v
            c+=1

        return expect_value/c, None

    def max_v(self, state, depth):
        t = self.judgeState(state, depth)
        if t[0]:
            return t[1], None  # score, action

        best_v = -10**8
        best_action = None
        for action in state.getLegalActions(self.index):
            new_state = state.generateSuccessor(self.index, action)
            tmp_v, tmp_action = self.expect_v(new_state, depth)
            if tmp_v>best_v:
                best_v = tmp_v
                best_action = action
        return best_v, best_action

    def judgeState(self, state, depth):
        if state.isWin() or state.isLose() or depth == self.depth:
            return True, self.evaluationFunction(state)
        else:
            return False, -1

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
