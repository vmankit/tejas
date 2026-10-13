import os
import base64
from playwright.sync_api import sync_playwright

WORKSPACE_DIR = r"C:\Users\rolln\OneDrive\Desktop\tejas"
ASSETS_DIR = os.path.join(WORKSPACE_DIR, "assets_clean")

def img_b64(filename):
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(path):
        print(f"Warning: image {path} does not exist")
        return ""
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = os.path.splitext(filename)[1].lower().replace(".", "")
    mime = "image/png" if ext == "png" else "image/jpeg"
    return f"data:{mime};base64,{data}"

print("Helper loaded.")
