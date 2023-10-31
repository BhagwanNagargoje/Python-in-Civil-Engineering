#Q-1
fck= float(input(" Enter the value of characteristic compressive strength:"))
# Experimental Determinations
Gca= float(input ("Enter the value of specific gravity of CA:"))
Gfa= float(input("Enter the value of specific gravity of FA:"))
Gc = float(input("Enter the value of specific gravity of Cement:"))
Water_Density = float(input("Enter the value of Water Density:"))
AGG_Size = float(input("Enter the nominal Size of Aggregate:"))
Nature_of_AGG= input("Nature of Aggregates:")
Slump = float(input("Enter the value of workability of concrete:"))
Admixture= input("Type of Admixture:")
Exposure_Condition = input("Exposure Condition:")
Concreting = input("Type of Concreting:")
Zone = int(input("Zone:")) # Target Mean Strength
sigma= {10:3.5,15:3.5,20: 4,25:4,30: 5,35: 5,40: 5,45: 5,50: 5,55: 5}
ft=fck+sigma[fck]*1.65
print("Target Mean Strength:",ft,"MPa") # Maximum free Water Cement Ratio # Reference IS 456: 2000 Table 5
if(Concreting == "Plain"):
WC_ratio= {"Mild" : 0.6,"Moderate" :0.6,"Severe" :0.5,"Very Severe" :0.45,"Extreme":0.4}
else:
WC_ratio ={"Mild": 0.55,"Moderate":0.5,"Severe" :0.45,"Very Severe" :0.45,"Extreme":0.4}
print("W/C Ratio:",WC_ratio[Exposure_Condition])
WC_ratio= WC_ratio[Exposure_Condition]
# Minimum Cement Content
if(Concreting == "plain"):
Min_Cement_Content= {"Mild":220,"Moderate": 240,"Severe": 250,"Very Severe": 260,"Extreme": 280}
else:
Min_Cement_Content= {"Mild":300,"Moderate": 300,"Severe": 320,
"Very Severe": 340,"Extreme": 360}
print("Minmum Cement Content:", Min_Cement_Content[Exposure_Condition],"kg/m^3") # Water Content
Water_Content={10:208,20:186,40:165}
Water_Content= Water_Content[AGG_Size]
if (Slump == 75):
Water_Content = Water_Content + Water_Content*0.03
elif (Slump == 100):
Water_Content = Water_Content + Water_Content*0.06
elif (Slump == 125):
Water_Content = Water_Content + Water_Content*0.09
elif (Slump == 150):
Water_Content = Water_Content + Water_Content*0.12
elif (Slump == 175):
Water_Content = Water_Content + Water_Content*0.15
elif (Slump == 200):
Water_Content = Water_Content + Water_Content*0.18
if (Nature_of_AGG == "Sub-Angular"):
Water_Content= Water_Content- 10
elif (Nature_of_AGG == "Gravel"):
Water_Content= Water_Content- 20
elif (Nature_of_AGG == "Round"):
Water_Content= Water_Content- 25
if (Admixture == "Plastisizer"):
Water_Content= Water_Content-(0.1*Water_Content)
elif (Admixture=="Super-plastisizer"):
Water_Content= Water_Content-(0.2*Water_Content)
print("Water Content:", Water_Content, "kg/m^3") 
# Cement Content
Cement_Content= Water_Content/WC_ratio
print("CementContent:", Cement_Content, "kg/m^3")
print("As Per IS 456:2000, Maximum allowed Cement Content is 450 kg/m^3")
if (Cement_Content< 450):
Cement_Content= Cement_Content
else:
Cement_Content= 450
if Cement_Content< 450:
print("Safe") # V l C l l ti 
# Volume Calculations
Vol_Cement= Cement_Content/(Gc*Water_Density)
print("Volume of Cemnet:",Vol_Cement,"m^3")
Vol_Water= Water_Content/Water_Density
print("Volume of Water:",Vol_Water,"m^3")
Vol_AGG= 1- Vol_Water-Vol_Cement
print("Volume of Course Aggregates and Fine Aggregates: ",Vol_AGG, "m^3")
Zone_ID ={}
Zone_ID[1]= {10:0.44, 20:0.60, 40:0.69}
Zone_ID[2]={10:0.46, 20:0.62, 40:0.71}
Zone_ID[3]={10:0.48, 20:0.64, 40:0.73}
Zone_ID[4]={10:0.5, 20:0.66, 40:0.75}
Fraction= Zone_ID[Zone] [AGG_Size]
if (WC_ratio==0.5) :
Fraction=Fraction
elif (WC_ratio==0.45):
Fraction=Fraction+(0.01*Fraction)
elif (WC_ratio==0.4):
Fraction=Fraction+(0.02 * Fraction)
elif (WC_ratio==0.55):
Fraction=Fraction-(0.01*Fraction)
elif (WC_ratio==0.60):
Fraction=Fraction-(0.02*Fraction)
print("Course Aggregate fraction:", Fraction)
Vol_CA= Vol_AGG*Fraction
print ("Volume of Course Aggregate:", Vol_CA,"m^3")
Vol_FA= Vol_AGG-Vol_CA
print ("Volume of Fine Aggregate: ", Vol_FA,"m^3")
Mass_CA= Vol_CA*Gca* Water_Density
print ("Mass of Course Aggregates: ", Mass_CA, "Kg/m^3")
Mass_FA= Vol_FA*Gfa*Water_Density
print ("Mass of Fine Aggregates:", Mass_FA, "kg/m^3") # Ratios
print("Weight Batching")
print(Cement_Content/Cement_Content,":", Mass_FA/Cement_Content,":",
Mass_CA/Cement_Content,":",Water_Content/Cement_Content)
print("Volume Batching:")
print(Vol_Cement/Vol_Cement,":",Vol_FA/Vol_Cement,":",Vol_CA/Vol_Cement,":",Vol_Water/Vol_Cement)
