import os
import re
import base64
import mimetypes
import pandas as pd
from openai import OpenAI
from cer import calculate_cer


# Konfigurasi LM Studio
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    timeout=300
)

MODEL_NAME = "qwen2-vl-2b-instruct"


# Folder Dataset
IMAGE_FOLDER = "dataset/images/test"
GROUND_TRUTH_FILE = "ground_truth.csv"

# Membaca Ground Truth
gt_df = pd.read_csv(GROUND_TRUTH_FILE)

# Membersihkan hasil OCR
def clean_prediction(text):

    if text is None:
        return ""

    text = text.upper()

    # Ambil pola plat Indonesia (misal B1234XYZ)
    match = re.search(r"[A-Z]{1,2}\s?\d{1,4}\s?[A-Z]{1,3}", text)

    if match:
        text = match.group()

    text = re.sub(r"[^A-Z0-9]", "", text)

    return text


results = []

# Loop seluruh gambar
for filename in sorted(os.listdir(IMAGE_FOLDER)):

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    print("=" * 60)
    print("Processing :", filename)


    # Ground Truth
    row = gt_df[gt_df["image"] == filename]

    if row.empty:
        print("Ground Truth tidak ditemukan.")
        continue

    ground_truth = row.iloc[0]["ground_truth"].strip().upper()

    # Encode Image
    image_path = os.path.join(IMAGE_FOLDER, filename)

    mime = mimetypes.guess_type(image_path)[0] or "image/jpeg"

    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode()


    # OCR dengan LM Studio
    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                     "What is the license plate number shown in this image? "
                                      "Respond only with the plate number."
                )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime};base64,{image_data}"
                            }
                        }
                    ]
                }
            ]
        )

    except Exception as e:

        print("Error :", e)
        continue

    # Prediction
    prediction = response.choices[0].message.content

    prediction = clean_prediction(prediction)


    # CER    
    cer_score, S, D, I, N = calculate_cer(
        ground_truth,
        prediction
    )

    print("Ground Truth :", ground_truth)
    print("Prediction   :", prediction)
    print("S =", S)
    print("D =", D)
    print("I =", I)
    print("N =", N)
    print("CER =", round(cer_score, 4))

 
    # Simpan
    results.append([
        filename,
        ground_truth,
        prediction,
        S,
        D,
        I,
        N,
        round(cer_score, 4)
    ])

# Simpan CSV
os.makedirs("output", exist_ok=True)

df = pd.DataFrame(
    results,
    columns=[
        "image",
        "ground_truth",
        "prediction",
        "S",
        "D",
        "I",
        "N",
        "CER_score"
    ]
)

df.to_csv(
    "output/prediction.csv",
    index=False
)


print("SELESAI")
print(df.head())