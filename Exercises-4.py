Q:
    To accept the radius of acircle and to display it circumference , area,volume and surface area


Here's the code

   pi=3.14
radius=float(input("enter the radius of the circle"))
circumference=2*pi*radius
area=pi*radius*radius
volume=4.0/3.0*pi*radius*radius*radius
surfacearea=4*pi*radius*radius
print(f"circumference:{circumference}cms")
print(f"area:{area}sq.cms")
print(f"volume:{volume}cms")
print(f"surface area:{surfacearea} sq.cms")
