# Indonesian License Plate Recognition using Visual Language Model (qwen2-vl-2b-instruct)

## Overview

This project implements **Optical Character Recognition (OCR)** for Indonesian vehicle license plates using a **Visual Language Model (VLM)**. The model used is **LLaVA 1.6 Mistral 7B**, which runs locally through **LM Studio** and is accessed via the OpenAI-compatible API.

The system reads license plate images, performs OCR using the VLM, compares the predicted text with the ground truth, and evaluates the performance using **Character Error Rate (CER)**.

---

## Features

- OCR for Indonesian license plates using Visual Language Model
- Local inference with LM Studio
- Python implementation using OpenAI API
- Automatic evaluation using Character Error Rate (CER)
- Outputs prediction results to CSV

---

## Project Structure

```
project/
│
├── dataset/
│   └── images/
│       └── test/
│
├── output/
│   └── prediction.csv
│
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
- qwen2-vl-2b-instruct
- Pandas
- OpenAI Python SDK

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas openai
```

---

## Dataset

Dataset:

**Indonesian License Plate Recognition Dataset**

Project structure:

```
dataset/
└── images/
    └── test/
```

Ground truth is stored in:

```
ground_truth.csv
```

Example:

| image | ground_truth |
|--------|--------------|
| test001_1.jpg | B9140BCD |
| test001_2.jpg | B2407UZO |

---

## LM Studio Configuration

Start LM Studio and load:

```
qwen2-vl-2b-instruct
```

Enable the local server.

Default endpoint:

```
http://127.0.0.1:1234/v1
```

The program connects using:

```python
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)
```

---

## Workflow

```
License Plate Image
          │
          ▼
Python
          │
          ▼
Convert Image to Base64
          │
          ▼
LM Studio
(LLaVA 1.6 Mistral)
          │
          ▼
Prediction
          │
          ▼
Clean Prediction
(Regex)
          │
          ▼
Ground Truth
          │
          ▼
CER Evaluation
          │
          ▼
prediction.csv
```

---

## OCR Prompt

The following prompt is used during inference:

```text
Read the Indonesian vehicle license plate.

Return ONLY the plate number.

Example:
B1234XYZ
```

---

## Character Error Rate (CER)

Performance is evaluated using Character Error Rate.

Formula:

```
CER = (S + D + I) / N
```

Where:

- **S** = Substitution
- **D** = Deletion
- **I** = Insertion
- **N** = Number of characters in Ground Truth

Example:

Ground Truth

```
B2407UZO
```

Prediction

```
B2407UZ
```

Result

```
S = 0
D = 1
I = 0
N = 8

CER = 0.125
```

---

## Running

Run:

```bash
python main.py
```

The program will

- Read all images
- Send images to LM Studio
- Predict license plate numbers
- Calculate CER
- Save the results

---

## Output

Example:

| image | ground_truth | prediction | S | D | I | N | CER_score |
|--------|--------------|------------|---|---|---|---|-----------|
| test001_1.jpg | B9140BCD | B9140BCD | 0 | 0 | 0 | 8 | 0.0000 |
| test001_2.jpg | B2407UZO | B2407UZ | 0 | 1 | 0 | 8 | 0.1250 |

Output file:

```
output/prediction.csv
```

---

## Technologies

- Python
- LM Studio
- LLaVA 1.6 Mistral 7B
- OpenAI Python SDK
- Pandas
- Regular Expression (Regex)

---

## Author

Arya Wardana

Computer Vision Project

Politeknik Negeri Batam
