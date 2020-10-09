def getMin(aNum,bNum):
    if(aNum<bNum):
        return aNum
    else:
        return bNum

aNum=int(input("Enter First Number: ")) #Get first number and save it in aNum
bNum=int(input("Enter Second Number: ")) #Get Second Number and save it in bNum

print("The Minimum between %d and %d is: %d" %(aNum,bNum,getMin(aNum,bNum)))