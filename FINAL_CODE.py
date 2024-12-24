'''
In this code, we have a beam with given loading system(refer the image), we have to 
plot the following graphs using the MATPLOTLIB library:
1. BMD
2. SFD
3. Variation of the support reactions at points A and B

'''
'''
Given data :
The beam is under a uniformly distributed load system, as 20KN/m. 
There is a hinge joint at point A and a roller support at point B.
The external load will be called P, whose location will be decided 
by the input from user i.e. we will plot the above graphs for 
P at the location of user's choice. 
The value of the load P will also be decided by the user.
The length of the beam is 6 metres, with the distance AB as 4m
and BC as 2m.
'''

'''
    now we will have 2 cases:
    Case 1: The load is in between x=0 and x=4 (endpoints not included)
    Case 2: The load is in between x=4 and x=6 (endpoints not included)
    For the endpoints, x=0,4,6, we will have only 2 sections, not 3.
    '''
    

import matplotlib.pyplot as plt
import numpy as np


#take input for the ext load P
print("Given: The length of the beam is 6 metres.")
P=float(input('Enter the value of load:(in KN)'))

#take the location of the load on beam
k=float(input('Give the location of the load (in metres):'))



def section1_shear(x,i):#as the section 1 is same for both cases
    V1= (-20*x)+Ay   
    plt.plot(x,V1,label=f'Section {i}', linewidth=1.5)



def case1_section2_shear(x,i):
    V2= (-20*x) + (Ay-P)
    plt.plot(x,V2, label=f'Section {i}',linewidth=1.5)



def case2_section2_shear(x,i):
    V2= np.full_like(x, Ay+By-80)
    plt.plot(x,V2, label=f'SECTION_{i}',linewidth=1.5)



def section3_shear(x,i):
    V3 = np.zeros_like(x)
    plt.plot(x, V3, label=f'Section {i}',linewidth=1.5)
    

def moment_s1(x,i):
    M1= (-10*(x**2))+ (x*Ay)
    plt.plot(x, M1, label=f'SECTION {i}',linewidth=1.5)
    
    
def c1_moment_s2(x,i):
    M2= (-10*(x**2))+(x*(Ay-P))+(k*P)
    plt.plot(x, M2, label=f'SECTION {i}',linewidth=1.5)
    
    
def c2_moment_s2(x,i):
    M_2=(x)*(Ay+By-80)-(4*By)+160
    plt.plot(x, M_2, label=f'SECTION_{i}',linewidth=1.5)
    
    
def moment_s3(x,i):
    M_3=np.full_like(x, ((k*P)-(4*By)+160))
    plt.plot(x, M_3, label=f'SECTION {i}',linewidth=1.5)
    
    
    
flag=True
if (k<0) or (k>6):
    print("The length of the beam is 6 metres only.")
    flag=False
    


#code for case 1
if (k>0 and k<4):
    i=1
    

    #initialising the support reactions for convenience
    Ay=By=0
    
    #to find the support reactions, we consider ΣM=0 for the whole beam
    #the eqn is (-2*(20*4))+(4*By)+(-k*P)=0
    By= ((k/4)*P)+ 40
    
    #to calculate the other support reaction, we use ΣF=0 for whole beam
    #Ay+By=80+P
    Ay= (80+P-By)
    plt.figure()
        
    #case 1: applied external load is in between x=0 and x=4
    # i.e. 0<k<4 
    #you will have 3 sections
    
    #section 1-1
    #this ranges from x=0 to x=k
    
    x1=np.linspace(0.0, k, 100)
    
    #equation for shear force diagram     
    section1_shear(x1,i)
    i+=1
    #section 2-2
    #ranges from x=0 to x=4
    
    #uncomment later
    x2=np.linspace(k, 4.0, 100)    
    case1_section2_shear(x2,i)
    i+=1

    #section 3-3
    #ranges from x=0 to x=6
    
    x3=np.linspace(4.0, 6.0, 100)
    section3_shear(x3,i)
    
    i=1
    
    
    plt.xlabel('x')
    plt.ylabel('Shear Force')
    plt.title('Shear Force Diagram (SFD)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    
    
    
    plt.figure()
    moment_s1(x1,i)
    i+=1
    c1_moment_s2(x2,i)
    i+=1
    moment_s3(x3,i)
    
    plt.xlabel('X')
    plt.ylabel('Bending moment')
    plt.title('Bending moment diagram')
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    
#case 2 
if (k>4 and k<6):
    i=1
    
    Ay=By=0
    
    By=((k/4)*P)+40
    
    Ay= (80+P-By)
    
    #section 1-1
    
    plt.figure()
    
    x_1=np.linspace(0.0, 4.0, 100)
    '''V1=(-20*x1)+Ay'''
    
    section1_shear(x_1,i)
    i+=1
    #section 2-2

    x_2=np.linspace(4.0,k, 100)
    
    case2_section2_shear(x_2,i)
    i+=1
    
    x_3=np.linspace(k,6.0, 100)
    section3_shear(x_3,i)
    i=1
    
    # moment_s3(x_3)
    plt.xlabel('X')
    plt.ylabel('Shear force')
    plt.title("Shear force diagram")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    # plt.show()
    
    
    plt.figure()
    
    moment_s1(x_1,i)
    i+=1
    c2_moment_s2(x_2,i)
    i+=1
    moment_s3(x_3,i)
    
    plt.xlabel('X')
    plt.ylabel('Bending moment')
    plt.title("Bending moment diagram")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    # plt.show()
    
    
'''handling the edge cases'''
if k==0:
    i=1
    
    #we will have only two sections in this case
    Ay=By=0
    By=((k/4)*P)+40
    Ay= (80+P-By)
    
    
    #first section here
    
    plt.figure()
    
    x0_1=np.linspace(0.0,4.0,100)
    # V_2=(-20*x_2)+(Ay-P)
    
    case1_section2_shear(x0_1,i)
    i+=1
    # c1_moment_s2(x0_1)
   
    #second section here
    
    x0_2=np.linspace(4.0,6.0,100)
    # V_3=np.zeros_like(x_3)
    section3_shear(x0_2,i)
    i=1
    
    
    plt.xlabel('X')
    plt.ylabel('Shear force')
    plt.title("Shear force diagram")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    
    plt.figure()
    
    c1_moment_s2(x0_1,i)
    i+=1
    moment_s3(x0_2,i)
    
    
    plt.xlabel('X')
    plt.ylabel('Bending moment')
    plt.title("BMD")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)

    
if k==4:
    i=1
    #we will have only two sections in this case
    Ay=By=0
    By=((k/4)*P)+40
    Ay= (80+P-By)
    
    #first section here
    
    plt.figure()
    
    x4_1=np.linspace(0.0, 4.0,100)
    # V_1= (-20*x_1)+Ay
    section1_shear(x4_1,i)
    i+=1
   
    #second section here
    
    x4_2=np.linspace(4.0,6.0,100)
    # V_2=np.zeros_like(x_2)
    
    section3_shear(x4_2,i)
    i=1
    
    # moment_s3(x4_2)
    
    plt.xlabel('X')
    plt.ylabel('Shear force')
    plt.title("SFD")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    
    plt.figure()
    
    moment_s1(x4_1,i)
    i+=1
    moment_s3(x4_2,i)
    
    plt.xlabel('X')
    plt.ylabel('Bending moment')
    plt.title("BMD")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    
    
if k==6:
    i=1
    
    Ay=By=0
    By=((k/4)*P)+40
    Ay= (80+P-By)
    
    #first section here
    
    plt.figure()
    
    
    x6_1=np.linspace(0.0,4.0,100)
    # V_1=(-20*x_1)+Ay
    section1_shear(x6_1,i)
    i+=1

    #second section     
    x6_2=np.linspace(4.0,6.0,100)
    
    case2_section2_shear(x6_2,i)
    i=1
    
    
    plt.xlabel('X')
    plt.ylabel('Shear force')
    plt.title("SFD")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    plt.figure()
    
    moment_s1(x6_1,i)
    i+=1
    c2_moment_s2(x6_2,i)
    
    
    plt.xlabel('X')
    plt.ylabel('Bending moment')
    plt.title("BMD")
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.grid(True)


plt.show()

if flag:
    print('Support reaction at A is : Ay=',Ay)
    print("Support reaction at B is : By=",By)