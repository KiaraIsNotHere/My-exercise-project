import random
import string
import time
import requests
listee = [
        "1.Madlibs",
        "2.Simple calculator",
        "3.Weight converter",
        "4.Temperature converter",
        "5.Time Countdown",
        "6.Shopping cart",
        "7.Quiz game",
        "8.Number Guessing",
        "9.Rock Paper Scissors",
        "10.Dice roller",
        "11.Bank program",
        "12.Slot",
        "13.Encryption",
        "14.Hangman Game",
        "15.Roman to numeric",
        "16.Pokemon Info",
        "17.Email Slicer",
        "18.Compund Interest Calculator",
        "19.Concession Stand",
        "20.Credit Card Validator"]
for item in listee:
    print(item)

def madlibs():
    print("***** Madlibs Game *****")
    tempat1 = input("nama tempat: ")
    benda1 = input("nama benda: ")
    sifat1 = input("nama sifat (benda1): ")
    ekspresi1 = input("ekspresi: ")

    print(" ")
    print(f"hari ini saya pergi ke {tempat1}")
    print(f"saya melihat {benda1}")
    print(f"{benda1} itu sangat {sifat1}")
    print(f"saya sangat {ekspresi1}")

def simpleCalculator():
    print("***** Simple Calculator *****")
    try:
        num1 = int(input("enter first number: "))
        op = input("enter the operator (+ - * /): ")
        num2 = int(input("enter second number: "))
        if op == '+':
            result = num1 + num2
            print(f"the result of {num1} {op} {num2} = {result:.2f}")
        elif op == '-':
            result = num1 - num2
            print(f"the result of {num1} {op} {num2} = {result:.2f}")
        elif op == '*':
            result = num1 * num2
            print(f"the result of {num1} {op} {num2} = {result:.2f}")
        elif op == '/':
            result = num1 / num2
            print(f"the result of {num1} {op} {num2} = {result:.2f}")
        else:
            print(f"{op} is not an operator")
    except ValueError:
        print("you cant enter a 'string' to 'num1' or 'num2' ")

def weightConverter():
    print("***** Weight converter *****")
    tipe = input("what weight currently in (kg/lbs): ")
    berat = int(input("Enter your weight: "))

    if tipe == 'kg':
        berat = berat  * 2.205
        tipe = "lbs"
        print(f"your weight is: {berat} {tipe}")
    elif tipe == 'lbs':
        berat = berat / 2.205
        tipe = "kg"
        print(f"your weight is: {berat} {tipe}")
    else:
        print(f"{tipe} is invalid input")

def temperatureConversion():
    unit = input("what temperature is this (C/F): ")
    temp = float(input("input temperature: "))

    if unit == "c":
        temp = round((9 * temp) / 5 + 32, 1 )
        print(f"the temperature in Fahreinheit is: {temp} °F")
    elif unit == "f":
        temp = round((temp - 32) * 5 / 9, 1 )
        print(f"the temperature in celcius is: {temp} °c")
    else:
        print(f"{unit} is not a valid input")

def timeCountDown():
    print("****** Time CountDown ******")
    timeIn = int(input("enter time in second: "))

    for x in range(timeIn,0,-1):
        detik = x % 60
        menit = int(x / 60 ) % 60
        jam = int(x / 3600)
        print(f"{jam:02}:{menit:02}:{detik:02}")
        time.sleep(1)

    print("wake up")

def shoppingCart():
    print("***** Shopping cart *****")
    price = []
    basket = []
    total = 0

    while True:
        baskets = input("enter a food (q to quit): ")
        if baskets.lower() == 'q':
            break
        else:
            harga = float(input(f"Enter the {baskets} price: "))
            basket.append(baskets)
            price.append(harga)

    print("***** Your Cart *****")
    for x in basket:
        print(x,end=" ")

    for x in price:
        total += x
    print()
    print(f"Here is your total: {total}")

def quizGame():
    print("***** Quiz Game *****")
    pertanyaan =   ("pick from 1 - 10",
                "how many alphabet are there",
                "can fish sleep",
                "Cs:Go or Valorant",
                "what is the biggest animal ever lived")

    opsi = (("A. 1 ", "B. 5", "C. 6", "D. 7"),
            ("A. 26", "B. 24", "C. 22", "D. 27"),
            ("A. Yes", "B.No", "C. Yeah, i guess", "D. Impassible"),
            ("A.Cs lah ", "B. no idea", "C. neither", "D. valo dongs"),
            ("A. Ur mom", "B. T-REX", "C. whale", "D. kontortus dikkus"))
    jawaban = ("B","A","C","B","A")
    tebakan = []
    skor = 0
    num_question = 0

    for t in pertanyaan:
        print("*********************")
        print(t)
        for x in opsi[num_question]:
                print(x)
        tebagan = input("Enter the answer: ").upper()
        tebakan.append(tebagan)   
        if tebagan == jawaban[num_question]:
                skor += 1
                print("correct")
        else:
                print("incorrect")
                print(f"the right answer is {jawaban[num_question]}")
            

        num_question += 1
    
    print("+++++++++++++++++++++++++++")
    print("         RESULT            ")
    print("+++++++++++++++++++++++++++")


    print("Answer: ",end="")
    for j in jawaban:
            print(j, end=" ")
    print()

    print("tebakan: ",end="")
    for z in tebakan:
            print(z, end=" ")
    print()

    skor = int(skor / len(pertanyaan) * 100 )
    print(f"Ur score is: {skor} %")

def numberGuessing():
    print("***** Number Guessing game *****")
    runnin = True
    while runnin:
        low = int(input("Enter the low number: "))
        high = int(input("Enter the high number: "))
        answer = random.randint(low, high)  
        guesses = 0                         
        print(f"Enter a number between {low} and {high}")

        while True:
            tebak = input("Enter your guess: ")

            if tebak.isdigit():
                tebak = int(tebak)
                guesses += 1

                if tebak < low or tebak > high:
                    print(f"{tebak} is out of range")
                    print(f"Enter a number between {low} and {high}")
                elif tebak < answer:
                    print("too low")
                elif tebak > answer:
                    print("too high")
                else:
                    print(f"Correct! the answer was {answer}")
                    print(f"you guess {guesses} times")
                    if not input("Play again ? (y/n): ").lower() == "y":
                        runnin = False
                    break  
            else:
                print(f"{tebak} is invalid")
                print(f"Enter a number between {low} and {high}")

def gunting_kertas_batu():
    print("***** Gunting Kertas Batu *****")
    opsi = ("gunting","kertas","batu",)
    runnin = True
    pScore = 0
    cScore = 0
    tScore = 0

    while runnin:
        player = None
        komputer = random.choice(opsi)

        while True:
            print("************************************")
            player = input("batu - kertas - gunting (q to quit): ")
            print("************************************")
            if player == "q":
                runnin = False
                break
            if player in opsi:
                break
            else:
                print(f"{player} is invalid pls choose (batu - kertas - gunting)")
        if not runnin:
            break

        if player == komputer:
            print("tie")
            tScore += 1
        elif player == "gunting" and komputer == "kertas":
            print("You win")
            pScore += 1
        elif player == "kertas" and komputer == "batu":
            print("You win")
            pScore += 1
        elif player == "batu" and komputer == "gunting":
            print("You win")
            pScore += 1
        else:
            print("you lose")
            cScore += 1

        print()
        print(f"you  : {player}")
        print(f"bot  : {komputer}")
        print("-----------------------")
        print(f"you  : {pScore}")
        print(f"tie  : {tScore}")
        print(f"bot  : {cScore}")
    print("thx for playing")

def dice_roller():
    while True:
        dice_art = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘",),
            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘",),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘",),
            4: ("┌─────────┐",
                "│ ●     ● │",
                "│         │",
                "│ ●     ● │",
                "└─────────┘",),
            5: ("┌─────────┐",
                "│ ●     ● │",
                "│    ●    │",
                "│ ●     ● │",
                "└─────────┘",),
            6: ("┌─────────┐",
                "│ ●     ● │",
                "│ ●     ● │",
                "│ ●     ● │",
                "└─────────┘",)
        }
        dadu = []
        total = 0
        jumlah = int(input("jumlah dadu: "))

        if jumlah > 23:
            print("cant enter more than 23")
            jumlah = int(input("jumlah dadu: "))

        for x in range(jumlah):
            dadu.append(random.randint(1,6))

        for line in range(5):
            for die in dadu:
                print(dice_art.get(die)[line],end="")
            print()

        for x in dadu:
            total += x
        print(f"total : {total}")
        if not input("roll again ? (y/n): ").lower() == "y":
            break

def bankProgram():
    print("***** Bank Program *****")
    def show_balance():
        print(f"Your balance is: Rp.{balance:.3f}")

    def deposit():
        jumlah = float(input("Enter the amount to be deposited: "))

        if jumlah <= 0:
            print("Debt is Unacceptable")
            return 0
        else:
            return jumlah

    def withdraw():
        jumlah = float(input("Enter the amount to withdraw: "))

        if jumlah > balance:
            print("You DONT have that money in ur balance")
            return 0
        elif jumlah <= 0:
            print("Amount must be greater than 0")
            return 0
        else:
            return jumlah

    balance = 0
    runnin = True

    while runnin:
        print()
        print("Python Bank")
        print("----------------------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("----------------------")

        pilihan = input("Enter you choice: ")
        if pilihan == "1":
            show_balance()
        elif pilihan == "2":
            balance += deposit()
        elif pilihan == "3":
            balance -= withdraw()
        elif pilihan == "4":
            runnin = False
            print("Thank You For Using Python Bank")
        else:
            print("******************")
            print("Invalid Input")
            print("******************")

def slot_game():
    print("***** Slot Game *****")
    def spin_row():
        simbol = ["🔔", "⭐", "🍒"]
        return [random.choice(simbol) for _ in range(3)]

    def print_row(row):
        print(" | ".join(row)) 

    def get_payout(row, bet):
        if row [0] == row [1] == row [2]:
            if row[1] == '🔔':
                return bet * 2
            elif row[1] == '🍒':
                return bet * 3
            elif row[1] == '⭐':
                return bet * 5
        return 0

    balance = 100
    print("--------------------")
    print("Welcome To Cahsino")
    print("Symbols: 🔔-⭐-🍒")
    print("--------------------")

    while balance > 0:
        print(f"Ur balance: {balance}")
        bet = input("enter ur bet: ")

        if not bet.isdigit():
            print("masukin nomor ya pea")
            continue
        bet = int(bet)
        if bet > balance:
            print("U dont have that much money pal")
            continue
        if bet <= 0:
            print("whatchu gonna bet idiot")
            continue
        
        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"you win {payout}")
        else:
            print("you lost")
            print(f"your balance: {balance}")

        balance += payout
        if balance == 0:
            print("Game Over")
            break
        if not input("Play again ? (y/n): ").lower() == "y":
            break

def encryption():
    print("***** encryption *****")
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)

    #Encrypt
    plain = input("enter a massage to be encrypted: ")
    cypher = ""

    for huruf in plain:
        index = chars.index(huruf)
        cypher += key[index]

    print(f"Original : {plain}")
    print(f"Encrypted: {cypher}")

    #Decrypt
    cypher = input("enter a massage to be Decrypted: ")
    plain = ""

    for huruf in cypher:
        index = key.index(huruf)
        plain += chars[index]

    print(f"Encrypted: {cypher}")
    print(f"Original : {plain}")

def hangMan():
    print("*****  Hangman Game *****")
    kata = ("aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra")
    hang_art = {0:("   ",
                "   ",
                "   "),

                1:(" o ",
                "   ",
                "   "),
                2:(" o ",
                " | ",
                "   "),
                3:(" o ",
                "/| ",
                "   "),
                4:(" o ",
                "/|\\ ",
                "   "),
                5:(" o ",
                "/|\\ ",
                "/  "),
                6:(" o ",
                "/|\\ ",
                "/ \\"),}
                
    def display(wrong_guesses):
        print("++++++++++++++++++")
    for x in hang_art[wrong_guesses]:
        print(x)
    print("++++++++++++++++++")

    def hint_display(hint):
        print(" ".join(hint))

    def display_answer(answer):
        print(" ".join(answer))

    answer = random.choice(kata)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letter = set()
    runnin = True

    while runnin:
        display(wrong_guesses)
        hint_display(hint)
        guess = input("enter 1 letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue
            
        if guess in guessed_letter:
            print(f"you already guess {guess}")
            continue

        guessed_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display(wrong_guesses)
            display_answer(answer)
            print("You Win")
            runnin = False

        elif wrong_guesses >= len(hang_art) - 1:
            display(wrong_guesses)
            display_answer(answer)
            print("You lose")
            runnin = False

def roman_2_numeric():
    print("***** Roman to number *****")
    numeral_input = input("enter the roman numeral input: ").upper()
    def roman_to_int(numeral_input):

        final = 0
        if "CM" in numeral_input:
            final += 900
            numeral_input = numeral_input.replace("CM", "")
        if "CD" in numeral_input:
            final += 400
            numeral_input = numeral_input.replace("CD", "")
        if "XC" in numeral_input:
            final += 90
            numeral_input = numeral_input.replace("XC", "")
        if "XL" in numeral_input:
            final += 40
            numeral_input = numeral_input.replace("XL", "")
        if "IX" in numeral_input:
            final += 9
            numeral_input = numeral_input.replace("IX", "")
        if "IV" in numeral_input:
            final += 4
        numeral_input = numeral_input.replace("IV", "")

        for i in numeral_input:
            if i == "M":
                final += 1000
            elif i == "D":
                final += 500
            elif i == "C":
                final += 100
            elif i == "L":
                final += 50
            elif i == "X":
                final += 10
            elif i == "V":
                final += 5
            elif i == "I":
                final += 1
        print("The roman numerals you entered translates to: " + str(final) + "!")
    roman_to_int(numeral_input)

def pokemon_info():
    print("***** Pokemon Info *****")
    base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon_info(name):
        url = f"{base_url}/pokemon/{name}"
        response = requests.get(url)
    
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else:
            print(f"failed to retrieve data {response.status_code}")

    pokemon_name = input("enter pokemon name: ")
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name   : {pokemon_info["name"].capitalize()}")
        print(f"Id     : {pokemon_info["id"]}")
        print(f"Height : {pokemon_info["height"]}")
        print(f"Weight : {pokemon_info["weight"]}")

def email_slicer():
    print("******* Email Slicer *******")
    email = input("enter your email: ")
    username = email[:email.index("@")]
    domain = email[:email.index("@") + 1:]
    print(f"your username is '{username}' and domain is '{domain}'")

def compound_interest():
    while True:
        principle = int(input("enter the principle: "))
        if principle <= 0:
            print("principle cant less than or equal to zero")
        else:
            break

    while True:
        rate = int(input("enter the rate: "))
        if rate <= 0:
            print("rate cant less than or equal to zero")
        else:
            break

    while True:
        year = int(input("enter the time (year): "))
        if year <= 0:
            print("year cant less than or equal to zero")
        else:
            break

    total = principle * pow((1 + rate / 100), year)
    print(f"Balance after {year} year is: ${total:.2f}")

def concession_stand():
    print("--------- Concession Stand ---------")
    menu = {"pizza": 3.00,
            "nachos": 4.50,
            "popcorn": 6.00,
            "fries": 2.50,
            "chips": 1.00,
            "pretzel": 3.50,
            "soda": 3.00,
            "lemonade": 4.25}
    cart = []
    total = 0

    print("---------- Menu ----------")
    for x, y in menu.items():
        print(f"{x:10}: {y:.2f}")
    print("--------------------------")

    while True:
        food = input("Enter the food (q to quit): ").lower()
        if food == 'q':
            break
        elif food not in menu:
            print(f"{food} is not on the list")
        elif menu.get(food) is not None:
            cart.append(food)

    print("------- Your Order -------")
    print(' - '.join(cart))
    for x in cart:
        total += menu.get(x)
    print(f"\nyour total is: {total:.2f}")

def credit_card_validator():
    print("**** Credit Card Validator ****")
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    card_number = input("enter a credit card number: ")
    card_number = card_number.replace("-","")
    card_number = card_number.replace(" ","")
    card_number = card_number [::-1]

    for x in card_number[::2]:
        sum_odd_digits += int(x)

    for x in card_number[1::2]:
        x = int(x) * 2
        if x >= 10:
            sum_even_digits += (1(x % 10))
        else:
            sum_even_digits += x

    total = sum_even_digits + sum_odd_digits
    if total % 10 == 0:
        print("VALID")
    else:
        print("INVALID")

choice = input("Whick project do you want to see: (1-15): ")

if choice == '1':
    madlibs()
elif choice == '2':
    simpleCalculator()
elif choice == '3':
    weightConverter()
elif choice == '4':
    temperatureConversion()
elif choice == '5':
    timeCountDown()
elif choice == '6':
    shoppingCart()
elif choice == '7':
    quizGame()
elif choice == '8':
    numberGuessing()
elif choice == '9':
    gunting_kertas_batu()
elif choice == '10':
    dice_roller()
elif choice == '11':
    bankProgram()
elif choice == '12':
    slot_game()
elif choice == '13':
    encryption()
elif choice == '14':
    hangMan()
elif choice == '15':
    roman_2_numeric()
elif choice == '16':
    pokemon_info()
else:
    print(f"{choice} is not yet created")        