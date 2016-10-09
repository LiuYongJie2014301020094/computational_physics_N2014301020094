import pylab as pl
class uranium_decay:
    def __init__(self, number_of_NA = 100,number_of_NB = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        self.na_uranium = [number_of_NA]
        self.nb_uranium = [number_of_NB]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration//time_step + 1)
        print("Initial number of NA ->", number_of_NA)
        print("Initial number of NB ->", number_of_NB)
        print("Time constant ->", time_constant)       
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmpa = self.na_uranium[i] + (self.nb_uranium[i]-self.na_uranium[i])/self.tau * self.dt
            tmpb = self.nb_uranium[i] + (self.na_uranium[i]-self.nb_uranium[i])/self.tau * self.dt
            self.nb_uranium.append(tmpb)
            self.na_uranium.append(tmpa)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.na_uranium)
        pl.plot(self.t, self.nb_uranium)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.show()

a = uranium_decay()
a.calculate()
a.show_results()
