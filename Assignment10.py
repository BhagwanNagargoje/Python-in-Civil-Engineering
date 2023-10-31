#Q-1
# Design of tension member
Tu=float(input("Enter the value of ultimate tensile strength:"))
fy=float(input("Enter the value of yield strength of steel:"))
fu= float(input("Enter the value of ultimate strength of steel:"))
fub=float(input("Enter the value of ultimate strength of bolt:"))
Gamma_mo= float(input("Enter the value of partial factor of safety Garmma mo:"))
Gamma_m1= float(input("Enter the value of partial factor of safety Garmma_m1:"))
Gamma_mb= float(input("Enter the value of partial factor of safety Gamma_mb:"))
print("Gross Area Required")
Agreq=1.1*Tu*1000/fy
print("The value of gross area required is:", 1.2*Agreq)
#Selection of section
#Selecting ISA 100x65x8
Ag= float(input("Enter the value of gross area of steel is:"))
Lcl= float(input("Enter the length of connected leg:"))
Lol= float(input("Enter the length of outstand leg:"))
t= float(input("Entert the value of least thickness: "))
Ag= 1257
#Design of connections
d= float(input("Enter the value of diameter of bolt:"))
do=d+2
print("The diameter of bolt hole is:", do) # As per IS code minimum pitch distance is
pmin =2.5*d
print("The minimum pitch is:", pmin)
#Edge distance as per IS 800 is
e=1.5*do
print("Enter the value of edge distance:", e)
nn=float(input("Number of shear planes with threaded intercepting the shear plane:"))
ns= float(input("Number of shear plane without threads:"))
Anb=0.78*0.7854*d*d
print("threaded area of bolt is:", Anb)
Asb=0.7854*d*d
print("plane shank area of bolt is:", Asb)
Vdsb=(fub/(1.732*Gamma_mb)*(nn*Anb+ns*Asb)*10**-3)
print("The value of Vdsb:", Vdsb)
kb1=e/(3*do)
print("Kb1:", kb1)
kb2=(pmin/(3*do))-0.25
print("Kb2:", kb2)
kb3=fub/fu
print("Kb3:", kb3)
kb4 = 1
print("Kb4:", kb4)
kb= min(kb1,kb2,kb3,kb4)
print("Kb:", kb)
Vdpb=(2.5*kb*d*t*fu*10**-3)/Gamma_mb
print("Vdpb:", Vdpb)
Vd= min(Vdsb ,Vdpb)
print("Vd:", Vd)
N=Tu/Vd
print("Number of bolts requird:", N)
N= float(input("Enter the value of number of bolts:")) # Check for strength # Criteria 1 Yeilding of Gross Section
Tdg=(Ag*fy*10-3)/Gamma_mo
print("The value of tensile strength due to yielding of gross section is:", Tdg) # Criteria 2 Rupture
Anc= (Lcl-(t/2)-do)*t
print("Net Area of Connecting leg is: (Anc):", Anc)
Ago=(Lol-(t/2))*t
print("Gross Area of outstand leg is: (Anc):", Ago)
Lc=(N-1)*pmin
print("Le:", Lc)
bs=(0.6*Lcl)+(Lol*t)
print("bs:", bs)
Beta1=((fu/Gamma_m1)*(fy/Gamma_mo))
print("Beta:1", Beta1)
Beta2=(1.4-(0.076*(fy/fu)*(bs/Lc)*(Lol/t)))
print("Beta:2", Beta2)
Beta=min(Beta1,Beta2)
print("Beta:",Beta)
print("Check 1")
if Beta>1.4:
print("Not Safe")
else: it("Sf")
print("Safe")
print("Check 2")
if Beta<0.7:
print("Not Safe")
else:
print("Safe")
Tdn=((0.9*fu*Anc)/Gamma_m1)+ (Beta*Ago*fy/Gamma_mo)
print("'Tdn:", Tdn) # Criteria 3 Block Shear
Avg=(pmin*(N-1)+e)*t
print("Avg:", Avg)
Avn=((pmin*(N-1) +e)-(N-1)*do+(8.5* do))*t
print("Avn:", Avn)
Atg=0.6*Lcl*t
print("Atg:", Atg)
Atn= Atg*(0.5*do)
print("Atn:", Atn)
Tb1 =((Avg*fy)/(1.732 *Gamma_mo))+((0.9* fu*Atn)/(Gamma_m1))*10**-3
print("Tb1:", Tb1)
Tb2 =((0.9*Avn*fu)/(1.732* Gamma_m1))+((Atg*fy)/(Gamma_mo))*10**-3
print("Tb2:", Tb2)
Tb = min(Tb1, Tb2)
print("Tb", Tb)
Td = min(Tdg,Tb)
print("Td", Td)
if Td>Tu:
print("SAFE")
else:
print("Revise the Section")