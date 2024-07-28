import pytesseract
import numpy as np
import re
import io

from PIL import Image


def extract_text(contents):
    image = Image.open(io.BytesIO(contents))
    text = pytesseract.image_to_string(image)

    return extract_info(text)


def extract_info(text):
    patterns = {
        'Nama': r'Nama\s*:\s*(.*)',
        'NPM': r'NPM\s*:\s*(\d+)',
        'Fakultas': r'Fakultas\s*:\s*(.*)',
        'Program Studi': r'Program Studi\s*:\s*(.*)',
        # 'Program': r'Program\s*:\s*(.*)',
    }
    
    info = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        if match:
            info[key] = re.sub(r'[^a-zA-Z0-9\s&]', '', match.group(1)).strip()
    
    info["Nama"] = ''.join([char for char in info["Nama"] if not char.islower()]).strip()
    return info

