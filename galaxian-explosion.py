import numpy as np 
import matplotlib.pyplot as plt 

gravitationnal_constant = 6.67430e-11



# ______                                      _                                                 _                    
# |  ___|                                    | |                                               | |                   
# | |_ _   _ _ __   ___   _ __ __ _ _ __   __| | ___  _ __ ___    _ __   ___  ___    __   _____| |     __ _  ___ ___ 
# |  _| | | | '_ \ / __| | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \  | '_ \ / _ \/ __|   \ \ / / _ \ |    / _` |/ __/ __|
# | | | |_| | | | | (__  | | | (_| | | | | (_| | (_) | | | | | | | |_) | (_) \__ \_   \ V /  __/ |_  | (_| | (_| (__ 
# \_|  \__,_|_| |_|\___| |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_| | .__/ \___/|___( )   \_/ \___|_( )  \__,_|\___\___|
#                                                                | |             |/              |/                  
#                                                                |_|                                                 



def velocity_of_star(i, number_of_star, position, masse, dt, v_i):
    vec_rji = []
    r_ji = []
    u_ji = []
    f_ji = []

    for j in range(number_of_star):
        if i != j:
            vec_rji.append(position[j] - position[i])
            r_ji.append(norm(vec_rji[j], 2))
            u_ji.append((vec_rji[j])/(r_ji[j]))

            f_ji.append(gravitationnal_constant * masse[j] * u_ji[j]/r_ji[j])

    a_i = sum(f_ji)
    v_i += v_i + dt * a_i
    return v_i    


def evolution_of_position():

    for i in range(number_of_star):

        


# funcanimation.
