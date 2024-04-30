#the program for finding factorials

#designed by python

#--- Algorithm 1 ----
#we get the input for the num(integer)
# --- create the function
# 1. declare the function
#   type: recursive function
# 2. iteration: check if the number is evenly divisible starting from 1 to half of the number.
# 3. check: if the number is evenly divisible, store the divisor into an array
# 4. repeat step 2
# 5. output the result
#--- Algorithm Ends ----

#--- Algorthm 2 ----
# 1. sort the factorial array reverse
# 2. multiply each element 
# 3. print result


print("**** finding the factoriels ***")

num = int(input("Please enter the number? "))
print(f"Girdiğiniz sayı: {num}")
print(num * 2)

primeFac = []

def findFactorials(para1):
    arr1 = []

    for i in range(2, para1+1):
        print(f"sayılar: {i}\n")
        #when we reach the half of the number, stop
        if(i > para1 // 2):
            print("Yarısına ulaşıldı...")
            return arr1
        
        if(para1 % i == 0):
            print(f"tam bölenler: {i}\n")
            arr1.append(i)
        # even divisible check


def multiplyList(list1, list2):
    list3 = []

    for i in range(len(list1)-1):
        list3.append(list1[i] * list2[i])

    return list3


primeFac = findFactorials(num)
print(primeFac)
primeFacReverse = primeFac
primeFacReverse.sort(reverse=True)
print(primeFacReverse, primeFac)
#find the products
def startProgram():
    print(multiplyList(primeFac, primeFacReverse))



