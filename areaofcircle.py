def findArea(r): 
    PI = 3.142
    return PI * (r*r); 
  
# Driver method
num=float(input("Enter r value:"))
print("Area is %.6f" % findArea(num)); 



# Python program to accept a file name 
fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])

