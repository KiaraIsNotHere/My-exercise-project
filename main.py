import proyek
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

choice = input("Whick project do you want to see: (1-15): ")

if choice == '1':
    proyek.madlibs()
elif choice == '2':
    proyek.simpleCalculator()
elif choice == '3':
   proyek.weightConverter()
elif choice == '4':
    proyek.temperatureConversion()
elif choice == '5':
    proyek.timeCountDown()
elif choice == '6':
    proyek.shoppingCart()
elif choice == '7':
    proyek.quizGame()
elif choice == '8':
    proyek.numberGuessing()
elif choice == '9':
   proyek.gunting_kertas_batu()
elif choice == '10':
    proyek.dice_roller()
elif choice == '11':
    proyek.bankProgram()
elif choice == '12':
    proyek.slot_game()
elif choice == '13':
    proyek.encryption()
elif choice == '14':
    proyek.hangMan()
elif choice == '15':
    proyek.roman_2_numeric()
elif choice == '16':
    proyek.pokemon_info()
elif choice == '17':
    proyek.email_slicer()
elif choice == '18':
    proyek.compound_interest()
elif choice == '19':
    proyek.concession_stand()
elif choice == '20':
    proyek.credit_card_validator()
else:
    print(f"{choice} is not yet created")        