import requests


def api(size):
    
    resp = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=' + str(size))
    if size == 9:
        matri = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"],
                 ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]
    elif size == 4:
        matri = [["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"],
                 ["x", "x", "x", "x"]]
    for item in resp.json()["squares"]:
        matri[item["y"]][item["x"]] = str(item["value"])

    return matri