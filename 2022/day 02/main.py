import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from helpers.files import readAdventInput

def main():
    oponent = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
    }

    me = {
      'X': 'Rock',
      'Y': 'Paper',
      'Z': 'Scissors',
    }

    prediction = {
      'X': 'Lose',
      'Y': 'Draw',
      'Z': 'Win',
    }


    txt = readAdventInput("2022", "02")
    #separate the lines of the txt file
    lines = txt.splitlines()

    pointsTotalStrat1 = 0
    pointsTotalStrat2 = 0
    for line in lines:
        columns = line.split(" ")

        oponentMove = oponent[columns[0]]
        myMove = me[columns[1]]

        #Convert the moves to numbers
        oponentMoveNumber = moveToNumber(oponentMove)
        myMoveNumber = moveToNumber(myMove)

        myPrediction = prediction[columns[1]]

        pointsTotalStrat1 += playRound(oponentMoveNumber, myMoveNumber)
        hola = predictRound(oponentMove, myPrediction)

        if columns[0] == 'B' and columns[1] == 'Z':
            #X = lose (0), Y = draw (3), Z = win (6)
            #play: Rock = 1, Paper = 2, Scissors = 3
            print(oponentMove,hola)

        pointsTotalStrat2 += hola
        print(f"Round: {oponentMove} vs {myMove} -> {pointsTotalStrat1} points in total, {pointsTotalStrat2} points in total (Strategy 2)")

    
    print(f"Total points for Strategy 1: {pointsTotalStrat1}")
    print(f"Total points for Strategy 2: {pointsTotalStrat2}")


def predictRound(oponentMove: str, myOutcome: str ) -> int:
  oponentMoveNumber = moveToNumber(oponentMove)
  match myOutcome:
      case 'Win':
          predictedMove = (oponentMoveNumber + 1) % 3
          return playRound(oponentMoveNumber, predictedMove)
      case 'Draw':
          predictedMove = oponentMoveNumber
          return playRound(oponentMoveNumber, predictedMove)
      case 'Lose':
          predictedMove = (oponentMoveNumber - 1) % 3
          return playRound(oponentMoveNumber, predictedMove)   

def playRound(oponentMoveNumber: int, myMoveNumber: int) -> int:
    if myMoveNumber == 0:
        myMoveNumber = 3
    result = (myMoveNumber - oponentMoveNumber) % 3

    match result:
        case 0: #Draw
            return 3  + myMoveNumber
        case 1: #Win
            return 6  + myMoveNumber
        case 2: #Lose
            return 0  + myMoveNumber

def moveToNumber(move: str) -> int:
    match move:
        case 'Rock':
            return 1
        case 'Paper':
            return 2
        case 'Scissors':
            return 3

main()