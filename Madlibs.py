from tokenize import Name


print("Have you ever played Mad libs before!")
print("Game One")
p1=input("What's your name: ")
Name = input("😏 Give me a Name: ")
Noun = input("Give me a Noun: ")
Noun2 = input("Give me another Noun: ")
Noun3 = input("😅 And another Noun: ")

MadLib = f"On that day, {Name} received a grim reminder. We Lived in fear of the {Noun}, and were \
disgraced to live in these {Noun2} we called {Noun3}. {p1.title()}" 
print(MadLib)

print("Game two")
p2=input("What's your name dear: ")
NOUN = input("You know the drill, a Noun: ")
Verb = input("A verb: ")
Verb1 = input("Another Verb: ")
Verb2 = input("And another Verb: ")

MadLib1 = f"The true measure of a {NOUN} is not how he {Verb} but how he {Verb1}. It's not what they do in life but \
what they did before {Verb2} that proves their worth. {p2.title()}"
print(MadLib1)

