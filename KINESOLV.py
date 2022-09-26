# Created by Rohan Reddy

import math
print("")
print("")
print("")
print("")
print("")
print("Welcome to kinematic")
print("equation solver")
print("Enter any unknown value as u")
print("Ensure that velocities are in m/s, acceleration is in m/s^2, time is in s, and distance is in m")

while True:
    Vfinal = input("Enter Vfinal (v): ")
    Vinitial = input("Enter Vinitial (v0): ")
    acceleration = input("Enter acceleration (a): ")
    time = input("Enter time (t): ")
    deltaX = input("Enter displacement (x-x0): ")
    solveFor = input("Enter variable to solve for (v, v0, a, t, x): ")

    #V = v0 + at
    if (solveFor == "v") and (Vinitial != "u") and (acceleration != "u") and (time != "u"):
        Vfinal = float(Vinitial) + (float(acceleration) * float(time))
        print(str(Vfinal) + "m/s")
    elif (solveFor == "v0") and (Vfinal != "u") and (acceleration != "u") and (time != "u"):
        Vinitial = float(Vfinal) - (float(acceleration) * float(time))
        print(str(Vinitial) + "m/s")
    elif (solveFor == "a") and (Vfinal != "u") and (Vinitial != "u") and (time != "u"):
        acceleration = (float(Vfinal) - float(Vinitial)) / float(time)
        print(str(acceleration) + "m/s^2")
    elif (solveFor == "t") and (Vfinal != "u") and (Vinitial != "u") and (acceleration != "u"):
        time = (float(Vfinal) - float(Vinitial)) / float(acceleration)
        print(str(time)+ "s")
    #V^2 = v0^2 + 2ax
    elif (solveFor == "v") and (Vinitial != "u") and (acceleration != "u") and (deltaX != "u"):
        Vfinal = math.sqrt(float(Vinitial)**2 + 2 * float(acceleration) * float(deltaX))
        print(str(Vfinal) + "m/s")
    elif (solveFor == "x") and (Vinitial != "u") and (acceleration != "u") and (Vfinal  != "u"):
        deltaX = (float(Vfinal)**2 - float(Vinitial)**2) / (2 * float(acceleration))
        print(str(deltaX)+ "m")
    elif (solveFor == "v0") and (deltaX != "u") and (acceleration != "u") and (Vfinal  != "u"):
        Vinitial = math.sqrt(float(Vfinal)**2 - (2 * float(acceleration) * float(deltaX)))
        print(str(Vinitial) + "m/s")
    elif (solveFor == "a") and (deltaX != "u") and (Vinitial != "u") and (Vfinal  != "u"):
        acceleration = (float(Vfinal)**2 - float(Vinitial)**2) / (2 * float(deltaX))
        print(str(acceleration)+ "m/s^2")
    #x = v0t + 1/2 * at^2
    elif (solveFor == "x") and (Vinitial != "u") and (acceleration != "u") and (time != "u"):
        deltaX = float(Vinitial) * float(time) + (0.5 * float(acceleration) * float(time)**2)
        print(str(deltaX)+ "m")
    elif (solveFor == "a") and (Vinitial != "u") and (deltaX != "u") and (time != "u"):
        acceleration = (float(deltaX) - float(Vinitial) * float(time)) / (0.5 * float(time)**2)
        print(str(acceleration)+ "m/s^2")
    elif (solveFor == "v0") and (acceleration != "u") and (deltaX != "u") and (time != "u"):
        Vinitial = (float(deltaX) - 0.5 * float(acceleration) * float(time)**2) / float(time)
        print(str(Vinitial) + "m/s")
    elif (solveFor == "t") and (acceleration != "u") and (deltaX != "u") and (Vinitial != "u"):
        a = 0.5 * float(acceleration)
        b = float(Vinitial)
        c = float(deltaX) * -1
        if ((-b + math.sqrt(b**2 - 4 * a * c))/(2*a)) < 0:
            time = ((-b - math.sqrt(b**2 - 4 * a * c))/(2*a))
        else:
            time = (-b + math.sqrt(b**2 - 4 * a * c))/(2*a)
        print(str(time)+ "s")
    else:
        print("Unsolvable. Double check your inputs.")
