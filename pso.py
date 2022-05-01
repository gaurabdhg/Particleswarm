from random import random,uniform

class Particle:
    def __init__(self, x0y0):
        self.pos_i=[]          # particle position
        self.vel_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual

        for i in range(0,dims):
            self.vel_i.append(uniform(-1,1))
            self.pos_i.append(x0y0[i])

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.pos_i)

        # check to see if the current position is an individual best
        if self.err_i<self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.pos_i.copy()
            self.err_best_i=self.err_i
                    
    # update new particle velocity
    def update_vel(self,pos_best_g):
        w=0.5       # constant inertia weight (how much to weigh the previous velocity)
        c1=1        # personal/individual constant
        c2=2        # social constant
        
        for i in range(0,dims):
            r1=random()
            r2=random()
            
            vel_pers=c1*r1*(self.pos_best_i[i]-self.pos_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.pos_i[i])
            self.vel_i[i]=w*self.vel_i[i]+vel_pers+vel_social

    # update the particle position based off new velocity updates
    def update_pos(self,bounds):
        for i in range(0,dims):
            self.pos_i[i]=self.pos_i[i]+self.vel_i[i]
            
            # adjust maximum position if necessary
            if self.pos_i[i]>bounds[i][1]:
                self.pos_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.pos_i[i]<bounds[i][0]:
                self.pos_i[i]=bounds[i][0]

def sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total
        
def minimize(costFunc, x0y0, bounds, pnos, maxiter, verbose=False):
    global dims

    dims=len(x0y0)
    err_best_g=-1                   # best error for group
    pos_best_g=[]                   # best position for group

    # establish the swarm
    swarm=[]
    for i in range(0,pnos):
        swarm.append(Particle(x0y0))

    # begin optimization loop
    i=0
    while i<maxiter:
        if verbose: 
            print(f'iter: {i:>4d}, best solution: {err_best_g:10.6f}')
            
        # cycle through particles in swarm and evaluate fitness
        for j in range(0,pnos):
            swarm[j].evaluate(costFunc)

            # determine if current particle is the best (globally)
            if swarm[j].err_i<err_best_g or err_best_g==-1:
                pos_best_g=list(swarm[j].pos_i)
                err_best_g=float(swarm[j].err_i)
        
        # cycle through swarm and update velocities and position
        for j in range(0,pnos):
            swarm[j].update_vel(pos_best_g)
            swarm[j].update_pos(bounds)
        i+=1

    # print final results
    if verbose:
        print('\nFINAL SOLUTION:')
        print(f'   > {pos_best_g}')
        print(f'   > {err_best_g}\n')

    return err_best_g, pos_best_g


if __name__=="__main__":
    x0y0=[5,5]
    bounds=[(-10,10),(-10,10)]
    minimize(sphere, x0y0, bounds, pnos=15, maxiter=30, verbose=True)
