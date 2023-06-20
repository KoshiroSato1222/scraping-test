import requests
r = requests.get("https://weather.tsukumijima.net/api/forecast/city/120010")
# forecasts の中身を表示
print(r.json()["forecasts"])

# リストのサイズを確認
print(len(r.json()["forecasts"]))

# 3日分の天気予報と最高気温を取得する
for i in range(0,3):
    # 日付
    print(r.json()["forecasts"][i]["date"])
    # 天気予報
    print(r.json()["forecasts"][i]["telop"])
    # 最高気温
    print(r.json()["forecasts"][i]["temperature"]["max"]["celsius"])