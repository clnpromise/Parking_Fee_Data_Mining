import json
import requests
import base64
from aip import AipOcr
import re


 
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=dvhSujnaY9qaWlWNenyCo2ZK&client_secret=82G08tOb0wYntAHD4oYdEMPGsvQEHinA'
response = requests.get(host)
content = response.json()
access_token = content["access_token"]

# 定义常量  
APP_ID = '11650666'
API_KEY = 'qQqkIOEYaLdMwA42op63gaLc'
SECRET_KEY = 'Cnw2YGHs2n58CyVmLvyKAc5zwaQHMyVl'
# 初始化文字识别分类器
aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片 
def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()
imageAddr= open('paris.txt','r')
fo=open('pictureToWords.txt','w+')
for filepath in imageAddr.readlines():
	filepath=filepath.replace('\n','')
	image = open(filepath, 'rb').read()
	data = {'image': base64.b64encode(image).decode()}

	request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/parkingFee" + "?access_token=" + access_token
	response = requests.post(request_url, data=json.dumps(data))
	content = response.json()
	results=content['results']
	score=0
	for result in results:
		if result['name']=='parkingFee':
			score=result['score']
	print(results)
	if score>0.9:
		print(filepath)
		fo.write("New Parking Lot Begins Here\n")
		name=re.sub(r'/Users/chenlingna/Desktop/Project/pictureCrawling/pictures/','', filepath)
		fo.write(name+'\n')
		print(score)
		# 定义参数变量
		options = {
		#	'detect_direction': 'true',
			'language_type': 'ENG'
		}
		# 网络图片文字文字识别接口
		result = aipOcr.basicAccurate(get_file_content(filepath),options)
		lists=result['words_result']
		for element in lists:
			fo.write(element['words']+'\n')
	
 
