import os
import csv
import re
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# ======================
# CONFIG
# ======================
INPUT_FOLDER = "images"
OUTPUT_FOLDER = "renamed_images"
OUTPUT_CSV = "metadata_output.csv"
MAX_KEYWORDS = 25  # Adobe ideal 20–25

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ======================
# LOAD MODEL
# ======================
print("Loading AI model...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# ======================
# HELPERS
# ======================

def resize_image(image, max_size=768):
    w, h = image.size
    if max(w, h) > max_size:
        ratio = max_size / max(w, h)
        image = image.resize((int(w * ratio), int(h * ratio)))
    return image


def generate_caption(path):
    try:
        img = Image.open(path).convert('RGB')
        img = resize_image(img)
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs, max_length=18)
        return processor.decode(out[0], skip_special_tokens=True)
    except:
        return ""


def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text

# ======================
# 🔥 ADOBE OPTIMIZED
# ======================

def generate_title(caption):
    words = clean(caption).split()
    core = " ".join(words[:6])
    return core.title()


def generate_keywords(caption):
    words = clean(caption).split()

    # prioritaskan keyword penting di depan
    keywords = []

    # keyword utama
    keywords.extend(words[:10])

    # variasi natural (bukan spam)
    variations = [
        "design", "background", "template", "concept",
        "modern", "minimal", "creative"
    ]

    keywords.extend(variations)

    # remove duplicate & limit
    final = []
    for k in keywords:
        if k not in final and len(final) < MAX_KEYWORDS:
            final.append(k)

    return ", ".join(final)


def generate_filename(caption):
    words = clean(caption).split()
    return "_".join(words[:5])[:50]


def detect_category(caption):
    c = caption.lower()

    if any(x in c for x in ["food", "drink", "coffee"]):
        return "Food"
    if any(x in c for x in ["business", "office", "team"]):
        return "Business"
    if any(x in c for x in ["wedding", "couple", "love"]):
        return "Lifestyle"
    if any(x in c for x in ["ui", "app", "interface", "digital"]):
        return "Technology"

    return "General"

# ======================
# PROCESS
# ======================

results = []

for file in os.listdir(INPUT_FOLDER):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(INPUT_FOLDER, file)
        print("Processing:", file)

        caption = generate_caption(path)
        if not caption:
            continue

        title = generate_title(caption)
        keywords = generate_keywords(caption)
        category = detect_category(caption)

        new_name = generate_filename(caption) + os.path.splitext(file)[1]
        new_path = os.path.join(OUTPUT_FOLDER, new_name)

        try:
            img = Image.open(path)
            img.save(new_path, quality=90)
        except:
            continue

        results.append({
            "filename": new_name,
            "title": title,
            "keywords": keywords,
            "category": category,
            "releases": ""
        })

# ======================
# SAVE CSV
# ======================

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["filename", "title", "keywords", "category", "releases"])
    writer.writeheader()
    writer.writerows(results)

print("\n✅ DONE - ADOBE + FREEPIK OPTIMIZED")

# ======================
# STRATEGY NOTES
# ======================
# ✔ Title pendek & natural (Adobe suka)
# ✔ Keyword tidak spam (ranking aman)
# ✔ Keyword utama di depan (SEO)
# ✔ Max 25 keyword (optimal Adobe)
# ✔ Filename clean keyword
# ✔ Freepik tetap aman
