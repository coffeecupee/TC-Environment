# -*- coding: utf-8 -*-

from aip import AipFace
import urllib.request
import base64
import time
from PIL import Image

# 百度人脸识别API账号信息
APP_ID = '35735257'
API_KEY = '6Y8oxmmmQEREMCbPaqIyePoA'
SECRET_KEY = 'XZtgGeL1Wo0yajlaghKxDxvNCCgI9NMi'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)  # 创建一个客户端用以访问百度云

# 图像编码方式
IMAGE_TYPE = 'BASE64'

# 用户组
GROUP = '108_9'

# 加载本地图片并转换为Base64编码
def load_image(file_path):
    with open(file_path, 'rb') as f:
        img = base64.b64encode(f.read()).decode('utf-8')
    return img

# 上传到百度API进行人脸检测
def go_api(image):
    result = client.search(image, IMAGE_TYPE, GROUP)
    if result['error_msg'] == 'SUCCESS':
        name = result['result']['user_list'][0]['user_id']
        score = result['result']['user_list'][0]['score']
        if score > 80:
            if name == 'wcx':
                print("welcome %s !" % str(name))
                time.sleep(3)
                return 1
            else:
                print("sorry,I don't know you")
                name = 'Unknow'
                return 0
    elif result['error_msg'] == 'pic not has face':
        print('cannot detect people')
        # time.sleep(2)
        return 0
    else:
        # print("error")
        #print(result['error_code'] + ' ' + result['error_code'])
        return 0

# 主函数
def face_recognition(image_path):
    image_data = load_image(image_path)  # 加载本地图片并转换为Base64编码
    res = go_api(image_data)  # 将图片上传到百度云进行人脸识别
    return res

# 在其他文件中调用时，传递image_path作为参数
if __name__ == '__main__':
    image_path = 'wcx1.jpg'  # 本地图片路径
    face_recognition(image_path)
