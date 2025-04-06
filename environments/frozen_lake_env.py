import gym

class FrozenLakeWrapper:
    def __init__(self, render_mode=None):
        self.env = gym.make("FrozenLake-v1", is_slippery=False, render_mode=render_mode)
        self.render_mode = render_mode
        self.nrow = self.env.unwrapped.nrow
        self.ncol = self.env.unwrapped.ncol
        self.goal_state = self.nrow * self.ncol - 1  # Bottom-right cell

    def reset(self):
        return self.env.reset()[0]

    def step(self, action):
        return self.env.step(action)

    def get_successors(self, state):
        successors = []
        original_state = self.env.unwrapped.s
        self.env.unwrapped.s = state
        for action in range(self.env.action_space.n):
            obs, reward, done, truncated, info = self.env.step(action)
            successors.append((obs, 1))  # Assume uniform cost = 1
            self.env.unwrapped.s = state  # Reset to original state
        self.env.unwrapped.s = original_state  # Fully restore after loop
        return successors

    def get_neighbors(self, state):
        # Alias for get_successors (used in branch and bound)
        return self.get_successors(state)

    def is_goal(self, state):
        return state == self.goal_state

    def render(self):
        return self.env.render()

    def render_path(self, path):
        # Optional visualization for GIF creation
        self.frames = []
        self.env.reset()
        for state in path:
            self.env.unwrapped.s = state
            frame = self.env.render()
            self.frames.append(frame)
        return self.frames
