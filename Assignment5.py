#Q1
#To find the ultimate moment carring capacity of singly r/f beam
fck= float(input("Enter the value of charateristics compressive strength:"))
fy= float(input("Enter the grade of steel:"))
Es= float(input("Enter the value of Modulus of Elasticity of steel:"))
b = float(input("Enter the value of Width:")) d = float(input("Enter the value of effective depth:"))
d1= float(input("Enter the value of bar diameter (d1):"))
d2= float(input("Enter the value of bar diameter (d2):"))
n=int(input("Enter the number of bars"))
Ast1=(n*0.7854*d1*d1)
Ast2=(n*0.7854*d2*d2)
print("The value of area of steel (Ast1):", Ast1)
print("The vaiue of area of steel (Ast2):", Ast2)
#Total area of steel
Ast=Ast1+Ast2
print("The value of area of steel (Ast):", Ast)
#Neutral Axis Factor
ku= 0.0035/(0.0055+(fy/(1.15*Es)))
print("The value of Neutral axis factor (ku):", ku)
#Momenent of Resistance factor
Ru=0.36*fck*ku*(1-(0.42*ku))
print("The value of Moment of Resistance factor (Ru):", Ru)
#Maximum Neutral Axis:
xumax= ku*d
print("The value of maximum neutral axis (xumax):", xumax)
xu= (0.87*fy*Ast)/(0.36*fck*b)
print ("The value of Actual Neutral Axis (xu):", xu)
if xumax>xu:
print("UNDER REINFORCED")
else:
print("OVER REINFORCED")
#By Comparing X = float(input("Enter the value of Neutral Axis:"))
#Moment of Resistance
Mu=0.36*fck*xu*b*(d-(0.42*xu))*10*-6
print("The value of Moment of Resistance is:", Mu)