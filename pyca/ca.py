import numpy as np

class ElementaryCA():
    def __init__(self, size = 32, ruleset = 110, max_timesteps = 1000, startstate = 'random'):
        self.size = 32
        self.cell_grid = np.zeros((max_timesteps + 1, self.size), dtype=int)
        if startstate == 'random': 
            self.cell_grid[0] =  np.random.randint(2, size=self.size)
        else:
            self.cell_grid[0] = startstate

        self.ruleset = 110
        self.max_timesteps = 1000
     
    def step_ca(self):#, timesteps, width, ruleset, startstate):
        g = self.cell_grid
        W = self.size
        for j in range(timesteps):
            for i in range(self.size):
                setrule = (g[j, (i - 1) % W]) << 2 | \
                          (g[j, i % W]) << 1 | \
                          (g[j, (i + 1) % W])
                next_cell_state = (self.ruleset >> setrule) & 1
                self.cell_grid[j + 1, i] = next_cell_state

            yield self.cell_grid[j + 1]

    @staticmethod
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