import re


def extract_fields(text):

    # 🔹 NAME (more flexible)
    name = re.search(r"(Name|Candidate's Name|Student Name)[:\- ]+(.*)", text)

    # 🔹 AMOUNT
    amount = re.search(r"(Amount|Total Amount)[:\- ]+(\d+\.?\d*)", text)

    # 🔹 DATE (🔥 FIXED — multiple formats)
    date = (
        re.search(r"\d{2}/\d{2}/\d{4}", text) or
        re.search(r"\d{2}-\d{2}-\d{4}", text) or
        re.search(r"\d{4}-\d{2}-\d{2}", text)
    )

    # 🔹 ID (capture payment / reference / generic ID)
    id_ = re.search(r"(ID|Payment ID|Reference Number)[:\- ]+(\w+)", text)

    return {
        "name": name.group(2).strip() if name else None,
        "amount": float(amount.group(2)) if amount else None,
        "date": date.group(0) if date else None,
        "id": id_.group(2) if id_ else None
    }