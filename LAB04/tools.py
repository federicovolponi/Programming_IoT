import json

def returnEvent(sensorDic, nameEvent):
    for event in sensorDic["e"]:
        if event.get("n") == nameEvent:
            return event