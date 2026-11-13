import numpy as np
import fitz  # PyMuPDF

"""Helper functions for processing PDF blueprints and visualizing instance segmentation results."""
# All polygon points in the JSON are in percentage format (0-100)
def pct_points_to_px(points_pct, W, H) -> np.ndarray:
    pts = np.asarray(points_pct, dtype=float)
    x = (pts[:, 0] / 100.0) * W
    y = (pts[:, 1] / 100.0) * H
    return np.column_stack([x, y])

def scale_points_to_dpi(points, dpi=300):
    scale_factor = dpi / 72.0 # 1 inch = 72 points (standard in PDF)
    return [[x * scale_factor, y * scale_factor] for x, y in points]

def remove_text(doc:fitz.Document, text_to_save:list[str]=["TS", "HT", "HS", "DM", "K", "MS", "TT", "TM"]):
    for page in doc:
        for block in page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT)["blocks"]:
            for line in block["lines"]:
                for span in line["spans"]:
                    keep = True
                    for keep_text in text_to_save: # Define what to save in pdf
                        if keep_text == span["text"].strip():
                            print(f"Removing text: '{span['text']}'")
                            keep = False
                            break
                    if not keep:
                        page.add_redact_annot(span["bbox"])  # cover text span with redact annot
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE,  # keep the images
            graphics=fitz.PDF_REDACT_LINE_ART_NONE,  # keep vector graphics
            )
        
"""
Example Instance Segmentation: Visualization of bounding boxes

PNG:

import helper
import cv2
import json
import numpy as np

imgidx = 1
img = cv2.imread(r"C:\dataset\instance segmentation\images\p_1\\" + f"{imgidx}.png")
data = json.load(open(r"C:\dataset\instance segmentation\labels\p_1\\" + f"{imgidx}.json", "r"))
w, h = img.shape[1], img.shape[0]
print(f"Image dimensions: width={w}, height={h}")
for room in data['rooms']:
    if room["segement_doc_idx"] != imgidx:
        continue
    points = room['points_pct'] # Use quad
    points = helper.pct_points_to_px(points, w, h)
    cv2.fillPoly(img, pts=[np.asarray(points, dtype=np.int32)], color=(0,255,0)) # Green fill for visualization

    

PDF numpy array:

import helper
import cv2
import json
import numpy as np
import fitz

imgidx = 1
dpi = 300

doc = fitz.open(r"C:\dataset\instance segmentation\pdfs\p_1\\" + f"{imgidx}.pdf")
data = json.load(open(r"C:\dataset\instance segmentation\labels\p_1\\" + f"{imgidx}.json", "r"))

helper.remove_text(doc, text_to_save=["Any text you want to keep on the blueprint, e.g. room labels"])
page = doc[0] # all of the pdfs are single page
w, h = page.rect.width, page.rect.height

# Render the page to a numpy array given a dpi (dots per inch) for better resolution
pixmap = page.get_pixmap(dpi=dpi)
np_img = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(pixmap.height, pixmap.width, pixmap.n).copy()

for room in data['rooms']:
    if room["segement_doc_idx"] != imgidx:
        continue
    points = room['points_pct'] # Use quad
    points = helper.pct_points_to_px(points, w, h)

    # Scale points to match the rendered image dimensions based on the dpi
    points_scaled = helper.scale_points_to_dpi(points, dpi)
    cv2.fillPoly(np_img, pts=[np.asarray(points_scaled, dtype=np.int32)], color=(0,255,0)) # Green fill for visualization
"""
