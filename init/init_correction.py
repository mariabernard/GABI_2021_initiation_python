#!/usr/bin/env python3

# simple addition
print(1 + 2)
# 2 cubed
print(2**3)
# simple division
print(17/3)
# concatenation
print("Hello" + " World!")

###################################
# variables are defined by
#   - a name
#   - a value
#   - a type

# remember, print() function is needed in script not in the Console

PRENOM = "Maria"
print(PRENOM)
#   print Maria
print(type(PRENOM))
#   print <class 'str'>

AGE=35
print(AGE)
#   print 35
print(type(AGE))
#   print <class 'int'>

####################################
# List and Dictionnary

SOME_LIST = ["Pierre",44,True]
print(SOME_LIST[0])
#   print Pierre
print(SOME_LIST[-1])
#   print True
print(SOME_LIST[1:3])
#   print [44,True]
print(type(SOME_LIST[1:3]))
#   print <class 'list'>

SOME_DICT = {"prenoms" : ["Pierre", "Paul", "Jacques"], "age":44, "est_permanent" : True}
print(SOME_DICT["prenoms"])
#    print ["Pierre", "Paul", "Jacques"]
print(type(SOME_DICT["prenoms"]))
#   print <class 'list'>
print(SOME_DICT.keys())
#   print dict_keys(['prenoms','age','est_permanent'])
print(SOME_DICT.values())
#   print dict_values([['Pierre', 'Paul', 'Jacques'], 44, True])


####################################
# parse list (or dict) using for loop

#   on a list
SCORES = [1, 0.5, 0.2]
for score in SCORES:
  print(score)
  print(type(score))
  

# 1
# 0.5
# 0.2

# on a Dictionnary
RH_dict = {
'Matricule1':'Maria Bernard',
'Matricule2':'Mathieu Charles'
}
for matricule in RH_dict:
	print(matricule)
	print(RH_dict[matricule])

# Matricule1
# Maria Bernard
# Matricule2
# Mathieu Charles


####################################
# how to express tests

score = 14
if score < 10:
	print("peut mieux faire")
elif score < 20:
	print("bien")
elif score == 20:
	print("parfait")
else:
	print("absent")

# bien

SCORES = [6, 11, 15, 20]
for score in SCORES:
	if score < 10:
		print("peut mieux faire")
	elif score < 20:
		print("bien")
	elif score == 20:
		print("parfait")
	else:
		print("absent")
