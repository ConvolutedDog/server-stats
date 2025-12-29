import requests
import base64
import os

def html_to_image_api():
    # 读取HTML内容
    with open('./dashboard/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 使用免费API（有限制）
    api_url = "https://html2img.com/api/v1"
    
    # 或者用这个：https://hcti.io/v1/image（免费额度）
    payload = {
        'html': html_content,
        'viewport_width': 1920,
        'viewport_height': 1080
    }
    
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        with open('output.png', 'wb') as f:
            f.write(response.content)
        print("✅ 使用API生成成功")
    else:
        print("❌ API调用失败")

html_to_image_api()
