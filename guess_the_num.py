import random
a = -1
n = random.randint(1,10)
guesses = 0

while(a != n):
   a= int(input("Guesse The Number : "))

   if(a < n):
      print("Guesse The High Number.\n")
      
   elif(a > n):
      print("Guesse The Low Number.\n") 

   guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts.\nThank You.")   
print("we're in github")