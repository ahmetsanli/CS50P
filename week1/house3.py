name = input("What is your name?" )
match name:
    case "harry" | "hermione" | "ron":
        print("gryffiondor")
    case "droco":
        print("slytherin")
    case _:
        print("Who?")