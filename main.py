from NumcGUI import runGUI
from Convert import *

def main() -> None:
    print("\n\t+-------------------------+\n\t\tNum-Sys-Conv\n\t+-------------------------+\n")
    print("\t1. Convert to Decimal")
    print("\t2. Convert to None-Decimal") 
    print("\t3. Run GUI")
    print("\n>_ ", end='')
    option = input()
    
    if option in("1", "2") :
        print("\nEnter the number : ", end='')
        number = input()
        print("Enter the base : ", end='')
        base = input()
        
        if option == "1":
            output = Convert.to_decimal_conv(number, base)
        else:
            output = Convert.decimal_conv(number, base)
            
        print(f"\n{output}\n")
        
    elif option == "3":
        runGUI()
    else:
        print("\nError! Invalid Selection\n")
        
if __name__ == '__main__':
    main()