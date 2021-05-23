from constraint import * 

##  Restriccion del problema (return bool)
def r1(X, Y, Z):
    resp = False
    sumaZ = X + Y
    if Y > X:
        if Z == sumaZ:
            resp = True
    return resp

## Funcion principal
def main():
    csp1 = Problem ()
    csp1.addVariable("x" ,[1 ,2 ,3, 4, 5])
    csp1.addVariable("y" ,[1, 2 ,3, 4, 5 ,6 ,7, 8, 9, 10])
    csp1.addVariable("z" ,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    csp1.addConstraint(r1 ,["x","y","z"])
    solu = csp1.getSolutions()
    print("Asignaciones que resuelven el problema :")
    print(solu)

## El punto de entrada al programa
if __name__ == '__main__':
    main()
