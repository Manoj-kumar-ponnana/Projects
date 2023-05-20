res={}
import math
def getmarks():
    d=int(input("enter description exam marks :"))
    o=int(input("enter Objective(online) marks :"))
    a=int(input("enter Assignment marks :"))
    return d+a+o
n=True
while n>0:
    print("\n"+"*"*50)
    print("\nenter '1' to caluculate average for single subject")
    print("enter '2' to calculate two mids average")
    print("enter '3' to show the saved results")
    print("enter '4' to clear the previous saved results")
    print("enter '0' to exit\n") 
    print("*"*50,"\n")
    n=int(input())
    if n==1:
        sub=input("enter the subject name :")
        print("\nDo you know the total marks(descriptive+Assignment+objective)")
        y=input("enter 'YES' or  'NO' :")
        if y=='NO' or y=='no' or y=='No':
            s1=getmarks()
        else:
            s1=int(input("enter the marks :"))
        c=int(input("enter '1' if u want 80% of the maks or enter '2' if you want 20% of the marks : "))
        if c==1:
            print(f"\n80% of {sub} marks is {math.ceil(s1*0.8)}")
        elif 2 :
            print(f"\n20% of {sub} marks is {math.ceil(s1*0.2)}")
    elif n==2:
        sub=input("enter the subject name :")
        if sub in res.keys():
            print(f"\n{sub} marks are already saved")
            c=input("Do you want to change it (YES/NO) :")
            if c=='YES'or c=='yes' or c=='Yes':
                pass
            elif c=='NO' or c=='no' or c=='No': 
                continue
            pass
        print("\nDo you know the total maks(descriptive+Assignment+objective)")
        x=input("enter 'YES' if u have else enter 'NO' :")
        if x=='YES' or x=='yes' or x=='Yes':
            m1=int(input("enter mid 1 marks :"))
            m2=int(input("enter mid 2 marks :"))
        else:
            for i in range(2):
                if i==0:
                    print(f"enter the MID 1 marks of {sub}")
                    m1=getmarks()
                else:
                    print(f"enter the MID 2 marks of {sub}")
                    m2=getmarks()

        avg=(math.ceil(max(m1,m2)*0.8))+(math.ceil(min(m1,m2)*0.2))
        print(f"\nMID Average of {sub} is {avg}")
        y=input("\nDo you want to store the data (YES or NO) :")
        if y=='YES' or y=='yes':
            res[sub]={"mid 1" : m1,"mid 2" :m2,"average" : avg}
            print("saved successfully!!")
  
        
    elif n==3:
        if len(res)==0:
            print("sorry nothing is saved yet!!")
            continue
        print(f"choose your subject from ",*res.keys(),"\nTo show all subject enter 'all'")
        x=input("choose the subject :")
        
        if x=="all":
            for i in res.keys():
                print(i,"\t: ",end=' ')
                for j in res[i]:
                    print(f"{j} - {res[i][j]}",end='   ')
                print()
        else:
            print(x,"\t: ",end=' ')
            for j in res[x]:
                print(f"{j} - {res[i][j]}",end='   ')
    elif n==4:
        print("Are you sure to delete the saved marks ?")
        y=input("enter (YES/NO) :")
        if y=='YES' or 'yes' or y=='Yes':
            res.clear()
        else:
            continue
    elif n>4:
        print("\nenter numbers mentioned below only")
        
print("\n","*"*15,"THANKYOU FOR USING","*"*15) 
