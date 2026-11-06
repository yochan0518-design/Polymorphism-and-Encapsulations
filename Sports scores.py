class cricket:
    def __init__(self, player, score):
        self.__player = player 
        self.__score = score

    def info(self):
        print(["cricket - player: {self.__player}, score: {self.__score}"])

    def play(self):
            print(" {self.__player} hits a six!")

    def get__score(self):
            return self.__score

    def set_score(self, new_score):
            if new_score >= 0:
                self.__score == new_score
                print(f"Score updated to {self.__score}")
            else:
                  print("Scores cannot be negative")


class Football:
    def __init__(self, player, score):
        self.__player = player 
        self.__score = score

    def info(self):
        print(["football - player: {self.__player}, score: {self.__score}"])

    def play(self):
            print(" {self.__player} hits a goal!")

    def get__score(self):
            return self.__score

    def set_score(self, new_score):
            if new_score >= 0:
                self.__score == new_score
                print(f"Score updated to {self.__score}")
            else:
                  print("Scores cannot be negative")

#create objects 
cricket = cricket("Rohit", 85)
Football = Football("Arjun", 2)

print("===Sports Scoreboard ===\n")
for sport in (cricket, Football):
      sport.info()
      sport.play()
      print()

print("--- direct changes attempt---")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score()}")

print("\n---Updating scores---")
cricket.set_score(100)
Football.set_score(1)