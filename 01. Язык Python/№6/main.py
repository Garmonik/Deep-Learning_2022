class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.s = 0
        self.x = None

    def forward(self, x):
        self.x = x
        return self.f(sum(list([a*b for a,b in zip(self.x, self.w)])))
        

    def backlog(self):
        return self.x
