import time
import os
from environments.frozen_lake_env import FrozenLakeWrapper
from algorithms.branch_and_bound import branch_and_bound
from algorithms.ida_star import ida_star
from utils.visualize import save_gif

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_branch_and_bound():
    env = FrozenLakeWrapper(render_mode="rgb_array")
    start = env.reset()
    goal = env.goal_state

    def get_successors(state):
        return env.get_successors(state)

    def is_goal(state):
        return state == goal

    start_time = time.time()
    path = branch_and_bound(start, goal, get_successors, is_goal)
    end_time = time.time()

    print(">>\n")
    print(f"Path: {path}")
    print(f"Steps: {len(path)}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")

    frames = env.render_path(path)
    save_gif(frames, RESULTS_DIR, "branch_and_bound.gif")

def run_ida_star():
    env = FrozenLakeWrapper(render_mode="rgb_array")
    start = env.reset()

    start_time = time.time()
    path = ida_star(env)
    end_time = time.time()

    print(">>\n")
    print(f"Path: {path}")
    print(f"Steps: {len(path)}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")

    frames = env.render_path(path)
    save_gif(frames, RESULTS_DIR, "ida_star.gif")

if __name__ == "__main__":
    algo = input("Choose the algorithm to run (bnb / ida): ").strip().lower()

    if algo == "bnb":
        run_branch_and_bound()
    elif algo == "ida":
        run_ida_star()
    else:
        print("Invalid option. Please choose either 'bnb' or 'ida'.")
