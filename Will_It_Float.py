
a = 1000

if  __name__ == "__main__":

    object = input("What are we putting in the water?")

    weight = float(input("what is the weight of the object?"))

    volume = float(input("Wha is the volume of the object?"))

    b = (weight / volume)

    if (a < b):
        print(object,"will sink.")

    elif(a > b):
        print(object,"will float.")

    else:
        print(object,"has neutral buoyancy.")







    













    
        


