#Q-1
#To determine alkalinity of given sample
H2SO4_req= float(input("Enter the volume ofH2SO4 required in ml:"))
Sample= float(input("Enter the value of sample inlitres:"))
Alkalinity_Removed=H2SO4_req
print("Alkalinity_Removed:", Alkalinity_Removed,"mg")
Alk_mg_per_lit= Alkalinity_Removed/ Sample
print("Total Alkalinity:",Alk_mg_per_lit,"mg/lit")
OH= float (input("Enter the value of OH-Alkalinity present : "))
#Alkalinity removed till pH of 8.3
H2SO4_req= float (input("Enter the volume ofH2S04 required in ml :"))
Alkalinity_Removed = H2SO4_req
print("Alkalinity_Removed: ",Alkalinity_Removed, "mg")
CO3_Combined= Alkalinity_Removed/Sample
print ("Carbonate Alkalinity upto pH8.3:",CO3_Combined, "mgperlit")
CO3=CO3_Combined-OH
print("Carbonate Alkalinity:", CO3,"'mg/lit")
HCO3 =Alk_mg_per_lit- 2*CO3-OH
print("Bicarbonate Alkalinity:", HCO3, "mg/it")