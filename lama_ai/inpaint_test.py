from PIL import Image

image = Image.open("static/uploads/test.png")

print("Image Loaded Successfully")
print("Image Size:", image.size)
image = image.convert("RGB")
image.save("static/ai_test_output.jpg")

print("AI Pipeline Ready")