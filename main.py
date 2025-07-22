import random
import string
import time


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
        tipe = lbs
        print(f"your weight is: {berat} {tipe}")
    elif tipe == 'lbs':
        berat = berat / 2.205
        tipe = kg
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
        answer = random.randint(low, high)  # reset answer for each round
        guesses = 0                         # reset guesses for each round
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
                    break  # break inner loop to start new round or exit
            else:
                print(f"{tebak} is invalid")
                print(f"Enter a number between {low} and {high}")