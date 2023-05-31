name1 = input("Your name: ")
name2 = input("Your lover's name: ")

name1 = name1.lower()
name2 = name2.lower()

combined_name = name1 + name2

T = combined_name.count("t")
R = combined_name.count("r")
U = combined_name.count("u")
E = combined_name.count("e")

TRUE = T+R+U+E

L = combined_name.count("l")
O = combined_name.count("o")
V = combined_name.count("v")
E = combined_name.count("e")

LOVE=L+O+V+E

love_score = int(str(TRUE) + str(LOVE))
print(love_score)

if love_score < 10 or love_score > 85:
  print("Your score is **x**, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 70:
    print(f"Your score is {love_score}, you alright go together")
else:
    print(f"Your score is {love_score}")