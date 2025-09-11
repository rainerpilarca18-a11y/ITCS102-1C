print("Welcome to the Manga Recommender")
genre = input("What genre do you prefer?(action, romance, horror) ")

if genre == "action":
	duration = input("How long?(short, medium, long) ")
	if duration == "short":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: Jujutsu Kaisen")
		elif decades == "2000s":
			print("we recommend: Bleach")
		else:
			print("invalid")
			
	elif duration == "medium":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: My Hero Academia")
		elif decades == "2000s":
			print("we recommend: Naruto")
		else:
			print("invalid")
			
	elif duration == "long":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: we are still short on the list")
		elif decades == "2000s":
			print("we recommend: One Piece")
		else:
			print("invalid")

elif genre == "romance":
	duration = input("How long?(short, medium, long) ")
	if duration == "short":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: Rent a Girlfriend")
		elif decades == "2000s":
			print("we recommend: Darling in the Franxx")
		else:
			print("invalid")
			
	elif duration == "medium":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: My Dress Up-Darling")
		elif decades == "2000s":
			print("we recommend: Ranma 1/2")
		else:
			print("invalid")
			
	elif duration == "long":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: we are still short on the list")
		elif decades == "2000s":
			print("we recommend: we are still short on the list")
		else:
			print("invalid")
			
elif genre == "horror":
	duration = input("How long?(short, medium, long) ")
	if duration == "short":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: Gleipner")
		elif decades == "2000s":
			print("we recommend: Akame Ga Kill")
		else:
			print("invalid")
			
	elif duration == "medium":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: Attack on Titan")
		elif decades == "2000s":
			print("we recommend: Deathnote")
		else:
			print("invalid")
			
	elif duration == "long":
		decades = input("what decade?(2000s, 2010s) ")
		if decades == "2010s":
			print("we recommend: we are still short on the list")
		elif decades == "2000s":
			print("we recommend: we are still short on the list")
		else:
			print("invalid")

else:
	print("invalid")