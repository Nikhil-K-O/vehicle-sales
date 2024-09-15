print ("What is your name?")
name=input().strip()

while not name.isalpha():
    print ("I'm pretty sure you can spell your name in alphabets, maybe try again.")
    name=input().strip()

print (f"Hi {name}. Are you doing good today?")
initial_response = input("Please answer Yes or No: ").strip().lower()

while initial_response.lower() not in ['yes', 'no']:
    print ("I'm sorry, I didn't get that, could you repeat that.")
    initial_response = input("Please answer Yes or No: ").strip().lower()

if initial_response == 'yes':
        print ("That's great!")
elif initial_response == 'no':
        print ("Sorry to hear that.")


print ("I actually wanted to ask you about the vehicle you have and want to sell. What vehcile is it again?")
vehicle_type = input().strip()

while not vehicle_type.isalpha():
    print ("I'm sorry, I didn't get that, could you repeat that.")
    vehicle_type = input().strip()

print ("Right right, and the colour?")
vehicle_colour = input().strip()

while not vehicle_colour.isalpha():
    print ("I'm sorry, I didn't get that, could you repeat that.")
    vehicle_colour = input().strip()

print ("And the company was?")
vehicle_company = input().strip()

while not vehicle_company.isalpha():
    print ("I'm sorry, I didn't get that, could you repeat that.")
    vehicle_company = input().strip()

print ("Also which model was it?")
vehicle_model = input().strip()


def describe_vehicle (vehicle_type, vehicle_colour, vehicle_company, vehicle_model):
    print (f"Oh, you have a {vehicle_colour} {vehicle_company} {vehicle_model} {vehicle_type}, that's amazing. Was it worth the price?")
    user_response = input("Please answer Yes or No: ").strip().lower()

    while user_response.lower() not in ['yes', 'no']:
        print ("I'm sorry, I didn't get that, could you repeat that.")
        user_response = input("Please answer Yes or No: ").strip().lower()

    if user_response == 'yes':
                print ("Oh that's great! I'm happy for you.")
    elif user_response == 'no':
                print("Oh is that so, I'm sorry to hear that.")
    print ("What year did you buy it?")
    
    while True:
        try:
            purchase_year = int(input("Enter the year: "))

            if purchase_year < 1885:
                print (f"I don't think {vehicle_type}s were even made back then, could you try again.")
            elif purchase_year > 2024:
                print (f"I don't think your {vehicle_type} is from the future, could you try again.")

            else:
                break

        except ValueError:
            print ("I'm sorry, I didn't get that, could you repeat that.")

    if purchase_year >2019:
                print ("That is quite recent.")
    elif purchase_year >2010:
                print ("Oh that's not that old.")
    elif purchase_year <=2010:
                print ("Oh that's quite an old vehicle you have.")
    print ("Did you have to import it?")
    import_response = input("Please answer Yes or No: ").strip().lower()

    while import_response.lower() not in ['yes', 'no']:
            print ("I'm sorry, I didn't get that, could you repeat that.")
            import_response = input("Please answer Yes or No: ").strip().lower()

    if import_response == 'yes':
                print ("That must have been very expensive.")
                expense_response = input("Please answer Yes or No: ").strip().lower()

                while expense_response.lower() not in ['yes', 'no']:
                    print ("I'm sorry, I didn't get that, could you repeat that.")
                    expense_response = input("Please answer Yes or No: ").strip().lower()

                if expense_response == 'yes':
                    print ("Well I'm glad you could afford it.")
                elif expense_response == 'no':
                    print ("Oh that's good.")
    elif import_response == 'no':
                print ("That must have made it that much more convenient for you.")
                convenience_response = input("Please answer Yes or No: ").strip().lower()

                while convenience_response.lower() not in ['yes', 'no']:
                    print ("I'm sorry, I didn't get that, could you repeat that.")
                    convenience_response = input("Please answer Yes or No: ").strip().lower()

                if convenience_response == 'yes':
                    print ("That's great.")
                elif convenience_response == 'no':
                    print ("That's kinda disappointing though.")
    print (f"Well then, it was nice talking to you {name}, but I'm not really interested in your {vehicle_type}, I was just messing with you. GEEHEEHEE. Ciao.")
describe_vehicle(vehicle_type, vehicle_colour, vehicle_company, vehicle_model)