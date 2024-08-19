class Config:


    def __init__(self, word=None):

        self.mode: str = "statistically random"
        self.locationsEnabled: bool = True
        self.itemsEnabled: bool = True

        if not word is None:
            if not word is "default":
                print("Woohoo! Looks like you found me c:")
        else:

            print("New configuration. Please fill out the following fields\n")

            while True:
                answer = input('Would you like to use the default configuration? ("Y" for yes or "N" for no)\n')

                if answer.lower() == "y":
                    break
                elif answer.lower() == "n":
                    while True:
                        print("Battle Royale Mode: (type in the letter corresponding to your preference)")
                        answer = input("A - Statistically random\nB - True Random\n")

                        if answer.lower() == "a":
                            break
                        elif answer.lower() == "b":
                            self.mode = "true random"
                        else:
                            print("!== Input invalid. Please try again. ==!")
                            continue

                    while True:
                        answer = input('Would you like the locations feature to be enabled? ("Y" for yes or "N" for no)\n')

                        if answer.lower() == "y":
                            break
                        elif answer.lower() == "n":
                            self.locationsEnabled = False
                        else:
                            print("!== Input invalid. Please try again. ==!")
                            continue

                    while True:
                        answer = input('Would you like the items feature to be enabled? ("Y" for yes or "N" for no)\n')

                        if answer.lower() == "y":
                            break
                        elif answer.lower() == "n":
                            self.itemsEnabled = False
                        else:
                            print("!== Input invalid. Please try again. ==!")
                            continue
                else:
                    print("!== Input invalid. Please try again. ==!")
                    continue