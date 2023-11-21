import numpy as np 
import matplotlib.pyplot as plt 

gravitationnal_constant = 6.67430e-11

def evolution_of_position():
    

    for i in range(number_of_star):
        for j in range(number_of_star):
            if i !=  j:
                
                # Define here our relative position vector and the unitary vector to have the correct direction

                vec_r_ji = position[j] - position[i]
                r_ji = norm(r_ji, 2)
                u_ji = vec_r_ji/r_ji

                # Define for each particule j the force that he exerce on particule i

                f_ji = (G * masse[j])/(r_ji**2) * u_ji

            a_i = np.sum(f_ji)


