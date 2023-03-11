fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]
choice = input()
if choice in fruit:
        print("fruit")
elif choice in vegetable:
        print("vegetable")
else:
        print("unknown")