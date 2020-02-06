import math
import numpy as np
import random

class Radioactive(object):
    def __init__(self, decay_constant, n):
        self.decay_constant = float(decay_constant)
        outer_list = []
        for i in range(0, n):
            inner_list = []
            for j in range(0, n):
                inner_list.append(1)
            outer_list.append(inner_list)
        #generate the undecayed nuclie
        self.nucler = outer_list
        self.n = int(n)
        self.half_life = math.log(2) / decay_constant  #real half-life
        self.average_lifetime = 1 / decay_constant




        
    def print_nuclei(self):
        for i in range(0, len(self.nucler)):
            for j in range(0, len(self.nucler)):
                print(self.nucler[i][j], end=' ')
            print('\n')
        #output the undecayed nuclie

    def actual_half_life(self):
        return self.half_life
        #accesser to actual half-life

    def decay(self, timestep):
        delta_N = self.n * self.n * np.power(math.e,
                                             (-self.decay_constant * timestep))
        #decayed nuclie number
        probality = delta_N / np.power(self.n, 2)
        for i in range(0, self.n):
            for j in range(0, self.n):
                randomNum = random.random()
                if randomNum > probality:
                    self.nucler[i][j] = 0
        #go over every nucler with probality of decay
        return self

    def sum_nucler(self):
        the_sum = 0
        for i in range(0, self.n):
            the_sum = the_sum + sum(self.nucler[i])
        return the_sum
        #find the sum of undecayed nuclei

    def sim_half_life(self, other):
        c = other
        while True:
            c = other
            i = c.actual_half_life()
            i = i + random.random() - 0.5
            if c.sum_nucler() == c.decay(i).sum_nucler():
                return i
        #apply the sum of actual-half and a random number of time on the undecayed nuclie



n = int(input("input N "))
decay_constant = float(input("input lambda "))
timestep = float(input("input timestep "))
if n < 0 or decay_constant < 0 or timestep < 0:
    print("error, negative input")
#error handling
else:
    a = Radioactive(decay_constant, n)
    print("here is your nucler")
    a.print_nuclei()
    print("actual half life is ", a.actual_half_life())
    print("simulated half life is ",
          a.sim_half_life(Radioactive(decay_constant, n)))
    print("here is your nucler after decay")
    a.decay(timestep).print_nuclei()
    print("initial nuclei number is ", n * n)
    print("final nuclei number is", a.sum_nucler())

# λ=0.02775, N=50, half_life=24.98, timeStep=0.01
