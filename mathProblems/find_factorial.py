#the program for finding factorials

#designed by python

#--- Algorithm ----
#we get the input for the num(integer)
# --- create the function
# 1. declare the function
#   type: recursive function
# 2. iteration: check if the number is evenly divisible starting from 1 to half of the number.
# 3. check: if the number is evenly divisible, store the divisor into an array
# 4. repeat step 2
# 5. output the result
#--- Algorithm Ends ----

print("**** finding the prime factoriels ***")

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


primeFac = findFactorials(num)

print(primeFac)
# input()


