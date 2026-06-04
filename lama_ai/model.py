import shutil

def remove_object(image_path, mask_path):

    print("AI Remove Object Called")
    print("Image:", image_path)
    print("Mask:", mask_path)

    shutil.copy(
        image_path,
        "static/result.png"
    )

    return "static/result.png"