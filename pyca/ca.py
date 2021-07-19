import numpy as np

def step_ca(timesteps, width, ruleset, startstate):
    cell_grid = np.zeros((timesteps + 1, width), dtype=int)
    cell_grid[0] = startstate  # np.random.randint(2, size=width)
    g = cell_grid
    W = width
    for j in range(timesteps):
        for i in range(width):
            setrule = (g[j, (i - 1) % W]) << 2 | \
                      (g[j, i % W]) << 1 | \
                      (g[j, (i + 1) % W])
            next_cell_state = (ruleset >> setrule) & 1
            cell_grid[j + 1, i] = next_cell_state

        yield cell_grid[j + 1]

def bool2int(x):
    y = 0
    for i,j in enumerate(x):
        if i == len(x) - 1:
            if j == 1:
                y *= -1
        else:
            y += j<<i
    return int(y)

if __name__ == "__main__":
    initial_state = np.random.randint(0,2,(32,))
    timesteps = 16
    w = len(initial_state)
    t = timesteps
    xint = []
    yint = []
    ca_rule = 142
    for time, state in enumerate(step_ca(t, w, ca_rule, initial_state)):
        x = state[0:int(w/2)]
        y = state[int(w/2):]

        intx = bool2int(x)
        inty = bool2int(y)
        xint.append(intx)
        yint.append(inty)