import requests
import json
import base64
import numpy as np
import datetime

img_path = "source/source.jpg"

img =  open(img_path, "rb").read()
response_type = "json"
request_body = {"response_type": response_type}
url = "https://ai-api.userlocal.jp/human_pose"
res = requests.post(url, data=request_body, files={"image_data": img})
data = json.loads(res.content)
result = data["result"]
image = base64.b64decode(data["image_data"])
with open("result/resultpic.jpg", "wb") as pic:
    pic.write(image)

#Extract point
##1人を複数人と捉える場合があるので強引に取得する
##TODO:スマートな実装じゃないので治す
def ExtractPoint(name, result):
    if (name in result["person1"]):
        return result["person1"][name]
    elif name in result["person2"]:
        return result["person2"][name]
    elif name in result["person3"]:
        return result["person3"][name]
    elif name in result["person4"]:
        return result["person4"][name]
    else:
        return [0,0]

#calcurate angle
def CalculateAngle(base, p1, p2):
    nbase = np.array(base)
    np1 = np.array(p1)
    np2 = np.array(p2) 
    u = np1 - nbase
    v = np2 - nbase

    x = np.inner(u, v)

    s = np.linalg.norm(u)
    t = np.linalg.norm(v)

    theta = np.arccos(x/(s*t))
    rd = np.rad2deg(theta)
    return rd

#Right Elbow Angle
re = CalculateAngle(ExtractPoint("RElbow",result), ExtractPoint("RShoulder",result), ExtractPoint("RWrist", result))
#Right Shoulder Angle
rs = CalculateAngle(ExtractPoint("RShoulder",result), ExtractPoint("RElbow",result), ExtractPoint("RHip", result))
#Right Hip Angle
rh = CalculateAngle(ExtractPoint("RHip",result), ExtractPoint("RKnee",result), ExtractPoint("RShoulder", result))
#Right Knee Angle
rk = CalculateAngle(ExtractPoint("RKnee",result), ExtractPoint("RHip",result), ExtractPoint("RAnkle", result))

with open("result/resultangle.txt", "a") as angle:
    angle.write("{}\n".format(datetime.datetime.now()))
    angle.write("Right Elbow :{:.1f} °\n".format(re))
    angle.write("Right Shoulder :{:.1f} °\n".format(rs))
    angle.write("Right Hip :{:.1f} °\n".format(rh))
    angle.write("Right Knee :{:.1f} °\n\n".format(rk))
