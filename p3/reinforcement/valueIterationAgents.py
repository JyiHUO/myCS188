# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections
from collections import Counter

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.runValueIteration()  # for initialization

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        state_store = Counter()
        for i in range(self.iterations):
            for state in self.mdp.getStates():
                v_l = []
                # print("state:******* ", state)
                for action in self.mdp.getPossibleActions(state):
                    v_l.append(self.computeQValueFromValues(state, action))
                if len(v_l) != 0:
                    state_store[state] = max(v_l)
            # update
            for state in self.mdp.getStates():
                self.values[state] = state_store[state]

    def getValue(self, state):
        """
        each state is a tuple, like (0, 0), (1, 1)
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        q_res = 0
        for next_state, prob in self.mdp.getTransitionStatesAndProbs(state=state, action=action):
            reward = self.mdp.getReward(state, action, next_state)
            # print(next_state)
            # print(self.values[next_state])
            # print("next_state: ", next_state, " prob: ", prob, "reward: ", reward, "value: ", self.values[next_state])
            q_res += prob*( reward + self.discount*self.values[next_state] )
        return q_res

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        best_action = None
        best_res = -1 * 10**8
        for action in self.mdp.getPossibleActions(state):
            res = self.computeQValueFromValues(state, action)
            if res > best_res:
                best_res = res
                best_action = action
        return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        states = self.mdp.getStates()
        for i in range(self.iterations):
            state = states[i % len(states)]
            if self.mdp.isTerminal(state):
                continue
            v_l = []
            for action in self.mdp.getPossibleActions(state):
                v_l.append(self.computeQValueFromValues(state, action))
            if len(v_l) != 0:
                self.values[state] = max(v_l)


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"

        # compute predecessors
        predecessors = dict()  # cur_state: {pre1, pre2}
        state_q = dict()  # state: best_q
        pri = util.PriorityQueue()

        for state in self.mdp.getStates():
            if self.mdp.isTerminal(state):
                continue
            for action in self.mdp.getPossibleActions(state):
                for next_state, _ in self.mdp.getTransitionStatesAndProbs(state=state, action=action):
                    if not (next_state in predecessors):
                        predecessors[next_state] = set()
                    predecessors[next_state].add(state)

        # initialization
        for state in self.mdp.getStates():
            if self.mdp.isTerminal(state):
                continue
            best_action = self.computeActionFromValues(state)
            best_q = self.computeQValueFromValues(state=state, action=best_action)
            diff = abs(best_q - self.getValue(state))
            pri.push( state, -diff)
            state_q[state] = best_q

        # asynchronous update
        for i in range(self.iterations):
            if len(pri.heap) == 0:
                break
            state = pri.pop() # debug here
            self.values[state] = state_q[state]
            # update pre state priority
            for pre_state in predecessors[state]:
                if self.mdp.isTerminal(pre_state):
                    continue
                best_action = self.computeActionFromValues(pre_state)
                best_q = self.computeQValueFromValues(state=pre_state, action=best_action)
                diff = abs(best_q - self.getValue(pre_state))
                if diff > self.theta:
                    # pri.update(pre_state, -diff)
                    # state_q[pre_state] = best_q
                    # print(state_q)
                    # with higher priority
                    if abs(state_q[pre_state] - self.values[pre_state]) < diff:
                        pri.update( pre_state, -diff)
                        state_q[pre_state] = best_q



