import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_lines(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    lines = []
    line_map = {}

    n = len(data['text'])

    for i in range(n):
        text = data['text'][i].strip()
        conf = int(data['conf'][i])

        if conf > 30 and text:
            y = data['top'][i]

            found = False
            for key in line_map:
                if abs(key - y) < 10:
                    line_map[key].append((data['left'][i], text))
                    found = True
                    break

            if not found:
                line_map[y] = [(data['left'][i], text)]

    # 🔥 Sort and clean lines
    for y in sorted(line_map.keys()):
        words = sorted(line_map[y], key=lambda x: x[0])
        line = " ".join([w[1] for w in words])

        # 🔴 REMOVE NOISE
        if len(line) > 3 and not line.startswith("@") and not line.lower().startswith("gmail"):
            lines.append(line)

    return lines