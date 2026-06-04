from PIL import Image

def remove_object(image_path, mask_path):
    print("AI PROCESSING STARTED")
    image = Image.open(image_path)

    print("AI processing started...")
    print("Image:", image_path)
    print("Mask:", mask_path)

    image.save("static/result.png")

    return "static/result.png"