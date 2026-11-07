"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    from planning.core import free
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    queue = deque([ctx.start])
    parent = {ctx.start: None}

    while queue:
        current = queue.popleft()

        if current == ctx.goal:
            return reconstruct(parent, current)

        for nxt in ctx.expand(current, len(queue) + 1):
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)

    return []

def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    from planning.core import free
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    stack = [ctx.start]
    parent = {ctx.start: None}

    while stack:
        current = stack.pop()

        if current == ctx.goal:
            return reconstruct(parent, current)

        neighbors = ctx.expand(current, len(stack) + 1)

        for nxt in reversed(neighbors):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)

    return []

def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path.
    """
    from planning.core import free

    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []

    if ctx.start == ctx.goal:
        return [ctx.start]

    max_depth = sum(cell == 0 for row in ctx.grid for cell in row) - 1

    for limit in range(max_depth + 1):
        stack = [(ctx.start, [ctx.start], 0)]
        cutoff = False

        while stack:
            current, path, depth = stack.pop()

            if current == ctx.goal:
                return path

            neighbors = ctx.expand(current, len(stack) + 1)
            valid = [nxt for nxt in neighbors if nxt not in path]

            if depth == limit:
                if valid:
                    cutoff = True
                continue

            for nxt in reversed(valid):
                stack.append((nxt, path + [nxt], depth + 1))

        if not cutoff:
            return []

    return []

def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell)."""
    from planning.core import free
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    heap = []
    parent = {ctx.start: None}
    best_g = {ctx.start: 0}

    heappush(heap, (ctx.heuristic(ctx.start), 0, ctx.start))

    while heap:
        priority, g, current = heappop(heap)

        if g != best_g.get(current):
            continue

        if current == ctx.goal:
            return reconstruct(parent, current)

        for nxt in ctx.expand(current, len(heap) + 1):
            new_g = g + 1

            if new_g < best_g.get(nxt, float("inf")):
                best_g[nxt] = new_g
                parent[nxt] = current

                f = new_g + ctx.heuristic(nxt)
                heappush(heap, (f, new_g, nxt))

    return []
