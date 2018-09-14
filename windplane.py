import math as m


def windplane(v1, v2):
    #v1 = windspeed, v2= airspeed

    # vi describes the sum of the i components, using x = rcos(theta).
    # vj describes the sum of the j components, using y = rsin(theta).
    vi = (v1 * m.cos(m.pi/4)) + (v2 * m.cos(m.pi/6))
    vj = (-v1 * m.sin (m.pi/4)) + (v2 * m.sin(m.pi/6))

    #distance formula
    vmag = m.sqrt((m.pow(vi,2) + m.pow(vj,2)))


    #arctan to find angle, and converstion to degrees
    theta = m.atan(vj/vi)
    theta_d = m.degrees(theta)

    #theta is N_E, Not E_N, so you need to do 90-theta.
    NE = (90 - theta_d)

    print('Ground Speed: ', vmag)
    print('Angle:', NE)
   
    return

windplane(60,300)
