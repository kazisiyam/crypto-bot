import numpy as np
import pickle
import random

class QLearningTrader:
    def __init__(self, actions=["buy", "sell", "hold"], learning_rate=0.1, discount_factor=0.95, exploration_rate=1.0):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = {}

    def get_action(self, state):
        """Selects action based on exploration or exploitation."""
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.actions)
        else:
            return self.get_best_action(state)

    def get_best_action(self, state):
        """Returns the best action for a given state."""
        state_key = str(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(len(self.actions))
        return self.actions[np.argmax(self.q_table[state_key])]

    def update_q_table(self, state, action, reward, next_state):
        """Updates Q-table using Bellman Equation."""
        state_key, next_state_key = str(state), str(next_state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(len(self.actions))
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = np.zeros(len(self.actions))

        best_next_action = np.argmax(self.q_table[next_state_key])
        td_target = reward + self.discount_factor * self.q_table[next_state_key][best_next_action]
        td_error = td_target - self.q_table[state_key][self.actions.index(action)]
        self.q_table[state_key][self.actions.index(action)] += self.learning_rate * td_error

    def save_model(self, filename="models/q_learning_model.pkl"):
        """Saves Q-table."""
        with open(filename, "wb") as f:
            pickle.dump(self.q_table, f)

    def load_model(self, filename="models/q_learning_model.pkl"):
        """Loads Q-table."""
        try:
            with open(filename, "rb") as f:
                self.q_table = pickle.load(f)
        except FileNotFoundError:
            pass