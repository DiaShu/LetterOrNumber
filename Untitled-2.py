Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CapitalLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ans = input("Please enter either a single letter, or add a single digit number: ")

if ans in Letters or ans in CapitalLetters:
    print("you entered a letter")
else:
    print("you didn't enter a letter")