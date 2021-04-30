def getDate():
    import datetime
    return datetime.datetime.now()

#Function for exercise
def exercise(exercise_file):
    exercise_name = input("Which Exercise did you complete today ==>>")
    date = getDate()
    fname = open(exercise_file,"a")
    fname.write("\n")
    fname.write("[")
    fname.write(str(date))
    fname.write("]")
    fname.write("\t")
    fname.write(":")
    fname.write("\t")
    fname.write(exercise_name)
    fname.close()
    print("Good job\n")

def show_exercise(exercise_file):
    fname = open(exercise_file)
    show = fname.read()
    print(show)
    fname.close()

def food(food_file):
    print("What did you eat?",food_file[0:7])
    exercise_name = input(">>>")
    date = getDate()
    fname = open(food_file,"a")
    fname.write("List of food that that you eat")
    fname.write("\n")
    fname.write("[")
    fname.write(str(date))
    fname.write("]")
    fname.write("\t")
    fname.write(":")
    fname.write("\t")
    fname.write(exercise_name)
    fname.close()
    print("Please follow the food chart given by gym trainer\n")

def show_food(food_file):
    fname = open(food_file)
    show = fname.read()
    print(show)
    fname.close()

def new_client():
    client_name = input("Please enter your name >>>")
    client_age = input("Please enter your age >>>")
    client_cat = int(input("Please select your choice\n1.Exercise\n2.Food\n>>>"))
    if(client_cat == 1):
        f2 = "exercise.txt"
    if(client_cat == 2):
        f2 = "food.txt"
        f1 = (client_name + f2)
        fname = open(f1,"a")
        date = str(getDate())
        fname.write("This is the information of ")
        fname.write(client_name)
        fname.write("\t\t\t\t\t\t")
        fname.write(date)
        fname.write("\n")
        fname.write("Age : \t")
        fname.write(client_age)
        fname.close()

count = 1
while(count<=50):
    print("Please select your choice ")
    print("1.Exercise")
    print("2.Food")
    print("3.Exit")
    print("4.New admission")
    client_input = int(input(">>>"))

    if(client_input == 1):
        print("Helathify Database")
        print("1.Add Exercise for Muller ")
        print("2.Add Exercise for Daniel ")
        print("3.Add Exercise for Santinel ")
        print("4.Show Exercise for Muller ")
        print("5.Show Exercise for Daniel ")
        print("6.Show Exercise for Santinel")
        print("7.For other")
        c1 = "muller.txt"
        c2 = "daniel.txt"
        c3 = "santinel.txt"
        ch = int(input(">>>"))
        if(ch == 1):
            exercise(c1)
        if(ch == 2):
            exercise(c2)
        if(ch == 3):
            exercise(c3)
        if(ch == 4):
            show_exercise(c1)
        if(ch == 5):
            show_exercise(c2)
        if(ch == 6):
            show_exercise(c3)
        if(ch == 7):
            print("1.Add")
            print("2.Display")
            ch2 = int(input("Please enter your choice >>>"))
            if(ch2 == 1):
                c_name = input("Enter your name>>>")
                c = c_name + "exercise.txt"
                exercise(c)
            if(ch2 == 2):
                c_name = input("Enter your name")
                c = c_name + "exercise.txt"
                show_exercise(c)
    
    if(client_input == 2):
        print("Helathify Database")
        print("1.Add Food for Muller ")
        print("2.Add Food for Daniel ")
        print("3.Add Food for Santinel ")
        print("4.Show Food for Muller ")
        print("5.Show Food for Daniel ")
        print("6.Show Food for Santinel")
        print("7.For other")
        food1 = "mullerf.txt"
        food2 = "danielf.txt"
        food3 = "santinelf.txt"
        ch = int(input("Please enter your choice >>>"))
        if(ch == 1):
            food(food1)
        if(ch == 2):
            food(food2)
        if(ch == 3):
            food(food3)
        if(ch == 4):
            show_food(food1)
        if(ch == 5):
            show_food(food2)
        if(ch == 6):
            show_food(food3)
        if(ch == 7):
            print("1.Add")
            print("2.Display")
            ch2 = int(input("Please enter your choice >>>"))
            if(ch2 == 1):
                c_name = input("Enter your name")
                c = c_name + "f.txt"
                food(c)
            if(ch2 == 2):
                c_name = input("Enter your name")
                c = c_name + "f.txt"
                show_food(c)
            if(ch2 != 1 and ch2 != 2):
                 print("Please enter the correct option")
    
    if(client_input != 1 and client_input != 2 and client_input != 3 and client_input != 4):
        print("Please choose a valid option")
    
    if(client_input == 4):
        new_client()
        print("Thank you for registering with us.... \n")
    if(client_input == 3):
        exit()