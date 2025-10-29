import proyek

print(proyek.df)

choice = input("Whick project do you want to see: (1-21): ")

handlers = {'1':  proyek.madlibs,'2':  proyek.simpleCalculator,'3':  proyek.weightConverter,'4':  proyek.temperatureConversion,'5':  proyek.timeCountDown,'6':  proyek.shoppingCart,'7':  proyek.quizGame,'8':  proyek.numberGuessing,'9':  proyek.gunting_kertas_batu,'10': proyek.dice_roller,'11': proyek.bankProgram,'12': proyek.slot_game,'13': proyek.encryption,'14': proyek.hangMan,'15': proyek.alarm,'16': proyek.pokemon_info,'17': proyek.email_slicer,'18': proyek.compound_interest,'19': proyek.concession_stand,'20': proyek.credit_card_validator,'21': proyek.roman_2_numeric,}

handler = handlers.get(choice)
if handler:
    handler()
else:
    print(f"{choice} is not yet created")       