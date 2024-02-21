from PIL import Image
import subprocess
import time

# Generate unique path with timestamp
image_path = "image_" + str(time.time()) + ".jpg"

# Execute command to take a picture with the camera and output it in the folder
subprocess.run(["raspistill", 
	"-n",
	"-t", "1",
	"--ISO", "100" , # Lower ISO to not saturate the camera
	"-o", image_path
])

# Open the image and resize for quicker calculations
image = Image.open(image_path)
resized_image = image.resize((100, 100))
pixels = list(resized_image.getdata())
resized_image.save("resized.jpg")

# Calculate the average RGB color in the picture
average = [0, 0, 0]

for pixel in pixels:
	average[0] += pixel[0]
	average[1] += pixel[1]
	average[2] += pixel[2]

average[0] /= round(len(pixels))
average[1] /= round(len(pixels))
average[2] /= round(len(pixels))

print("Manual average: " + str(average))
print("1x1 resize: " + str(image.resize(1, 1)[0]))
