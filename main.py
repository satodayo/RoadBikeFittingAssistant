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

#Extract
rs = ExtractPoint("RShoulder",result)
rw = ExtractPoint("RWrist", result)
re = ExtractPoint("RElbow",result)
rh = ExtractPoint("RHip", result)
rk = ExtractPoint("RKnee", result)
ra = ExtractPoint("RAnkle", result)

#Right Elbow Angle
re_angle = CalculateAngle(re, rs, rw)
#Right Shoulder Angle
rs_angle = CalculateAngle(rs, re, rh)
#Right Hip Angle
rh_angle = CalculateAngle(rh, rk, rs)
#Right Knee Angle
rk_angle = CalculateAngle(rk, rh, ra)

with open("result/resultangle.txt", "a") as angle:
    angle.write("{}\n".format(datetime.datetime.now()))
    angle.write("Right Elbow Angle:{:.1f} °\n".format(re_angle))
    angle.write("Right Shoulder Angle:{:.1f} °\n".format(rs_angle))
    angle.write("Right Hip Angle:{:.1f} °\n".format(rh_angle))
    angle.write("Right Knee Angle:{:.1f} °\n\n".format(rk_angle))
