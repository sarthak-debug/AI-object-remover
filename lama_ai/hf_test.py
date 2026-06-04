from transformers import pipeline

print("Loading model...")

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

print("Hugging Face Working!")