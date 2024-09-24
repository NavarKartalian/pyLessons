number: int = 1

floatNumber: float = 1.5

text: str = 'Testing'

boolean: bool = True

dictionary: dict = {
    "id": 1,
    "name": "Navar",
    "age": 22,
    "isStudent": False,
    "grades": []
}

listArray: list = [
  dictionary,
    {
      "id": 2,
      "name": "Cecília",
      "age": 20,
      "isStudent": True,
      "grades": [9, 8, 10]
    },
]

emptyList: list = []

tuple: tuple = (
    'Banana',
    "Apple",
    "Orange"
)

def findItemInList(list: list, index: int):
    return list[index]

if(number):
    print(number)



print(findItemInList(listArray, 0))