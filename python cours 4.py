import matplotlib.pyplot as plt
import numpy as np

def exo3():
    n = int(input('nombre a entrer'))
    x = np.linspace(0,4,500)
    y=np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
    plt.plot(x,y)
    plt.show()

def exo2():
    nb=int(input("nombre de point"))
    x = np.linspace(-1,1,nb)
    y = np.cos(2*np.pi*x)
    plt.plot(x,y)
    plt.show()

def exo3():
    n = 200
    ar=[]
    while type(n) == int:
        n = input('veuillez entrer la valeure de la temperature en kelvin')
        try :
            n = int(n)
            ar.append(n)
        except:
            n=''
        
    for i in ar:
        x = np.linspace(2,10,500)
        y = (0.08206*i)/x
        plt.plot(x,y)
        plt.xlabel('Molar volume (L/mol)')
        plt.ylabel('Pressure level (Pa)')
        plt.title('isotherm ideal gas')
    plt.show()

def exo4():
    xo = float(input("Enter the value of X0"))
    s = float(input("Enter the value of s"))
    x = np.linspace(-1,1,500)
    y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*np.power((x-xo),2)/np.power(s,2))
    plt.plot(x,y)
    plt.title("Gaussian function")
    plt.show()

def exo5():
    x = np.linspace(0,3,500)
    y = np.exp(-x)
    y1 = np.sin(3*np.pi*x)*np.exp(-x)
    plt.plot(x,y,label ="e^(-x)" )
    plt.plot(x,y1,label="sin(3*pi*x)*e^(-x)" )
    plt.title("comparison")
    plt.legend()
    plt.show()

def exo6():
    n = 200
    ar=[]
    while type(n) == int:
        n = input('veuillez entrer la valeure de la temperature en kelvin')
        try :
            n = int(n)
            ar.append(n)
        except:
            n=''
    for i in ar:
        x = np.linspace(2,10,500)
        y = y = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*np.power((x-xo),2)/np.power(s,2))
        plt.plot(x,y)
    plt.show()

exo6()