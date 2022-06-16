from operator import methodcaller


medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    podium = []
    for value in results:
        podium.extend(value['podium'])      

    medallist = list(map(methodcaller("split", "."), podium))

    for (value) in medallist:
        match value[0]:
            case '1':
                value[0] = 3
            case '2':
                value[0] = 2

            case '3': 
                value[0] = 1

    scores = {}
    for value, country in medallist:
        total = scores.get(country, 0) + value
        scores[country] = total
    

    return scores


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
