# auto-metadata
# 📸 Auto Metadata Generator (Adobe Stock & Freepik Optimized)

A Python-based automation tool to generate **high-quality metadata (title, keywords, filename, category)** for stock images.

Designed specifically for:

* Adobe Stock contributors
* Freepik contributors
* Bulk image upload workflows

---

## 🚀 Features

* 🔍 **AI Captioning (BLIP Model)**

  * Automatically generates image descriptions

* 🧠 **Adobe Stock Optimized Metadata**

  * Natural titles (not spammy)
  * SEO-friendly keyword ordering
  * Max 25 keywords (ideal for Adobe)

* 🏷 **Auto Filename Generator**

  * Converts keywords into clean, SEO-friendly filenames

* 🗂 **Auto Category Detection**

  * Technology, Business, Food, Lifestyle, etc.

* ⚡ **Batch Processing**

  * Process entire folders of images at once

* 🖼 **Image Optimization**

  * Auto resize for faster AI processing

* 📄 **CSV Export**

  * Ready-to-use metadata file

---

## 📦 Installation

```bash
pip install pillow transformers torch
```

---

## 📁 Project Structure

```
project/
│
├── generator.py
├── images/
│   ├── image1.jpg
│   ├── image2.png
│
├── renamed_images/
├── metadata_output.csv
```

---

## ⚙️ Configuration

Edit inside script:

```python
INPUT_FOLDER = "images"
OUTPUT_FOLDER = "renamed_images"
OUTPUT_CSV = "metadata_output.csv"
```

---

## ▶️ Usage

Run the script:

```bash
python generator.py
```

---

## 📊 Output

### 1. Renamed Images

Images will be saved to:

```
/renamed_images
```

Filename example:

```
modern_login_ui_design.jpg
```

---

### 2. Metadata CSV

```
metadata_output.csv
```

| filename | title | keywords | category | releases |
| -------- | ----- | -------- | -------- | -------- |

---

## 💡 Best Practices (IMPORTANT)

### Adobe Stock

* Keep titles **short and natural**
* Avoid keyword stuffing
* Put **most important keywords first**

### Freepik

* More flexible than Adobe
* Still prioritize relevance

---

## ⚠️ Limitations

* Adobe Stock does **not support CSV upload directly**
* Metadata must be copy-pasted manually
* AI captions may require slight manual refinement

---

## 🔥 Recommended Workflow

1. Run script
2. Upload images
3. Copy metadata from CSV
4. Add 2–3 niche keywords manually
5. Submit

---

## 🚀 Future Improvements

* GPT-based keyword optimization
* Trend-based keyword generation
* Multi-folder niche detection
* Auto uploader integration

---

## 🤝 Contributing

Feel free to fork this repo and improve it.

---

## 📜 License

MIT License

---

## 💬 Notes

This tool is designed to **speed up workflow**, not fully replace human optimization.

For best results:

* Combine automation + manual refinement
* Focus on niche-specific keywords

---

🔥 Happy uploading & selling!
