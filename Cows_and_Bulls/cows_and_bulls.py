import random
import time

# Generates the answer to the game
def generate_answer(level):
	answer = random.randint(10**(level-1),10**level-1)
	return answer

# Choose the num of digits
def choose_lvl():
	level = None
	while level is None:
		try:
			level = int(input("Enter the difficulty(Number of digits to play with!) :"))
		except:
			print("Invalid input")
	return level;

def find_cows_and_bulls(answer,guess,length):
	guess = guess;
	answer = answer;
	bulls ,cows = 0 , 0
	
	list1 , list2= [], [];
	for i in range (1,length+1):
		list1.append(answer%10)
		answer //= 10
		list2.append(guess%10)
		guess //= 10
	
	#print(list1,list2)
	
	# find bulls
	list = [] 
	for i in range(length): 
		list.append(list1[i]-list2[i]);
	
	#print(list)
	
	for i in list:
		if i == 0 :
			bulls += 1;
			del list1[list.index(i)]
			del list2[list.index(i)]
	
	
	#print(list1,list2)
	# find cows
	for i in list2 : 
		cows += list1.count(i);
			
	print("Bulls:",bulls,"Cows:",cows)
	print("\n")
	


# Main part
print ("Welcome to the Cows and Bulls Game.\nCan you guess it right??")
time.sleep(0.45)
print ("\n")

while True:
	level  = choose_lvl();
	
	# level == 0 means he doesnt want to play...simple
	if level == 0 :
		print("You will be missed...")
		break;
	
	answer = generate_answer(level)

	print ("Okay let me select my number\nProcessing")


	time.sleep(0.25)
	print(".")
	time.sleep(0.25)
	print(".")
	time.sleep(0.25)
	print(".\n")
	print("Done!!!\nLet's start\n")

	#print(answer);


	# Interactive part
	guess = None
	tries = max(((10**level-1)-(10**(level-1)))//5**level,20);
	print ("You have exactly",tries,"tries left")
	while guess != answer and tries >0 :
		guess = None
		tries -= 1;
		while guess is None:
			try : 
				guess = int(input("Enter your number: "))
			except:
				print("Invalid number\n")
	
		if( 10**(level-1) <= guess <=  10**level-1):
			find_cows_and_bulls(answer,guess,level)
			print("tries left:",tries)
		else:
			print ("Enter a",level,"digit number\n")
			continue;
		
	
	if guess == answer:
		print("YaY you win!!\n");
	else :
		print("Better luck next time!!");
	
	inp = input("Wanna play again??...Press N to quit and any other key to continue: \n")
	if inp == "N" or inp == "n":
		break
	else :
		print("\n")
		continue;
	
