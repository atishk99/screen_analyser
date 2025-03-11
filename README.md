# Screen Analyzer with Local LLM

This Python script captures a specific area of the screen, extracts text using OCR, and analyzes it using a **local Llama 3 model**.

## 📌 Features
- Captures a screen region (supports **primary and secondary monitors**)
- Extracts text using **Tesseract OCR**
- Sends the text to a **local Llama 3 model** for analysis
- Outputs a **summary** or an **answer** (configurable)

## 🛠️ Installation

### 1. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Ensure Tesseract OCR is installed on macOS:
```bash
brew install tesseract
```

### 3. Run the script:
```bash
python main.py
```


## 🛠️ Configuration
### Modify these values in main.py:
```text
•   monitor_index = 0 → Primary screen (Change to 1 for secondary)
•   (x, y, width, height) → Adjust for your screen layout
```



