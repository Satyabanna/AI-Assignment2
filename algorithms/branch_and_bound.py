from queue import PriorityQueue
import time

def branch_and_bound(start_state, goal_state, get_successors, is_goal, render_callback=None):
    start_time = time.time()

    visited = set()
    queue = PriorityQueue()
    queue.put((0, [start_state]))  # (cost, path)

    while not queue.empty():
        cost, path = queue.get()
        state = path[-1]

        if state in visited:
            continue

        visited.add(state)

        if is_goal(state):
            if render_callback:
                render_callback()
            print(f"Time Taken: {time.time() - start_time:.4f} seconds")
            return path

        for next_state, step_cost in get_successors(state):
            if next_state not in visited:
                new_path = list(path)
                new_path.append(next_state)
                queue.put((cost + step_cost, new_path))
                if render_callback:
                    render_callback()

    print("No path found.")
    return []
