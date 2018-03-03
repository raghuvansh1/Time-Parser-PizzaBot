
Veg = {"MARGHERITA":200 ,"DOUBLE CHEESE MARGHERITA":250,
       "FARM HOUSE":225,
       "PEPPY PANEER":300,"MEXICAN GREEN WAVE":300,
       "DELUXE VEGGIE":275,
       "5 PEPPER":350,
       "VEG EXTRAVAGANZA":375,
       "CHEESE N CORN":350,"PANEER MAKHANI":425,"VEGGIE PARADISE":450}

Crust = {"new hand tossed":0,"wheat thin rice":50,"cheese burst":99,"fresh pan pizza":35}

Size = {"small":0.8,"medium":1.25,"large":1.5}

Extratopp = {"onion":30,"paneer":30,"black olive":30,"paneer":30,"golden corn":30,"jalapeno":45,
             "red paprika":50,"fresh tomato":25,"crisp capsicum":35,"extracheese":45}

Roll = {"kathi":50,"paneer":30,"masala veggie":40,"masala capsicum":50,"mexican cheese":70,"italian cheese":60}

Multicuisine = {"indian thali":200, "schezwan noodles":150, "fried rice with manchurian":200}

answers = {"yes", "y", "try", "again", "order"}

def pizza_decider():
    ans= 'y'
    while ans in answers:
        print("We have a whole variety of pizzas with us.")
        print("MARGHERITA")
        print("DOUBLE CHEESE MARGHERITA")
        print("PEPPY PANEER")
        print("MEXICAN GREEN WAVE")
        print("DELUXE VEGGIE")
        print("5 PEPPER")
        print("VEG EXTRAVAGANZA")
        print("CHEESE N CORN")
        print("PANEER MAKHANI")
        print("VEGGIE PARADISE")

        response = input("Enter only the name of the pizza you want to order.")
        response = response.upper()

        if response in Veg:
            print("So you have ordered ",response)
            print("We also have various kinds of crusts: ")
            print("Wheat thin rice")
            print("Cheese burst")
            print
        else:
            print("The pizza name you entered cannot be found!")
            ans = input("Do you wish to try again?")

    if ans not in answers:
        food_decider()

def food_decider():
    print("Welcome to the food ordering portal")
    print("So what do you want to order from the following:")
    print("Rolls")
    print("Pizzas")
    print("Multicuisine Dinner")
    print("Sweet Dish")

    response = input()
    resList = response.split()

    num = 0

    while num<len(resList)
