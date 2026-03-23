from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import io
from datetime import datetime
from pdf2image import convert_from_bytes

from app.ocr import extract_lines
from app.extractor import extract_fields
from app.validator import validate_all
from app.actions import trigger_action

app = FastAPI()

POPPLER_PATH = r"C:\Users\sande\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"


@app.post("/process/")
async def process(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        results = []

        # 🔴 PDF handling
        if file.filename.lower().endswith(".pdf"):
            images = convert_from_bytes(contents, poppler_path=POPPLER_PATH)

            for idx, image in enumerate(images):
                lines = extract_lines(image)
                full_text = "\n".join(lines)

                data = extract_fields(full_text)
                validation = validate_all(data)
                is_valid = all(validation.values())
                action = trigger_action(is_valid, data)

                results.append({
                    "page": idx + 1,
                    "lines": lines,
                    "structured_data": data,
                    "validation": validation,
                    "status": "processed" if is_valid else "failed",
                    "action": action
                })

        # 🔴 Image handling
        else:
            image = Image.open(io.BytesIO(contents))
            lines = extract_lines(image)
            full_text = "\n".join(lines)

            data = extract_fields(full_text)
            validation = validate_all(data)
            is_valid = all(validation.values())
            action = trigger_action(is_valid, data)

            results.append({
                "page": 1,
                "lines": lines,
                "structured_data": data,
                "validation": validation,
                "status": "processed" if is_valid else "failed",
                "action": action
            })

        return {
            "document_id": "DOC_" + datetime.now().strftime("%Y%m%d%H%M%S"),
            "total_pages": len(results),
            "results": results,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))