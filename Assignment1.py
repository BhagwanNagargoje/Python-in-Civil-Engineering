# To find the downstream depth of open channel # Given Data
Q= float(input("Enter the value of Discharge:"))
T= int(input("Enter the value of top width:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
y1= float(input("Enter the value of upstream depth:"))
Z= float(input("Enter the Value of hump:"))
#Dicharge per meter width
q=Q/T
print("The value of discharge per meter width is:", q)
#Area Calculation
A1= T*y1
print("The value of upstream area is:", A1) # Calculation of Froude Number
Fr1
= ((Q*Q*T)/(g*A1* A1 *A1))**0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
print("The flow is Super Critical Flow")
else:
print("The flow is Sub Critical Flow")
#Upstream Energy
E1=(y1+(Q*Q)/(2 *g*A1 *A1))
print("The value of Energy at initial Section is:", E1)
#Downstream Energy
E2=E1
-
Z
print("The value of downstream Energy E2 is:", E2)
#Critical Depth
yc=(q*q/g)**0.3333
print("The Value of critical depth is:", yc)
Ec=1.5*yc
print("The value of critical Energy is:", Ec)
if Ec>E2:
print("Chocking Conditlon")
else:
print ("SAFE")
#Calculation of Zmax
Zmax=E1
-Ec
print("The value of maxinmum hump is:", Zmax)