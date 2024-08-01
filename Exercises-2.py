Q: To accept the length,breadth,height  of a ractangular boxand to display its volume,perimetr and volume.
 

here's the code

print("enter the dimension of box")
length=float(input("enter the length"))
breadth=float(input("enter the breadth"))
height=float(input("enter the height"))
volume=length*breadth*height
area=length*breadth
perimeter=2*(length+breadth)
print("volume of the box is ",volume,"cubic meter")
print(f"area:{area}")
print(f"perimeter:{perimeter}")
