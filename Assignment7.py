#Q-1
#To Determine the bearing capacity of soil with water table
BulkDensity =float(input("Enter the value of Bulk Density of soil:"))
SatDensity= float(input("Enter the value of Saturated Density of soil:"))
WaterDensity= float(input("Enter the unit Weight of Water:"))
Df= float(input("Enter the value of depth of footing:"))
Dw= float(input("Enter the value of water table above footing level:"))
Dw1= float(input("Enter the value of Water table below the level of footing:"))
B= float(input("Enter the value of width of footing:"))
Nq= float(input("Enter the vaiue of Nq:"))
N= float(input("Enter the value of
N ganna (N):"))
SubDensity=float(input())
print("Submerged Weight of soil is: SubDensity)
#The bearing capacity of soil when water table is at ground
print("CASE A")
qu=(SubDensity*Df*Nq)+(0.5*0.8*B*SubDensity*N)
print("The value of ultimate bearing capacity of soil is:", qu)
#Approximate calculation of Bearing capacity of soil is.
Rw= 0.5+0.5*(Dw/B)
print("The value of Rw is:", Rw)
Rw1=0.5+0.5*(Dw1/8)
print("The value of Rw1 is:", Rw1)
qu=(BulkDensity*Df*Nq*Rw)+ (0.5*0.8*8*BulkDensity*N*Rw1)
print("The value ultimate bearing capacity of soil is:", qu)
# Case B
print("CASE B")
qu=(BulkDensity*Df*Nq)+(0.5*0.8*8*SubDensity)
print("The value of ultimate bearing capacity is:", qu)
Dw= float(input("Enter the value of water table above footing level:"))
Dw1= float(input("Enter the value of Water table below the level of footing:"))
print("The approximate value of ultimate bearing capacity is: ")
Rw=0.5+0.5*(Dw/B)
print("The value of Rw is:", Rw)
Rw1= 0.5+ 0.5* (Dw1/8)
print("The value of Rw1 is:", Rw1)
qu=(BulkDensity*Df*Nq*Rw)+(0.5*0.8*8*BulkDensity*Rw1)
print("The approximate value of ultimate hearing capacity is: ", qu) # Case C
print("CASE C") x = float(input("Enter the value of depth of water below footing:"))
qu=(BulkDensity*Df*Nq)+(0.5*0.8*((BulkDensity*x)+(SubDensity*(B-x)))*N)
print("The value of ultimate bearing capacity is:", qu)
Dw= float(input("Enter the value of water table above footing level:"))
Dw1= float(input("Enter the value of Water table below the level of footing:"))
print("The approximate value of ultimate bearing capacity is:")
Rw= 8.5+ 8.5*(Dw/B)
print("The value of Rw is:", Rw)
Rw1 = 0.5+ 0.5*(Dw1/8)
print("The value of Rwl is: ", Rw1)
qu= (BulkDensity*Df*Nq*Rw)+(0.5*0.8*8*BulkDensity*N*Rw1)
print("the value of ultimate bearing capaciy is:", qu)

#Q-2
#To find the ultimate load carring capacity of pile
UCS= float(input("Enter the value of UCS of soil:"))
Cu = UCS/2 B = float(input("Enter the value of dimension of pile:"))
a=float(input("Enter the length of pile:"))
Alpha =float(input("Enter the value of adhesion factor:"))
Nc=float(input("The value of Nc: "))
Ab=B*B
print("the Base area of footing is:", Ab)
As=4*B*a
print("The value of chohesion of soil is:", Cu)
Qpu=Cu*Nc*Ab
print("'Qpu:", Qpu)
Qf=Alpha*Cu*As
print("Qf:", Qf)
Qu=Qpu+Qf
print("the value of load carring capacity of pile is (Qu):", Qu)

#Q-3 
# To Determine the bearing capacity of soil with water table
BulkDensity= float(input("Enter the value of Bulk Density of soil:"))
SatDensity= float(input("Enter the value of Saturated Density of soil:"))
WaterDensity= float(input("Enter the unit Weight of Water:"))
Df= float(input("Enter the value of depth of footing:"))
B = float (input ("Enter the value of width of footing:"))
Nq = float(input("Enter the value of Ng:"))
N_Gamma= float (input ("Enter the value of
N gamma (N):"))
SubDensity= SatDensity- WaterDensity
print ("Submerged Weight of soil is:", SubDensity) M = int (input("Number of data values of Water table above footing level: "))
N = int (input("Number of data values of Water table below footing level: "))
Dw= []
Dw1 = []
for i in range (1, M+1) :
print ("Enter the value of water table above footing level measured w.r.t. ground (Dw) :")
Depth_Dw= float(input())
Dw.append(Depth_Dw)
Rw =0.5+0.5*(Depth_Dw/B)
print("The value of Rw is:", Rw)
for j in range (1, N+1):
print("Enter the value of water table above footing level measured w.r.t. ground (Dw1): ")
Depth_Dw1= float(input())
Dw.append(Depth_Dw1)
Rw1 =0.5+0.5*(Depth_Dw1/B)
print("The value of Rw1 is:", Rw1)
qu=(BulkDensity*Df*Nq*Rw)+(0.5*0.8*B*BulkDensity*N_Gamma*Rw1)
print ("'qu: ", qu, "kN/m^2")