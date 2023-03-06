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
