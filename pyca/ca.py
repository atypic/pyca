import numpy as np

class ElementaryCA():
    def __init__(self, size = 32, ruleset = 110, save_timesteps = 1000, startstate = 'random'):
        self.size = size
        self.history = np.zeros((save_timesteps, self.size), dtype=int)
        #self.current_state = np.zeros((save_timesteps + 1, self.size), dtype=int)
        if startstate == 'random': 
            self.current_state =  np.random.randint(2, size=self.size)
        else:
            self.current_state = startstate
        self.history[0] = self.current_state

        self.ruleset = 110
        self.max_save_timesteps = save_timesteps
        self.steps = 0

    def __repr__(self) -> str:
        return f"R {self.ruleset} W  {self.size} CS {self.current_state}"

    def step_ca(self):#, timesteps, width, ruleset, startstate):
        g = self.current_state
        W = self.size
        while True:
            for i in range(self.size):
                setrule = (g[(i - 1) % W]) << 2 | \
                          (g[i % W]) << 1 | \
                          (g[(i + 1) % W])
                next_cell_state = (self.ruleset >> setrule) & 1
                self.current_state[i] = next_cell_state
            
            self.history[self.steps % self.max_save_timesteps] = self.current_state
            self.steps += 1

            yield self.current_state
    
    def get_history(self):
        #build a continous history.
        overflow = self.steps % self.max_save_timesteps
        if overflow > 0:
            return np.concatenate((self.history[overflow:], self.history[:overflow]))
        else:
            return self.history[:self.steps]

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
    ca = ElementaryCA(size=w, ruleset=ca_rule, save_timesteps=10, startstate='random')
    for time, state in enumerate(ca.step_ca()):
        if time > 1000:
            break

    print(ca.get_history())