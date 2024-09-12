"""
Maciej Kos
DS 2001 - Assignment 2
Sept 11/12, 2024

Copyright 2024 Maciej Kos

This programming assignment is the intellectual property of Maciej Kos.
All rights reserved.

Students are prohibited from sharing, distributing, or making this assignment publicly
available in any form, including but not limited to posting on public repositories,
forums, or websites. Use of this assignment is restricted to the student it was
provided to for educational purposes only.

Unauthorized sharing or distribution of this assignment may result in academic
penalties and/or disciplinary action as determined by the author or Northeastern University.

Student's first and last name:
Date:
"""

FEE_BASIC = 50
FEE_PREMIUM = 100


def main():
	"""

	░██████╗░██╗░░░██╗███╗░░░███╗
	██╔════╝░╚██╗░██╔╝████╗░████║
	██║░░██╗░░╚████╔╝░██╔████╔██║
	██║░░╚██╗░░╚██╔╝░░██║╚██╔╝██║
	╚██████╔╝░░░██║░░░██║░╚═╝░██║
	░╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝

	███╗░░░███╗███████╗███╗░░░███╗██████╗░███████╗██████╗░░██████╗██╗░░██╗██╗██████╗░
	████╗░████║██╔════╝████╗░████║██╔══██╗██╔════╝██╔══██╗██╔════╝██║░░██║██║██╔══██╗
	██╔████╔██║█████╗░░██╔████╔██║██████╦╝█████╗░░██████╔╝╚█████╗░███████║██║██████╔╝
	██║╚██╔╝██║██╔══╝░░██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗██╔══██║██║██╔═══╝░
	██║░╚═╝░██║███████╗██║░╚═╝░██║██████╦╝███████╗██║░░██║██████╔╝██║░░██║██║██║░░░░░
	╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░

	░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
	██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
	██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
	██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
	╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
	░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝



	Northeastern University wants to develop a new exciting technology: A GYM MEMBERSHIP CALCULATOR! (Woah!)

	Now, you – yes YOU! – will write this fancy piece of tech in Python.

	We are under tight deadlines, so you need to submit it Gradescope BY THE END OF TODAY'S CLASS.

	[ONLY USE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER INSTRUCTIONS, FUNCTIONS, ETC.]

	Q1:
	The Dean of Gyms read that it is important for software to be personalized.
	This means that you have to implement a personalization feature. Your job is to have the calculator ask for the
	user's name and store it in a variable `username`.

	To achieve this feat:
	- use the input() function
	- save the user name in a variable called `username`
	- make sure to ask the user for their username using the input function

	"""

	# Your code goes here.

	"""
	Q2:
	
	The Dean also wants the gym experience to feel welcoming. 
	After all, gyms should be a place where everyone feels great, right?
	
	Your task is to greet the user with a super warm welcome message:
	"Hi [username]! Welcome to the Gym Membership Calculator."
	
	- Use print() to display the message.
	- Personalize it by including the user's name.
	"""

	# Your code goes here.

	"""
	Q3:
	
	Now, it's time for the user to pick a membership type and calculate the monthly membership fee.
	
	The Dean of Gyms insists on keeping things simple, so there are only 2 types of membership: Basic and Premium. Their
	prices are hardcoded and stored in variables FEE_BASIC and FEE_PREMIUM. You can see them at the top of the file.
	
	The code fairy has already written the code for calculating the monthly fee for your. Use it but don't change it.
	
	Here is what to do:
	1. Using the input() function, ask the user the following two questions.      
		- "Would you like to buy the Basic membership? For yes, enter 1. For no, enter 0. Your selection: " 
		- "Would you like to buy the Premium membership? For yes, enter 1. For no, enter 0. Your selection: " 
		(Notes: Yes, it is possible to buy both membership types at once. It is also possible to buy nothing, but don't 
		worry about this and assume the user will always buy at least one membership type.)
	2. Store their answers in appropriately named variables. (Hint: look at the fairy's code.)
	3. Use the fairy's code to calculate the monthly membership fee.
	4. Print the monthly fee.
 
	"""

	# Your code goes here.

	#### BEGIN: Do not edit the following line ####
	membership_fee_monthly = selected_basic * FEE_BASIC + selected_premium * FEE_PREMIUM
	#### END: Do not edit the above line — yours, code fairy!####

	"""
	Q4:
	
	Breaking news! The Dean's assistant says you should apply a **promotional discount** if the user has one.
	
	Here's the plan:
	- Assume only 0%, 13% and 21% discounts are possible. 
	- Ask the user to input the discount percentage, i.e., 
	  "What is your discount percentage? Type 0 for 0%, 13 for 13% off or 21 for 21% off: "
	- Apply the discount to the total monthly fee.
	
	Oh, and the Dean wants us to show off a bit, so we need to calculate not just the monthly fee, 
	but the **annual cost** as well!
	
	Your end goal is to print:
	- the discounted monthly membership fee,
	- the annual cost after the discount (discounted monthly membership fee multiplied by 12)

	Some test cases to help you:
		(1) Basic membership with 13% off:
			pre-discount monthly fee = $50, discounted monthly fee = $43.5, annual cost = $522
		(2) Premium membership with 21% off:
			pre-discount monthly cost = $100, final monthly cost = $79, annual cost = $948
	
	[It is perfectly fine if Python prints out floats (e.g., 79.0) instead of ints (e.g., 79)]
	"""

	# Your code goes here.

	"""
	OPTIONAL 
	
	Q5: 
	
	Oh no, the Dean's office has another request! Actually, it is not that bad. To make the gym (slightly) more 
	affordable, the office wants you to round down the discounted monthly membership fee. Remember that rounding down
	is not the same as rounding. For example, 43.5 is rounded to 44, but 43.5 rounded down is 43.
	
	Compute and print rounded down discounted monthly membership fee.
	
	(Hint: This can be pretty tricky because you can only use operations covered in class. Try those unusual ones. 
	
	There are at least three ways to solve it. (Of course, you only need to solve it one way.)
	- One is very simple (one line of code).
	- One is clever (one line of code) but requires knowing one of the unusual arithmetic operations well.
	- One is straight forward (a few lines of code) but requires knowing another of the unusual arithmetic operations.
	
	Again, just come up with a single solution. 
	)
	
	"""
	# Your code goes here.

	########################################################################
	# Before submitting the assignment:

	# 1) fill out lines 19 and 20
	# 2) are variables named correctly?
	# 3) are all lines of code < 80 characters?
	# 4) do you use comments?
	# 5) are comments above the code they reference, not next to it?
	# 6) are there spaces around items? (e.g., x = y not x=y, and # comment not #comment)
	# 7) are strings enclosed in either double or single quotes, never mixed? (unless nested: "Alex says 'Hi!'" )
	# 8) do you use whitespace to separate code into logical chunks?
	# 9) make sure the file is called assignment2.py
	# 10) close PyCharm, open again, run the whole file and check that everything works correctly

	# Finally, when submitting it to Gradescope, make sure there aren't any errors.

	########################################################################


main()