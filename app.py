from flask import Flask, render_template, request, jsonify
import os
import base64
import cv2
import numpy as np

current_image_path = ""
app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)
    with open("current_image.txt", "w") as f:
     f.write(filepath)
     
    global current_image_path
    current_image_path = filepath

    image_path = f"uploads/{file.filename}"

    print("Saved:", filepath)
    print("Image Path:", image_path)

    return render_template(
        "index.html",
        image_path=image_path
    )


@app.route("/load_sample/<filename>")
def load_sample(filename):
    import shutil
    src = os.path.join("static", "samples", filename)
    dst = os.path.join("static", "uploads", filename)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(src):
        shutil.copy(src, dst)
        with open("current_image.txt", "w") as f:
            f.write(dst)
        global current_image_path
        current_image_path = dst
        return render_template(
            "index.html",
            image_path=f"uploads/{filename}"
        )
    return "Sample not found", 404


@app.route("/save_mask", methods=["POST"])
def save_mask():

    data = request.json["image"]

    header, encoded = data.split(",", 1)

    image_data = base64.b64decode(encoded)

    with open("mask.png", "wb") as f:
        f.write(image_data)

    return "Mask Saved Successfully!"


@app.route("/remove_object")
def remove_object():

    with open("current_image.txt", "r") as f:
        current_image_path = f.read().strip()

    print("Current Image Path:", current_image_path)

    image = cv2.imread(current_image_path)

    if image is None:
        return f"Could not load image: {current_image_path}"

    mask = cv2.imread("mask.png", 0)

    mask = cv2.resize(
        mask,
        (image.shape[1], image.shape[0])
    )
    print("Image Shape:", image.shape)
    print("Mask Shape:", mask.shape)
    result = cv2.inpaint(
        image,
        mask,
        3,
        cv2.INPAINT_TELEA
    )

    cv2.imwrite(
        "static/result.png",
        result
    )

    normalized_path = current_image_path.replace("\\", "/")
    if normalized_path.startswith("static/"):
        original_relative = normalized_path[len("static/"):]
    else:
        original_relative = normalized_path

    return render_template(
        "result.html",
        result_image="result.png",
        original_image=original_relative
    )
if __name__ == "__main__":
    app.run(debug=True)