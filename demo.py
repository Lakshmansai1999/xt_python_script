import wget
#import cv2
import shutil

import sys





# image_url = "https://tyreehouseplans.com/wp-content/uploads/2017/07/front.jpg"
image_url = "https://xamplify.io/assets/images/xamplify-logo.png"

weburl_input= "https://xamplify.co/login"


image_filename = wget.download(image_url)
#print(image_filename)

#cv2.imwrite('C:\\Users\\klakshmansai\\Desktop\\project1\\res\\image.png', image_filename)

file_to_copy = "xamplify-logo.png"
destination_directory = "/var/lib/jenkins/workspace/xt_xAmplify_APK/res"

print('Image downloaded successfully:', image_filename)

shutil.copy(file_to_copy, destination_directory)



# Define the JavaScript code as a string
js_code = f"""
var weburl_input = "{weburl_input}";
console.log(weburl_input);
"""

# Specify the file name and path
file_name = r"/var/lib/jenkins/workspace/xt_xAmplify_APK/www/js/constanconfig.js"

# Write the JavaScript code to the file
with open(file_name, "w") as js_file:
    js_file.write(js_code)

print(f"JavaScript file '{file_name}' created successfully.")
