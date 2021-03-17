# First Program
from pprint import pprint

sample1 = {
    "items":
        {
            "item":
                [
                    {
                        "id": "0001",
                        "type": "donut",
                        "name": "Cake",
                        "ppu": 0.55,
                        "batters":
                            {
                                "batter":
                                    [
                                        {"id": "1001", "type": "Regular"},
                                        {"id": "1002", "type": "Chocolate"},
                                        {"id": "1003", "type": "Blueberry"},
                                        {"id": "1004", "type": "Devil's Food"}
                                    ]
                            },
                        "topping":
                            [
                                {"id": "5001", "type": "None"},
                                {"id": "5002", "type": "Glazed"},
                                {"id": "5005", "type": "Sugar"},
                                {"id": "5007", "type": "Powdered Sugar"},
                                {"id": "5006", "type": "Chocolate with Sprinkles"},
                                {"id": "5003", "type": "Chocolate"},
                                {"id": "5004", "type": "Maple"}
                            ]
                    },
                    {
                        "id": "0002",
                        "type": "donut",
                        "name": "Cake",
                        "ppu": 0.55,
                        "batters":
                            {
                                "batter":
                                    [
                                        {"id": "1005", "type": "Regular"},
                                        {"id": "1006", "type": "Chocolate"},
                                        {"id": "1007", "type": "Blueberry"},
                                        {"id": "1008", "type": "Devil's Food"}
                                    ]
                            },
                        "topping":
                            [
                                {"id": "6001", "type": "None"},
                                {"id": "6002", "type": "Glazed"},
                                {"id": "6005", "type": "Sugar"},
                                {"id": "6007", "type": "Powdered Sugar"},
                                {"id": "6006", "type": "Chocolate with Sprinkles"},
                                {"id": "6003", "type": "Chocolate"},
                                {"id": "6004", "type": "Maple"}
                            ]
                    }
                ]
        }
}
# pprint(sample1.keys())

# print("case_2 result: ")
# var_1 = sample1["items"]["item"][0]["batters"]["batter"]
# var_4 = var_1  # temporary storage of data
# var_1.extend(sample1["items"]["item"][0]["topping"])
# var_2 = sample1["items"]["item"][1]["batters"]["batter"]  # case 2
# var_2.extend(sample1["items"]["item"][1]["topping"])
#
# var_3 = var_1 + var_2
# pprint(var_3)
# print("case_1 result: ")
# pprint({sample1["items"]["item"][0]["id"]: var_4, sample1["items"]["item"][1]
# ["id"]: var_2})

# or
# for key, values in sample1.items():
#     print(values)
# new_data = []
# for data in sample1["items"]["item"]:
#     print(data)
#     new_data.extend(data["batters"]["batter"])
#     new_data.extend(data["topping"])
# pprint(new_data)


# def get_user_data():
new_result1 = {}

# for data, data_1 in sample1["items"].items():
#     for data_2 in data_1:
#         new_result1[data_2["id"]] = data_2["batters"]["batter"] + data_2["topping"]
#     print(new_result1)
for data_2 in sample1["items"]["item"]:
    new_result1[data_2["id"]] = data_2["batters"]["batter"] + data_2["topping"]
print(new_result1)




# new_data1[data_2["id"]] = new_data2(data_2["batters"]["batter"])


# {"id": "5007", "type": "Powdered Sugar"}
# print(sample1.keys())
# print(sample1.values())
# print(len(sample1))
# print(type(sample1))

# print(sample1["items"]["item"][0]["type"])
# print(sample1["items"]["item"][0]["batters"]["batter"][0]["id"])
# print("expected output", sample1["items"]["item"][0]["topping"][3])
#
# # # Second Program
# sample2 = {
#     "items":
#         {
#             "item":
#                 [
#                     {
#                         "id": "0001",
#                         "type": "donut",
#                         "name": "Cake",
#                         "ppu": 0.55,
#                         "batters":
#                             {
#                                 "batter":
#                                     [
#                                         {"id": "1001", "type": "Regular"},
#                                         {"id": "1002", "type": "Chocolate"},
#                                         {"id": "1003", "type": "Blueberry"},
#                                         {"id": "1004", "type": "Devil's Food"}
#                                     ]
#                             },
#                         "topping":
#                             [
#                                 {"id": "5001", "type": "None"},
#                                 {"id": "5002", "type": "Glazed"},
#                                 {"id": "5005", "type": "Sugar"},
#                                 {"id": "5007", "type": "Powdered Sugar"},
#                                 {"id": "5006", "type": "Chocolate with Sprinkles"},
#                                 {"id": "5003", "type": "Chocolate"},
#                                 {"id": "5004", "type": "Maple"}
#                             ]
#                     }
#                 ]
#         }
# }
# # # expected output ----> "Blueberry"
# print("expected output", sample2["items"]["item"][0]["batters"]["batter"][2]["type"])
