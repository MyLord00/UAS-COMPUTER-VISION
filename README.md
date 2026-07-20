# Indonesian License Plate Recognition using Qwen2-VL-2B-Instruct

This project implements **Optical Character Recognition (OCR)** for Indonesian vehicle license plates using the **Qwen2-VL-2B-Instruct** Visual Language Model (VLM) running locally with **LM Studio**. The model predicts the license plate number from an image, and the prediction is evaluated using **Character Error Rate (CER)**.

---

## Features

- Visual Language Model (VLM) based OCR
- Local inference using LM Studio
- Python implementation with OpenAI API
- Automatic CER calculation
- Save prediction results to CSV

---

## Project Structure

```text
.
├── dataset
│   └── images
│       └── test
├── output
│   └── prediction.csv
├── ground_truth.csv
├── main.py
├── cer.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.10+
- LM Studio
- Qwen2-VL-2B-Instruct
- OpenAI Python SDK
- Pandas

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install openai pandas
```

---

## Dataset

The project uses the **Indonesian License Plate Recognition Dataset**.

Directory structure:

```text
dataset/
└── images/
    └── test/
```

Ground truth labels:

```text
ground_truth.csv
```

Example:

| image | ground_truth |
|-------|--------------|
| test001_1.jpg | B9140BCD |
| test001_2.jpg | B2407UZO |

---

## LM Studio Configuration

1. Open LM Studio.
2. Load **Qwen2-VL-2B-Instruct**.
3. Start the Local Server.

Example configuration:

```python
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    timeout=300
)
```

Model:

```python
MODEL_NAME = "qwen2-vl-2b-instruct"
```

---

## OCR Workflow

```text
License Plate Image
        │
        ▼
Read Image (Python)
        │
        ▼
Convert Image to Base64
        │
        ▼
Send Request to LM Studio
        │
        ▼
Qwen2-VL-2B-Instruct
        │
        ▼
Prediction
        │
        ▼
Clean Prediction (Regex)
        │
        ▼
Ground Truth Comparison
        │
        ▼
CER Evaluation
        │
        ▼
prediction.csv
```

---

## OCR Prompt

```text
You are an OCR system.

Read the Indonesian vehicle license plate.

Rules:
- Return ONLY the license plate.
- Do not explain.
- Do not add any extra words.
- Remove all spaces.
- Output must contain only uppercase letters and digits.

Example:
B1234XYZ
```

---

## Character Error Rate (CER)

CER is calculated using the following equation:

```text
CER = (S + D + I) / N
```

Where:

- **S** = Substitution
- **D** = Deletion
- **I** = Insertion
- **N** = Number of characters in Ground Truth

Example:

Ground Truth

```text
B2407UZO
```

Prediction

```text
B2407UZ
```

Result

```text
S = 0
D = 1
I = 0
N = 8

CER = (0 + 1 + 0) / 8
CER = 0.125
```

---

## Running

Run the project:

```bash
python main.py
```

The program will:

1. Read all images from the test dataset.
2. Convert images into Base64 format.
3. Send the images to LM Studio.
4. Predict the license plate number.
5. Clean the prediction using Regular Expression.
6. Compare prediction with Ground Truth.
7. Calculate Character Error Rate.
8. Save the results to `prediction.csv`.

---

## Output

Example:

| image | ground_truth | prediction | S | D | I | N | CER_score |
|-------|--------------|------------|---|---|---|---|-----------|
| test001_1.jpg | B9140BCD | B9140BCD | 0 | 0 | 0 | 8 | 0.0000 |
| test001_2.jpg | B2407UZO | B2407UZ | 0 | 1 | 0 | 8 | 0.1250 |

Output file:

```text
output/prediction.csv
```

---

## Technologies

- Python
- Qwen2-VL-2B-Instruct
- LM Studio
- OpenAI API
- Pandas
- Regular Expression (Regex)

---

## Author

**Arya Wardana**

Computer Vision Project

Politeknik Negeri Batam
