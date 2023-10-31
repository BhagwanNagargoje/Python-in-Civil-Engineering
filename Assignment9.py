#Q-1
#To find BOD at 7th day 25C
#To find Decay Coefficient at 25C
K1=float(input("Decay Coefficient:"))
T= int(input("Temperature of 3rd day BOD:"))
T1=int(input("Temperature of 7th day BOD:"))
K2= (K1*(1.047)**(T1-T))
print("The value ofK2 is:", K2)
#To find Ultimate BOD
e=float("2.718")
print("The value ofe is:", e)
B1=float(input("BOD at 3rd day 20c:"))
t=float(input("time in days for finding B1:"))
E=(1-e**(-0.23*t))
print("The value ofE is:", E)l0=(B1/E)
print("The value of 10 is:", l0)
#To find BOD at 7th day 25C
B2= float(input("BoD at 7rd day 25c:"))
t1 =float(input("time in days for findinfB2:"))
E1 =(1-e**(-0.289*t1))
print("The value ofEl is:", E1)
B2= (l0*E1)
print("The value of B2 is:", B2)

#Q-2
#Determination if density of sludge removed from aeration tank
M= float(input("Enter the value of initial mass :"))
S=float(input("Enter the value ofsolid containing sludge inpercentage:"))
Gs= float(input("Enterthe value of Specific gravity ofsludge solid:"))
Rho_W= float(input("Enter the value of density of water:"))
Ws= ((S/M)*100)
m= M- Ws
print("the value ofmass of water", m)
print("The value of Solid Content in sludge", Ws)
Vw =m/Rho_W
print("The Value of Volume", Vw)
Rho_S =Gs*Rho_W
print("The value ofDensity of solid content in sludge", Rho_S)
Vs=(Ws/(Gs*Rho_S))
print("The value of volume of solid content in sludge", Vs)
Vt= Vw+Vs
print("The value of total volume of solid content in sludge", Vt)
Rho_SL= M/Vt
print("The value of Density of sludge removed from aeration", Rho_SL)