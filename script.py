from PIL import Image
import subprocess
import time

image_path = "image_" + str(time.time()) + ".jpg"

subprocess.run(["raspistill", 
	"-n",
	"-t", "1",
	"-o", image_path
])

image = Image.open(image_path)
resized_image = image.resize((100, 100))
pixels = list(resized_image.getdata())
resized_image.save("resized.jpg")

average = [0, 0, 0]

for pixel in pixels:
	average[0] += pixel[0]
	average[1] += pixel[1]
	average[2] += pixel[2]

average[0] /= round(len(pixels))
average[1] /= round(len(pixels))
average[2] /= round(len(pixels))

print(average)
