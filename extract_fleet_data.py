import re
import json

with open("generate_catalog.py", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split('<div class="page')
print(f"Total page sections found: {len(pages)}")

vehicles = []

# Regex patterns
car_pat = re.compile(
    r'<div class="car-card">.*?<div class="car-name">(.*?)</div>.*?'
    r'<div class="car-pill">(.*?)</div>.*?'
    r'(?:<div class="car-specs-row">(.*?)</div>)?.*?'
    r'<table class="pricing-table">(.*?)</table>.*?'
    r'(?:<div class="deposit-badge">(.*?)</div>)?.*?'
    r'<img src="\{img_b64\(\'([^\']+)\'\)\}"',
    re.DOTALL
)

bike_pat = re.compile(
    r'<div class="bike-card">.*?<img src="\{img_b64\(\'([^\']+)\'\)\}".*?'
    r'<div class="bike-title">(.*?)</div>.*?'
    r'<div class="bike-spec-pill-row">(.*?)</div>.*?'
    r'<div class="bike-rate-val gold-gradient-text">(.*?)</div>.*?'
    r'<div class="bike-deposit">.*?<span>(.*?)</span>',
    re.DOTALL
)

for p_idx, p in enumerate(pages):
    cat_match = re.search(r'<div class="header-sub-title">(.*?)</div>', p)
    cat_title = cat_match.group(1) if cat_match else f"Page {p_idx}"
    
    # Split page by car cards
    car_chunks = p.split('<div class="car-card">')[1:]
    for chunk in car_chunks:
        name_m = re.search(r'<div class="car-name">(.*?)</div>', chunk)
        pill_m = re.search(r'<div class="car-pill">(.*?)</div>', chunk)
        specs_m = re.search(r'<div class="car-specs-row">(.*?)</div>', chunk, re.DOTALL)
        table_m = re.search(r'<table class="pricing-table">(.*?)</table>', chunk, re.DOTALL)
        dep_m = re.search(r'<div class="deposit-badge">(.*?)</div>', chunk, re.DOTALL)
        img_m = re.search(r'img_b64\(\'([^\']+)\'\)', chunk)
        
        if not (name_m and img_m):
            continue
            
        name = name_m.group(1).strip()
        pill = pill_m.group(1).strip() if pill_m else ""
        specs_raw = specs_m.group(1).strip() if specs_m else ""
        table_raw = table_m.group(1).strip() if table_m else ""
        dep_raw = dep_m.group(1).strip() if dep_m else ""
        img = img_m.group(1).strip()
        
        deposit = ""
        dep_match = re.search(r'₹\s*([0-9,]+)', dep_raw)
        if dep_match:
            deposit = "₹ " + dep_match.group(1)
        elif "₹" in dep_raw:
            deposit = dep_raw
            
        rates = re.findall(r'<td class="rate[^"]*">(.*?)</td>', table_raw)
        
        # Clean specs
        specs_list = re.findall(r'<div class="spec-tag">(.*?)</div>', specs_raw)
        clean_specs = [re.sub(r'<[^>]+>', '', s).strip() for s in specs_list]
        
        vehicles.append({
            "type": "car",
            "name": name,
            "category_header": cat_title,
            "pill": pill,
            "specs": clean_specs,
            "table_raw": table_raw,
            "rates": rates,
            "deposit": deposit,
            "image": img
        })

        
    # Check bike cards
    bike_matches = bike_pat.findall(p)
    for bm in bike_matches:
        img = bm[0].strip()
        title = bm[1].strip()
        specs = bm[2].strip()
        rate = bm[3].strip()
        dep = bm[4].strip()
        vehicles.append({
            "type": "bike",
            "name": title,
            "category_header": cat_title,
            "pill": "Superbike",
            "specs_raw": specs,
            "rates": [rate],
            "deposit": dep,
            "image": img
        })

print(f"Extracted {len(vehicles)} vehicles successfully.")

with open("fleet_dump.json", "w", encoding="utf-8") as f:
    json.dump(vehicles, f, indent=2, ensure_ascii=False)
print("Saved to fleet_dump.json")

