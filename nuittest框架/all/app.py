import json,os


# path1 = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(path1)
BASE_DIR = os.path.dirname(__file__)
def build_add_data():
    data = []
    with open(BASE_DIR + "/data/logindata.json", "r", encoding="utf-8") as f:
        da = json.load(f)
        for a, b in da.items():
            data.append((a, b[0], b[1], b[2]))
    return data

