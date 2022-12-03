# Created by Rohan Reddy
# Updated by Spencer Boggs

#Version with a medium amount of RAM usage

import math
print("")
print("      Welcome to Kinematic")
print("        Equation Solver!")
print("     Created by Rohan Reddy")
print("    Updated by Spencer Boggs")
print("")
print(" Enter any unknown value as u")
print(" Ensure velocities are in m/s,")
print(" acceleration is in m/s^2, time")
print(" is in s, and distance is in m")
print("")
input("    Press [Enter] to Start")
while True:
    print("")
    Vfinal = input("Enter Vfinal (v): ")
    Vinitial = input("Enter Vinitial (v0): ")
    acceleration = input("Enter acceleration (a): ")
    time = input("Enter time (t): ")
    deltaX = input("Enter displacement (x-x0): ")
    print("Enter variable to solve for. ")
    solveFor = input("(v, v0, a, t, x): ")

    #V = v0 + at
    #Requires v0, a, t
    if (solveFor == "v") and (Vinitial != "u") and (acceleration != "u") and (time != "u"):
        Vfinal = float(Vinitial) + (float(acceleration) * float(time))
        print("")
        print("v = " + str(Vfinal) + "m/s")
        print("Equation: v = v0 + at")
        print("v = " + str(Vinitial) + " + " + str(acceleration) + "(" + str(time) + ")")

    #Requires v, a, t
    elif (solveFor == "v0") and (Vfinal != "u") and (acceleration != "u") and (time != "u"):
        Vinitial = float(Vfinal) - (float(acceleration) * float(time))
        print("")
        print("v0 = " + str(Vinitial) + "m/s")
        print("Equation: v = v0 + at")
        print(str(Vfinal) + " = v0 + " + str(acceleration) + "(" + str(time) + ")")

    #Requires v0, v, t
    elif (solveFor == "a") and (Vfinal != "u") and (Vinitial != "u") and (time != "u"):
        acceleration = (float(Vfinal) - float(Vinitial)) / float(time)
        print("")
        print("a = " + str(acceleration) + "m/s^2")
        print("Equation: v = v0 + at")
        print(str(Vfinal) + " = " + str(Vinitial) + " + " + "a" + "(" + str(time) + ")")

    #Requires v0, v, a
    elif (solveFor == "t") and (Vfinal != "u") and (Vinitial != "u") and (acceleration != "u"):
        time = (float(Vfinal) - float(Vinitial)) / float(acceleration)
        print("")
        print("t = " + str(time)+ "s")
        print("Equation: v = v0 + at")
        print(str(Vfinal) + " = " + str(Vinitial) + " + " + str(acceleration) + "(t)")

    #V^2 = v0^2 + 2ax
    #Requires v0, a, x
    elif (solveFor == "v") and (Vinitial != "u") and (acceleration != "u") and (deltaX != "u"):
        Vfinal = math.sqrt(abs(float(Vinitial)**2 + 2 * float(acceleration) * float(deltaX)))
        print("")
        print("v = " + str(Vfinal) + "m/s")
        print("Equation: V^2 = v0^2 + 2ax")
        print("v^2 = " + str(float(Vinitial)**2) + "^2 + (2)" + str(acceleration) + "(" + str(deltaX) + ")" )

    #Requires v0, v, a
    elif (solveFor == "x") and (Vinitial != "u") and (acceleration != "u") and (Vfinal  != "u"):
        deltaX = (float(Vfinal)**2 - float(Vinitial)**2) / (2 * float(acceleration))
        print("")
        print("x = " + str(deltaX)+ "m")
        print("Equation: V^2 = v0^2 + 2ax")
        print(str(float(Vfinal)**2) + " = " + str(float(Vinitial)**2) + "^2 + (2)" + str(acceleration) + "(x)" )

    #Requires v, a, x
    elif (solveFor == "v0") and (deltaX != "u") and (acceleration != "u") and (Vfinal  != "u"):
        Vinitial = math.sqrt(abs(float(Vfinal)**2 - (2 * float(acceleration) * float(deltaX))))
        print("")
        print("v0 = " + str(Vinitial) + "m/s")
        print("Equation: V^2 = v0^2 + 2ax")
        print(str(float(Vfinal)**2) + " = " + "v0^2 + (2)" + str(acceleration) + "(" + str(deltaX) + ")" )

    #Requires v, v0, deltaX
    elif (solveFor == "a") and (deltaX != "u") and (Vinitial != "u") and (Vfinal  != "u"):
        acceleration = (float(Vfinal)**2 - float(Vinitial)**2) / (2 * float(deltaX))
        print("")
        print("a = " + str(acceleration)+ "m/s^2")
        print("Equation: V^2 = v0^2 + 2ax")
        print(str(float(Vfinal)**2) + " = " + str(float(Vinitial)**2) + "^2 + 2a(" + str(deltaX) + ")" )


    #x = v0t + 1/2 * at^2
    #Requires v0, t, a
    elif (solveFor == "x") and (Vinitial != "u") and (acceleration != "u") and (time != "u"):
        deltaX = float(Vinitial) * float(time) + (0.5 * float(acceleration) * float(time)**2)
        print("")
        print("x = " + str(deltaX) + "m")
        print("Equation: x = v0t + 1/2 * at^2")
        print("x = " + str(Vinitial) + " + (1/2)" + str(acceleration) + "(" + str(time) + ")^2" )

    #Requires x, v0, t
    elif (solveFor == "a") and (Vinitial != "u") and (deltaX != "u") and (time != "u"):
        acceleration = (float(deltaX) - float(Vinitial) * float(time)) / (0.5 * float(time)**2)
        print("")
        print("a = " + str(acceleration)+ "m/s^2")
        print("Equation: x = v0t + 1/2 * at^2")
        print(str(deltaX) + " = " + str(Vinitial) + " + (1/2)a(" + str(time) + ")^2" )

    #Requires x, a, t
    elif (solveFor == "v0") and (acceleration != "u") and (deltaX != "u") and (time != "u"):
        Vinitial = (float(deltaX) - 0.5 * float(acceleration) * float(time)**2) / float(time)
        print("")
        print("v0 = " + str(Vinitial) + "m/s")
        print("Equation: x = v0t + 1/2 * at^2")
        print(str(deltaX) + " = v0(" + str(time) + ") + (1/2)" + str(acceleration) + "(" + str(time) + ")^2" )

    #Requires a, v0, x
    elif (solveFor == "t") and (acceleration != "u") and (deltaX != "u") and (Vinitial != "u"):
        a = 0.5 * float(acceleration)
        b = float(Vinitial)
        c = float(deltaX) * -1
        if ((-b + math.sqrt(abs(b**2 - 4 * a * c)))/(2*a)) < 0:
            time = ((-b - math.sqrt(abs(b**2 - 4 * a * c)))/(2*a))
        else:
            time = (-b + math.sqrt(abs(b**2 - 4 * a * c)))/(2*a)
        print("")
        print("t = " + str(time)+ "s")
        print("Equation: x = v0t + 1/2 * at^2")
        print(str(deltaX) + " = " + str(Vinitial) + " + (1/2)" + str(acceleration) + "(t)^2" )


    else:
        print("Unsolvable.")
        print("Double check your inputs.")
