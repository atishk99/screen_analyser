import pytesseract
import cv2
import ollama
import os
import mss
import numpy as np
import datetime

# Ensure required directories exist
os.makedirs("screenshots", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# Select the monitor (0 is primary, 1 is secondary)
monitor_index = 0  # Change this to 1 for the secondary screen

# Define coordinates for the question area
x, y, width, height = 0, 200, 1600, 600  # Adjust as per screen layout

with mss.mss() as sct:
    monitors = sct.monitors  # Get all available monitors
    if len(monitors) > monitor_index:
        monitor = monitors[monitor_index]

        # Capture the screen area
        screenshot = sct.grab({
            "top": monitor["top"] + y,
            "left": monitor["left"] + x,
            "width": width,
            "height": height
        })

        # Convert screenshot to OpenCV format
        image = np.array(screenshot)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        # Generate timestamp for unique file names
        #timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save the screenshot
        #screenshot_path = f"screenshots/question_{timestamp}.png"
        #cv2.imwrite(screenshot_path, image)
        #print(f"Screenshot saved: {screenshot_path}")

        # Convert to grayscale for OCR
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Extract question text using OCR
        extracted_text = pytesseract.image_to_string(gray).strip()
        print("Extracted Question:", extracted_text)

        # Query local Llama 3 model via Ollama
        response = ollama.chat(
            model="llama3.1:latest",
            messages=[{"role": "user", "content": f"Analyse the text and give summary: {extracted_text}"}]
            # If you want to answer it to question that is on screen
            # messages=[{"role": "user", "content": f"Answer this quiz question concisely: {extracted_text}"}]
        )

        # Extract AI-generated answer
        answer = response['message']['content']
        print("AI Answer:", answer)

        # Save extracted text and AI response
        #result_path = f"results/response_{timestamp}.txt"
        #with open(result_path, "w") as file:
        #    file.write(f"Extracted Text:\n{extracted_text}\n\n")
        #    file.write(f"AI Answer:\n{answer}\n")
        #print(f"Results saved: {result_path}")

    else:
        print(f"Monitor {monitor_index} not found. Available monitors: {len(monitors) - 1}")