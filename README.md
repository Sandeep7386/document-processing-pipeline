# 📄 Automated Document Processing Pipeline

## 🚀 Overview

This project implements an automated system to extract and process structured data from documents (PDFs and images) using OCR and rule-based validation.

The pipeline performs:

* OCR-based text extraction
* Line-by-line content reconstruction
* Structured data extraction (Name, Amount, Date, ID)
* Data validation
* Automated action triggering

---

## 🎯 Features

* ✅ Supports **PDF and Image inputs**
* ✅ **OCR using Tesseract**
* ✅ **Line-by-line text extraction (layout-aware)**
* ✅ Extracts structured fields:

  * Name
  * Amount
  * Date
  * ID
* ✅ Validation logic for extracted data
* ✅ Automated decision system (action triggering)
* ✅ Clean and structured JSON output

---

## 🧠 System Architecture

```
Input (PDF/Image)
        ↓
PDF → Image Conversion (Poppler)
        ↓
OCR Engine (Tesseract)
        ↓
Line Extraction (Spatial Grouping)
        ↓
Full Text Reconstruction
        ↓
Field Extraction (Regex)
        ↓
Validation Layer
        ↓
Action Trigger
        ↓
JSON Output
```

---

## 🛠️ Tech Stack

| Component        | Technology          |
| ---------------- | ------------------- |
| Backend API      | FastAPI             |
| Server           | Uvicorn             |
| OCR Engine       | Tesseract OCR       |
| Image Processing | Pillow              |
| PDF Processing   | pdf2image (Poppler) |
| Language         | Python              |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/Sandeep7386/document-processing-pipeline.git
cd document-processing-pipeline
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Install Tesseract OCR

* Download and install Tesseract
* Default path:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

* Update path in `app/ocr.py` if required

---

### 5. Install Poppler (for PDF support)

* Download Poppler (Windows build)
* Extract to:

```
C:\poppler\
```

* Update path in `app/main.py`:

```
POPPLER_PATH = r"C:\poppler\Library\bin"
```

---

## ▶️ Run the Project

```
uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📦 Sample Output

```json
{
  "document_id": "DOC_001",
  "total_pages": 1,
  "results": [
    {
      "page": 1,
      "lines": [
        "Payment Confirmation",
        "Transaction ID : TXN123456789",
        "Name : John Doe",
        "Reference Number : REF987654321",
        "Contact Number : 0000000000",
        "Amount : 1000.00"
      ],
      "structured_data": {
        "name": "John Doe",
        "amount": 1000.0,
        "date": null,
        "id": "TXN123456789"
      },
      "validation": {
        "name": true,
        "amount": true,
        "date": false,
        "id": true
      },
      "status": "failed",
      "action": "sent_to_manual_review"
    }
  ],
  "timestamp": "2026-01-01T00:00:00"
}
```

---

## ✅ Validation Rules

* **Name** → Alphabetic, non-empty
* **Amount** → Numeric, > 0
* **Date** → Valid format (DD/MM/YYYY, DD-MM-YYYY, YYYY-MM-DD)
* **ID** → Alphanumeric, 6–12 characters

---

## ⚡ Action Logic

* ✔ If all fields are valid → `"stored_and_api_triggered"`
* ❌ If any field is invalid → `"sent_to_manual_review"`

---

## 📌 Key Highlights

* Hybrid approach: **OCR + Rule-based extraction**
* Handles **real-world noisy documents**
* Supports **multi-page PDFs**
* Designed with **modular architecture**

---

## 📢 Note

This project demonstrates a complete document processing pipeline combining OCR, data extraction, validation, and automation — suitable for real-world applications like invoice processing, form digitization, and document analytics.
