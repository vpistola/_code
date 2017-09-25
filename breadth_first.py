from collections import deque # Doubly-ended queue: pop from left, append to right.

def breadth_first(start, goal, neighbors):
    "Find a shortest sequence of states from start to the goal."
    frontier = deque([start]) # A queue of states
    previous = {start: None}  # start has no previous state; other states will
    while frontier:
        s = frontier.popleft()
        if s == goal:
            return path(previous, s)
        for s2 in neighbors[s]:
            if s2 not in previous:
                frontier.append(s2)
                previous[s2] = s
                
def path(previous, s): 
    "Return a list of states that lead to state s, according to the previous dict."
    return [] if (s is None) else path(previous, previous[s]) + [s]

