#!/usr/bin/env python3
#import sys
import random

args = ["52", "2", "36", "2", "54", "6"]
int_lst = list(map(int, args))
#print("script name:", sys.argv[0])
print("Arguments:", int_lst)

#print("number of arguments", len(sys.argv))

#
#a = {1, 2, 3, 5, 7, 2}
#b = {2, 3, 4, 5, 6}
#c = {3, 4, 8, 7}
#d = {4, 3, 5, 9, 10}

#print (a | b)   # union → {1, 2, 3, 4}
#print (a & b)  # intersection → {2, 3}
#print (a - b) # difference → {1}
#print (a ^ b)  # symmetric difference (in one but not both) → {1, 4}

#c = set.symmetric_difference(a,b)
#print("c", c)

#lst = [1, 2, 2, 3]
#s = set(lst)
#h = s.pop()

#u = a | b | c | d
#print(u)
#print(c)
#print(u - c)


#achievements = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor','Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer']

#length = len(achievements)

#num = random.randint(3, length)
#num2 = random.randint(3, length)
#num3 = random.randint(3, length)


#print("num:", num)
#print("num:", num2)
#print("num:", num3)
#Alice = set(random.sample(achievements, k=num))
#Bob = set(random.sample(achievements, k=num2))
#Jack = set(random.sample(achievements, k=num3))
#print("ach:", Alice)
#print("ach:", Bob)
#print("ach:", Jack)

#dicts = {"sword" : 65, "shield" : 5}
dicts = {}

value = " sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value"
liste = value.split()
list_of_list = []

for arg in liste:
	lst1 = arg.split(':')
	if len(lst1) != 2:
		print(f"invalid parameter: '{lst1[0]}'")
	else:
		second_list = []
		second_list.append(lst1[0])
		try:
			second_list.append(int(lst1[1]))
		except ValueError as e:
			print("Quantity error for 'key':", e)
		if len(second_list) == 2:
			list_of_list.append(second_list)

d = dict(list_of_list)

print(d)













#a = [["name", 9]]
#b = ["age", 58]

#a.append(b)

#dicts = dict(a)
#print(dicts)

