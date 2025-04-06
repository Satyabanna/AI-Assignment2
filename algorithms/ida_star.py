# algorithms/ida_star.py
def heuristic(state, goal, env):
    row_s, col_s = divmod(state, env.ncol)
    row_g, col_g = divmod(goal, env.ncol)
    return abs(row_s - row_g) + abs(col_s - col_g)

def ida_star(env):
    start = env.reset()
    goal = env.goal_state

    def dfs(path, g, threshold):
        node = path[-1]
        f = g + heuristic(node, goal, env)

        if f > threshold:
            return f, None
        if node == goal:
            return f, path

        min_threshold = float("inf")
        for succ, cost in env.get_successors(node):
            if succ not in path:
                new_path = path + [succ]
                temp, result = dfs(new_path, g + cost, threshold)
                if result is not None:
                    return temp, result
                if temp < min_threshold:
                    min_threshold = temp
        return min_threshold, None

    threshold = heuristic(start, goal, env)
    path = [start]
    while True:
        temp, result = dfs(path, 0, threshold)
        if result is not None:
            return result
        if temp == float("inf"):
            return None
        threshold = temp
