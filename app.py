import requests

image_url = 'https://xamplify.io/assets/images/xamplify-logo.png'  # Replace with your image URL
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open('image.png', 'wb') as f:
        f.write(response.content)
    print('Image downloaded successfully')
else:
    print('Failed to download image. Status code:', response.status_code)
