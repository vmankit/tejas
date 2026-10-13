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

print("Building HTML with all 14 luxury pages...")

# Load key assets
logo_b64 = img_b64("logo_clean_alpha.png")
hero_b64 = img_b64("hero_cover.png")
qr_b64 = img_b64("qr_code.png")

cat_economic_b64 = img_b64("cat_economic.png")
cat_suvs_b64 = img_b64("cat_suvs.png")
cat_exec_b64 = img_b64("cat_executive.png")
cat_bikes_b64 = img_b64("cat_bikes.png")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>RevvRizz Luxe - Luxury Cars & Sports Bikes Catalog</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Montserrat:wght@400;500;600;700;800&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  
  @page {{
    size: 657pt 882pt;
    margin: 0;
  }}

  body {{
    background-color: #050608;
    color: #E2E8F0;
    font-family: 'Outfit', sans-serif;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .page {{
    width: 657pt;
    height: 882pt;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    background: radial-gradient(circle at 50% 0%, #151821 0%, #090A0E 55%, #040507 100%);
    display: flex;
    flex-direction: column;
    padding: 24pt 26pt 20pt 26pt;
  }}

  /* Gold Gradients */
  .gold-gradient-text {{
    background: linear-gradient(135deg, #FFF4D9 0%, #E3BC52 35%, #B88B27 70%, #F5DE96 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}

  .gold-border {{
    border: 1px solid rgba(212, 175, 55, 0.35);
  }}

  /* HEADER */
  .page-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding-bottom: 9pt;
    border-bottom: 1.5pt solid rgba(212, 175, 55, 0.4);
    margin-bottom: 12pt;
  }}
  .header-titles {{
    display: flex;
    flex-direction: column;
    gap: 2pt;
  }}
  .header-main-title {{
    font-family: 'Cinzel', serif;
    font-size: 15.5pt;
    font-weight: 800;
    letter-spacing: 2pt;
    line-height: 1.1;
  }}
  .header-sub-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 1.8pt;
    color: #ECC880;
    text-transform: uppercase;
  }}
  .header-limits {{
    display: flex;
    gap: 5pt;
    flex-wrap: wrap;
    justify-content: flex-end;
  }}
  .limit-badge {{
    background: linear-gradient(135deg, rgba(212, 175, 55, 0.18) 0%, rgba(212, 175, 55, 0.08) 100%);
    border: 1px solid rgba(212, 175, 55, 0.45);
    border-radius: 5pt;
    padding: 3.5pt 7pt;
    font-size: 7.2pt;
    font-weight: 700;
    letter-spacing: 0.8pt;
    color: #FFF2D1;
    text-transform: uppercase;
  }}
  .limit-badge-alt {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 5pt;
    padding: 3.5pt 7pt;
    font-size: 7.2pt;
    font-weight: 700;
    letter-spacing: 0.8pt;
    color: #DDE2EC;
    text-transform: uppercase;
  }}

  /* CAR CARDS CONTAINER */
  .car-cards-container {{
    display: flex;
    flex-direction: column;
    gap: 9.5pt;
    flex: 1;
    justify-content: space-between;
  }}

  .car-card {{
    background: linear-gradient(135deg, rgba(23, 26, 33, 0.9) 0%, rgba(12, 14, 18, 0.96) 100%);
    border: 1px solid rgba(212, 175, 55, 0.28);
    border-radius: 10pt;
    padding: 8pt 10pt;
    display: flex;
    align-items: center;
    gap: 12pt;
    box-shadow: 0 6pt 16pt rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
  }}
  .car-card::before {{
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 3.5pt;
    background: linear-gradient(180deg, #ECC880 0%, #D4AF37 50%, #8A6818 100%);
  }}

  .car-info {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 5pt;
  }}
  .car-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .car-name {{
    font-family: 'Cinzel', serif;
    font-size: 11pt;
    font-weight: 700;
    letter-spacing: 0.6pt;
    color: #FFFFFF;
  }}
  .car-pill {{
    background: rgba(212, 175, 55, 0.15);
    border: 1px solid rgba(212, 175, 55, 0.4);
    border-radius: 4pt;
    padding: 2pt 6pt;
    font-size: 6.5pt;
    font-weight: 700;
    color: #ECC880;
    letter-spacing: 0.5pt;
    text-transform: uppercase;
  }}

  .car-specs-row {{
    display: flex;
    gap: 5pt;
    align-items: center;
  }}
  .spec-tag {{
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 3.5pt;
    padding: 2pt 5pt;
    font-size: 6.8pt;
    color: #A6ACB8;
    font-weight: 600;
  }}
  .spec-tag strong {{
    color: #FFFFFF;
  }}

  /* PRICING TABLE */
  .pricing-table {{
    width: 100%;
    border-collapse: collapse;
    background: rgba(0,0,0,0.3);
    border-radius: 5pt;
    overflow: hidden;
    border: 1px solid rgba(212, 175, 55, 0.18);
  }}
  .pricing-table th, .pricing-table td {{
    padding: 3pt 5pt;
    font-size: 6.8pt;
    text-align: center;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }}
  .pricing-table th {{
    background: rgba(212, 175, 55, 0.12);
    color: #ECC880;
    font-weight: 700;
    letter-spacing: 0.5pt;
    font-size: 6.5pt;
    text-transform: uppercase;
  }}
  .pricing-table td.rate {{
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 8pt;
    color: #FFFFFF;
  }}
  .pricing-table td.rate-gold {{
    color: #F8E2A7;
    font-weight: 800;
  }}

  .deposit-badge {{
    display: inline-flex;
    align-items: center;
    gap: 4pt;
    font-size: 6.8pt;
    color: #9297A5;
  }}
  .deposit-badge span {{
    color: #ECC880;
    font-weight: 700;
  }}

  /* CAR SHOWCASE STAGE */
  .car-showcase {{
    width: 178pt;
    height: 102pt;
    border-radius: 8pt;
    background: #FFFFFF;
    border: 1.5pt solid rgba(212, 175, 55, 0.45);
    box-shadow: 0 4pt 15pt rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    position: relative;
    overflow: hidden;
  }}
  .car-img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
  }}

  /* BIKE GRID LAYOUT */
  .bike-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 10pt;
    flex: 1;
  }}
  .bike-card {{
    background: linear-gradient(135deg, rgba(23, 26, 33, 0.9) 0%, rgba(12, 14, 18, 0.96) 100%);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 9pt;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 6pt 16pt rgba(0,0,0,0.5);
  }}
  .bike-photo-container {{
    width: 100%;
    height: 155pt;
    overflow: hidden;
    position: relative;
    background: #000;
  }}
  .bike-photo {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .bike-info-box {{
    padding: 7pt 8pt 8pt 8pt;
    display: flex;
    flex-direction: column;
    gap: 4.5pt;
    flex: 1;
    justify-content: space-between;
  }}
  .bike-title {{
    font-family: 'Cinzel', serif;
    font-size: 8.8pt;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.15;
  }}
  .bike-spec-pill-row {{
    display: flex;
    gap: 4pt;
    align-items: center;
  }}
  .bike-pill {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 3pt;
    padding: 1.5pt 4pt;
    font-size: 6.2pt;
    font-weight: 600;
    color: #AAB0BE;
  }}
  .bike-pricing-strip {{
    background: rgba(212, 175, 55, 0.12);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 4pt;
    padding: 3.5pt 6pt;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .bike-rate-label {{
    font-size: 6.2pt;
    color: #E6CA85;
    font-weight: 600;
    text-transform: uppercase;
  }}
  .bike-rate-value {{
    font-family: 'Outfit', sans-serif;
    font-size: 8.8pt;
    font-weight: 800;
    color: #FFFFFF;
  }}
  .bike-deposit {{
    font-size: 6.2pt;
    color: #8C92A0;
  }}
  .bike-deposit strong {{
    color: #ECC880;
  }}

  /* FOOTER */
  .page-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(212, 175, 55, 0.2);
    padding-top: 7pt;
    margin-top: 9pt;
    font-size: 6.8pt;
    color: #727988;
    letter-spacing: 1pt;
    text-transform: uppercase;
  }}
  .footer-brand {{
    font-family: 'Cinzel', serif;
    color: #ECC880;
    font-weight: 700;
  }}

  /* PAGE 1: COVER */
  .cover {{
    justify-content: space-between;
    align-items: center;
    text-align: center;
    padding: 28pt 24pt 24pt 24pt;
    background: radial-gradient(circle at 50% 20%, #1c202a 0%, #090a0e 65%, #020304 100%);
  }}
  .cover-logo-wrapper {{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 5pt;
  }}
  .cover-logo-circle {{
    width: 190pt;
    height: 190pt;
    border-radius: 50%;
    background: #000000;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 35pt rgba(212, 175, 55, 0.4), inset 0 0 20pt rgba(0,0,0,0.9);
    border: 3.5pt solid #D4AF37;
    overflow: hidden;
  }}
  .cover-logo-img {{
    width: 88%;
    height: auto;
    object-fit: contain;
    filter: drop-shadow(0 4pt 12pt rgba(0,0,0,0.8));
  }}
  .cover-title {{
    font-family: 'Cinzel', serif;
    font-size: 19pt;
    font-weight: 800;
    letter-spacing: 4.5pt;
    text-transform: uppercase;
    margin-top: 15pt;
    display: flex;
    align-items: center;
    gap: 12pt;
    width: 100%;
    justify-content: center;
  }}
  .gold-divider {{
    height: 1.5pt;
    width: 60pt;
    background: linear-gradient(90deg, transparent, #D4AF37, transparent);
  }}
  .cover-hero-container {{
    width: 100%;
    position: relative;
    margin: 8pt 0;
  }}
  .cover-hero-img {{
    width: 100%;
    max-height: 410pt;
    object-fit: cover;
    border-radius: 12pt;
    box-shadow: 0 16pt 35pt rgba(0,0,0,0.85);
    border: 1px solid rgba(212, 175, 55, 0.35);
  }}
  .cover-badge-bar {{
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(90deg, rgba(212, 175, 55, 0.12) 0%, rgba(212, 175, 55, 0.28) 50%, rgba(212, 175, 55, 0.12) 100%);
    border: 1px solid rgba(212, 175, 55, 0.55);
    border-radius: 30pt;
    padding: 7.5pt 24pt;
    box-shadow: 0 4pt 15pt rgba(0,0,0,0.5);
    margin-bottom: 5pt;
  }}
  .cover-badge-text {{
    font-family: 'Montserrat', sans-serif;
    font-size: 10.5pt;
    font-weight: 700;
    letter-spacing: 3pt;
    text-transform: uppercase;
    color: #FFF2D1;
  }}

  /* PAGE 2: EXPLORE THE FLEET CATEGORIES */
  .category-showcase-container {{
    display: flex;
    flex-direction: column;
    gap: 12pt;
    flex: 1;
    justify-content: space-around;
  }}
  .category-card {{
    background: linear-gradient(135deg, rgba(24, 28, 36, 0.9) 0%, rgba(12, 14, 18, 0.96) 100%);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 12pt;
    padding: 12pt 16pt;
    display: flex;
    align-items: center;
    gap: 16pt;
    box-shadow: 0 8pt 20pt rgba(0,0,0,0.5);
    position: relative;
    overflow: hidden;
  }}
  .category-card::before {{
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4pt;
    background: linear-gradient(180deg, #ECC880 0%, #D4AF37 50%, #8A6818 100%);
  }}
  .category-img-container {{
    width: 100pt;
    height: 100pt;
    border-radius: 50%;
    border: 2.5pt solid #D4AF37;
    box-shadow: 0 0 15pt rgba(212, 175, 55, 0.35);
    overflow: hidden;
    flex-shrink: 0;
  }}
  .category-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .category-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 4.5pt;
  }}
  .category-title {{
    font-family: 'Cinzel', serif;
    font-size: 13pt;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 1pt;
  }}
  .category-desc {{
    font-size: 8pt;
    color: #CBD2E0;
    line-height: 1.45;
  }}
  .category-models {{
    font-size: 7.2pt;
    color: #ECC880;
    font-weight: 600;
    letter-spacing: 0.5pt;
  }}

  /* PAGE 14: BACK COVER */
  .back-cover {{
    justify-content: space-between;
    align-items: center;
    text-align: center;
    padding: 26pt 24pt;
    background: radial-gradient(circle at 50% 30%, #1a1e27 0%, #090a0e 70%, #020304 100%);
  }}
  .back-brand-box {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8pt;
  }}
  .back-logo-img {{
    width: 180pt;
    height: auto;
    object-fit: contain;
  }}
  .back-tagline {{
    font-family: 'Cinzel', serif;
    font-size: 13.5pt;
    font-weight: 700;
    letter-spacing: 2.5pt;
    color: #FFF2CE;
    text-transform: uppercase;
  }}

  .contact-grid {{
    width: 100%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12pt;
    margin: 10pt 0;
    text-align: left;
  }}
  .contact-card {{
    background: linear-gradient(135deg, rgba(23, 26, 33, 0.9) 0%, rgba(12, 14, 18, 0.96) 100%);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 9pt;
    padding: 10pt 12pt;
    display: flex;
    flex-direction: column;
    gap: 4pt;
  }}
  .contact-label {{
    font-size: 6.8pt;
    font-weight: 700;
    color: #ECC880;
    letter-spacing: 1pt;
    text-transform: uppercase;
  }}
  .contact-val {{
    font-size: 8.2pt;
    font-weight: 600;
    color: #FFFFFF;
    line-height: 1.35;
  }}
  .contact-val a {{
    color: #FFFFFF;
    text-decoration: none;
  }}

  .qr-box {{
    background: linear-gradient(135deg, rgba(24, 28, 36, 0.95) 0%, rgba(12, 14, 18, 0.98) 100%);
    border: 1.5pt solid rgba(212, 175, 55, 0.45);
    border-radius: 12pt;
    padding: 12pt 20pt;
    display: flex;
    align-items: center;
    gap: 16pt;
    box-shadow: 0 6pt 20pt rgba(0,0,0,0.6);
  }}
  .qr-img-wrapper {{
    background: #FFFFFF;
    padding: 5pt;
    border-radius: 8pt;
    border: 1.5pt solid #D4AF37;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .qr-img {{
    width: 75pt;
    height: 75pt;
    object-fit: contain;
  }}
  .qr-info {{
    text-align: left;
    display: flex;
    flex-direction: column;
    gap: 4pt;
  }}
  .qr-title {{
    font-family: 'Cinzel', serif;
    font-size: 11pt;
    font-weight: 800;
    color: #ECC880;
    letter-spacing: 1pt;
  }}
  .qr-desc {{
    font-size: 7.8pt;
    color: #CBD2E0;
    line-height: 1.4;
  }}
  .social-pill {{
    display: inline-flex;
    align-items: center;
    gap: 5pt;
    background: rgba(212, 175, 55, 0.15);
    border: 1px solid rgba(212, 175, 55, 0.4);
    border-radius: 4pt;
    padding: 3pt 8pt;
    font-size: 7.2pt;
    font-weight: 700;
    color: #FFF2CE;
    width: fit-content;
    margin-top: 3pt;
  }}

  .checklist-strip {{
    width: 100%;
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(212, 175, 55, 0.2);
    border-radius: 8pt;
    padding: 8pt 12pt;
    display: flex;
    justify-content: space-around;
    font-size: 6.8pt;
    color: #A0A6B5;
    letter-spacing: 0.5pt;
  }}
  .checklist-item strong {{
    color: #ECC880;
  }}

</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover">
  <div class="cover-logo-wrapper">
    <div class="cover-logo-circle">
      <img src="{logo_b64}" class="cover-logo-img" alt="RevvRizz Logo">
    </div>
    <div class="cover-title">
      <div class="gold-divider"></div>
      <span class="gold-gradient-text">Luxury Cars & Sports Bikes</span>
      <div class="gold-divider"></div>
    </div>
  </div>

  <div class="cover-hero-container">
    <img src="{hero_b64}" class="cover-hero-img" alt="Hero Cars">
  </div>

  <div class="cover-badge-bar">
    <span class="cover-badge-text">Self-Drive Rentals &bull; With Chauffeur &bull; Events & Weddings</span>
  </div>
</div>

<!-- PAGE 2: EXPLORE THE FLEET OVERVIEW -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Premium Vehicle Categories</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">✦ Handpicked Premium Fleet</div>
    </div>
  </div>

  <div class="category-showcase-container">
    <!-- Cat 1 -->
    <div class="category-card">
      <div class="category-img-container">
        <img src="{cat_economic_b64}" class="category-img" alt="Economic Cars">
      </div>
      <div class="category-content">
        <div class="category-title gold-gradient-text">Economic & Compact Cars</div>
        <div class="category-desc">Looking for an affordable, high-efficiency ride? Choose from our curated range of budget-friendly self-drive cars offering exceptional mileage, easy city handling, and reliable comfort for daily commutes and family trips.</div>
        <div class="category-models"><strong>FEATURED MODELS:</strong> Baleno &bull; Glanza &bull; Kia Carens &bull; Ertiga &bull; Fronx &bull; Brezza &bull; Swift</div>
      </div>
    </div>

    <!-- Cat 2 -->
    <div class="category-card">
      <div class="category-img-container">
        <img src="{cat_suvs_b64}" class="category-img" alt="SUVs">
      </div>
      <div class="category-content">
        <div class="category-title gold-gradient-text">SUVs & Premium Off-Roaders</div>
        <div class="category-desc">Spacious, bold, and commanding. Refined comfort built for business travel, mountain expeditions, family getaways, and rugged long-distance highway journeys with unmatched road presence and 4x4 capability.</div>
        <div class="category-models"><strong>FEATURED MODELS:</strong> Mahindra Thar (RWD & 4x4) &bull; Scorpio N &bull; Creta &bull; Fortuner &bull; Innova Hycross &bull; XUV 700</div>
      </div>
    </div>

    <!-- Cat 3 -->
    <div class="category-card">
      <div class="category-img-container">
        <img src="{cat_exec_b64}" class="category-img" alt="Executive Cars">
      </div>
      <div class="category-content">
        <div class="category-title gold-gradient-text">Executive Sedans & Supercars</div>
        <div class="category-desc">Arrive in grand style. Elegant German sedans, open-top convertibles, and exotic sports cars tailored for VIP arrivals, pre-wedding photoshoots, luxury weddings, red carpet galas, and momentous celebrations.</div>
        <div class="category-models"><strong>FEATURED MODELS:</strong> Rolls-Royce Ghost &bull; Lamborghini Huracán &bull; Porsche Boxster &bull; BMW Z4 &bull; Mercedes CLE &bull; Audi A6</div>
      </div>
    </div>

    <!-- Cat 4 -->
    <div class="category-card">
      <div class="category-img-container">
        <img src="{cat_bikes_b64}" class="category-img" alt="Sports Bikes">
      </div>
      <div class="category-content">
        <div class="category-title gold-gradient-text">Sports Bikes & Adventure Touring</div>
        <div class="category-desc">Discover pure adrenaline on two wheels. Experience world-class superbikes and tour-ready adventure motorcycles engineered for track exhilaration, weekend highway cruising, and unforgettable open-road escapes.</div>
        <div class="category-models"><strong>FEATURED MODELS:</strong> Suzuki Hayabusa &bull; Kawasaki ZX-10R &bull; Z900 &bull; BMW R 1300GS &bull; Triumph Daytona 660 &bull; Aprilia RS 457</div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 02 &bull; Category Fleet Overview</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 3: ECONOMIC CARS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Economic Cars &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 12 Hrs : 100 KMs Limit</div>
      <div class="limit-badge">⚡ 24 Hrs : 250 KMs Limit</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Baleno Petrol -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Maruti Suzuki - Baleno</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2024</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 1,800/-</td>
            <td class="rate">₹ 2,000/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 2,300/-</td>
            <td class="rate rate-gold">₹ 2,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('baleno_petrol.png')}" class="car-img" alt="Baleno Petrol">
      </div>
    </div>

    <!-- Card 2: Baleno CNG -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Maruti Suzuki - Baleno (CNG)</div>
          <div class="car-pill">Petrol + CNG</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Transmission: <strong>Manual</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td>--</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 2,700/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('baleno_cng.png')}" class="car-img" alt="Baleno CNG">
      </div>
    </div>

    <!-- Card 3: Ertiga CNG -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Maruti Suzuki - Ertiga (CNG)</div>
          <div class="car-pill">Petrol + CNG &bull; 7 Seater</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2023</strong></div>
          <div class="spec-tag">Transmission: <strong>Manual</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 2,700/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 3,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('ertiga_cng.png')}" class="car-img" alt="Ertiga CNG">
      </div>
    </div>

    <!-- Card 4: Kia Carens Diesel -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Kia Carens (Diesel)</div>
          <div class="car-pill">Diesel &bull; 7 Seater</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2025</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 3,000/-</td>
            <td class="rate">₹ 3,200/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 4,000/-</td>
            <td class="rate rate-gold">₹ 4,200/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 7,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('carens_diesel.png')}" class="car-img" alt="Kia Carens Diesel">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 03 &bull; Economic Cars Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 4: ECONOMIC CARS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Economic Cars &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 12 Hrs : 100 KMs Limit</div>
      <div class="limit-badge">⚡ 24 Hrs : 250 KMs Limit</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Toyota Glanza -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Toyota Glanza</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2025</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 2,000/-</td>
            <td class="rate">₹ 2,200/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 2,500/-</td>
            <td class="rate rate-gold">₹ 2,700/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('glanza_petrol.png')}" class="car-img" alt="Toyota Glanza">
      </div>
    </div>

    <!-- Card 2: Toyota Glanza CNG -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Toyota Glanza (CNG)</div>
          <div class="car-pill">Petrol + CNG</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Transmission: <strong>Manual</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td>--</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 2,800/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('glanza_cng.png')}" class="car-img" alt="Glanza CNG">
      </div>
    </div>

    <!-- Card 3: Brezza -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Maruti Suzuki - Brezza</div>
          <div class="car-pill">Petrol &bull; Compact SUV</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2024</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2024</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 3,000/-</td>
            <td class="rate">₹ 3,300/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 4,000/-</td>
            <td class="rate rate-gold">₹ 4,300/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 7,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('brezza.png')}" class="car-img" alt="Maruti Brezza">
      </div>
    </div>

    <!-- Card 4: Taisor -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Toyota Urban Cruiser - Taisor</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2024</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td>--</td>
            <td>--</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 3,200/-</td>
            <td class="rate rate-gold">₹ 3,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('taisor.png')}" class="car-img" alt="Toyota Taisor">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 04 &bull; Economic Cars Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 5: ECONOMIC CARS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Economic Cars &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 12 Hrs : 100 KMs Limit</div>
      <div class="limit-badge">⚡ 24 Hrs : 250 KMs Limit</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Fronx -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Maruti Suzuki - Fronx</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2024</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 2,500/-</td>
            <td class="rate">₹ 2,800/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 3,200/-</td>
            <td class="rate rate-gold">₹ 3,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('fronx.png')}" class="car-img" alt="Maruti Fronx">
      </div>
    </div>

    <!-- Card 2: Rumion CNG -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Toyota Rumion (CNG)</div>
          <div class="car-pill">Petrol + CNG &bull; 7 Seater</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Transmission: <strong>Manual</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td>--</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 4,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('rumion_cng.png')}" class="car-img" alt="Toyota Rumion">
      </div>
    </div>

    <!-- Card 3: Swift -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Maruti Suzuki - Swift</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2024</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2024</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 2,000/-</td>
            <td class="rate">₹ 2,300/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 2,500/-</td>
            <td class="rate rate-gold">₹ 2,700/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('swift.png')}" class="car-img" alt="Maruti Swift">
      </div>
    </div>

    <!-- Card 4: Carens Clavis -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Kia Carens Clavis</div>
          <div class="car-pill">Petrol &bull; 7 Seater</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2025</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td>--</td>
            <td>--</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 3,200/-</td>
            <td class="rate rate-gold">₹ 3,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('carens_clavis.png')}" class="car-img" alt="Kia Carens Clavis">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 05 &bull; Economic Cars Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 6: SUVS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">SUVs & Off-Roaders &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 12 Hrs : 100 KMs Limit</div>
      <div class="limit-badge">⚡ 24 Hrs : 250 KMs Limit</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Creta -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Hyundai - Creta</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2025</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 3,800/-</td>
            <td class="rate">₹ 4,000/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 5,000/-</td>
            <td class="rate rate-gold">₹ 5,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 7,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('creta.png')}" class="car-img" alt="Hyundai Creta">
      </div>
    </div>

    <!-- Card 2: Thar Black 4x2 & 4x4 -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mahindra Thar (Black) - RWD & 4x4</div>
          <div class="car-pill">Diesel / Petrol</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Variant</th>
            <th>Transmission</th>
            <th>12 Hours</th>
            <th>24 Hours</th>
          </tr>
          <tr>
            <td>4x2 RWD (Diesel)</td>
            <td>Manual '25</td>
            <td class="rate">₹ 3,800/-</td>
            <td class="rate rate-gold">₹ 5,000/-</td>
          </tr>
          <tr>
            <td>4x4 Hard Top (Petrol)</td>
            <td>Manual '24</td>
            <td class="rate">₹ 4,200/-</td>
            <td class="rate rate-gold">₹ 5,500/-</td>
          </tr>
          <tr>
            <td>4x2 RWD (Diesel)</td>
            <td>Automatic '25</td>
            <td class="rate">₹ 4,000/-</td>
            <td class="rate rate-gold">₹ 5,500/-</td>
          </tr>
          <tr>
            <td>4x4 Hard Top (Petrol)</td>
            <td>Automatic '25</td>
            <td class="rate">₹ 4,500/-</td>
            <td class="rate rate-gold">₹ 6,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 10,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('thar_black.png')}" class="car-img" alt="Mahindra Thar Black">
      </div>
    </div>

    <!-- Card 3: Thar White -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mahindra Thar (White) - RWD & 4x4</div>
          <div class="car-pill">Diesel</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual Model: <strong>2025</strong></div>
          <div class="spec-tag">Automatic Model: <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 4,000/-</td>
            <td class="rate">₹ 4,500/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 6,500/-</td>
            <td class="rate rate-gold">₹ 7,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 10,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('thar_white.png')}" class="car-img" alt="Mahindra Thar White">
      </div>
    </div>

    <!-- Card 4: Scorpio N -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mahindra - Scorpio N</div>
          <div class="car-pill">Diesel / Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Manual (Diesel): <strong>2024</strong></div>
          <div class="spec-tag">Automatic (Petrol): <strong>2025</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Manual</th>
            <th>Automatic</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 4,000/-</td>
            <td class="rate">₹ 4,500/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 6,500/-</td>
            <td class="rate rate-gold">₹ 7,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 10,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('scorpio_n.png')}" class="car-img" alt="Mahindra Scorpio N">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 06 &bull; SUVs Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 7: SUVS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">SUVs & MPVs &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 12 Hrs : 100 KMs Limit</div>
      <div class="limit-badge">⚡ 24 Hrs : 250 KMs Limit</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Venue -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Hyundai - Venue</div>
          <div class="car-pill">Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Transmission: <strong>Manual</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 3,000/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 4,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 5,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('venue.png')}" class="car-img" alt="Hyundai Venue">
      </div>
    </div>

    <!-- Card 2: Innova Hycross -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Toyota - Innova Hycross</div>
          <div class="car-pill">Petrol Hybrid &bull; Luxury MPV</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Transmission: <strong>Automatic</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td>--</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 7,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 10,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('innova_hycross.png')}" class="car-img" alt="Toyota Innova Hycross">
      </div>
    </div>

    <!-- Card 3: Fortuner -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Toyota Fortuner - 4x2 & 4x4</div>
          <div class="car-pill">Diesel / Petrol</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Variant</th>
            <th>Transmission</th>
            <th>12 Hours</th>
            <th>24 Hours</th>
            <th>Deposit</th>
          </tr>
          <tr>
            <td>4x2 Diesel/Petrol</td>
            <td>Manual '23</td>
            <td class="rate">₹ 9,000/-</td>
            <td class="rate rate-gold">₹ 12,000/-</td>
            <td>₹ 15k</td>
          </tr>
          <tr>
            <td>4x4 Petrol</td>
            <td>Manual '25</td>
            <td class="rate">₹ 11,500/-</td>
            <td class="rate rate-gold">₹ 13,500/-</td>
            <td>₹ 20k</td>
          </tr>
          <tr>
            <td>4x2 Diesel/Petrol</td>
            <td>Automatic '24</td>
            <td class="rate">₹ 10,000/-</td>
            <td class="rate rate-gold">₹ 12,500/-</td>
            <td>₹ 15k</td>
          </tr>
          <tr>
            <td>4x4 Diesel</td>
            <td>Automatic '25</td>
            <td class="rate">₹ 12,000/-</td>
            <td class="rate rate-gold">₹ 15,000/-</td>
            <td>₹ 20k</td>
          </tr>
        </table>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('fortuner.png')}" class="car-img" alt="Toyota Fortuner">
      </div>
    </div>

    <!-- Card 4: XUV 700 -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mahindra - XUV 700 (AX7L)</div>
          <div class="car-pill">Petrol &bull; Flagship Luxury</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Transmission: <strong>Automatic</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>12 Hours</td>
            <td class="rate">₹ 5,500/-</td>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 7,500/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 10,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('xuv_700.png')}" class="car-img" alt="Mahindra XUV 700">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 07 &bull; SUVs & MPVs Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 8: LUXURY SEDANS & PREMIUM SUVS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Luxury Sedans & Premium SUVs &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">✦ 1 Day : 180 KMs</div>
      <div class="limit-badge">✦ 2 Days : 400 KMs</div>
      <div class="limit-badge">✦ 3 Days : Unlimited KMs</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Mercedes E220d -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mercedes-Benz - E220d LWB</div>
          <div class="car-pill">Automatic &bull; Diesel</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2022</strong></div>
          <div class="spec-tag">Executive Long Wheelbase</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 25,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 70,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('mercedes_e220d.png')}" class="car-img" alt="Mercedes E220d">
      </div>
    </div>

    <!-- Card 2: Mercedes C300 Cabriolet -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mercedes-Benz - C300 Cabriolet</div>
          <div class="car-pill">Automatic &bull; Convertible</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2021</strong></div>
          <div class="spec-tag">Fuel: <strong>Petrol</strong></div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 55,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 2,00,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('mercedes_c300_cabrio.png')}" class="car-img" alt="Mercedes C300 Cabriolet">
      </div>
    </div>

    <!-- Card 3: BMW 520d -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">BMW - 520d</div>
          <div class="car-pill">Automatic &bull; Diesel</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2020</strong></div>
          <div class="spec-tag">Sport Executive Sedan</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 20,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 70,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('bmw_520d.png')}" class="car-img" alt="BMW 520d">
      </div>
    </div>

    <!-- Card 4: Audi A6 -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Audi - A6</div>
          <div class="car-pill">Automatic &bull; Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2023</strong></div>
          <div class="spec-tag">Matrix LED &bull; Virtual Cockpit</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 20,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 70,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('audi_a6.png')}" class="car-img" alt="Audi A6">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 08 &bull; Luxury Sedans Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 9: PREMIUM SUVS & LUXURY SEDANS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Premium SUVs & Luxury Sedans &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">✦ 1 Day : 180 KMs</div>
      <div class="limit-badge">✦ 2 Days : 400 KMs</div>
      <div class="limit-badge">✦ 3 Days : Unlimited KMs</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Audi Q7 -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Audi - Q7 Quattro</div>
          <div class="car-pill">Automatic &bull; Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2024</strong></div>
          <div class="spec-tag">Quattro AWD &bull; 7 Seater Luxury</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 35,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 1,00,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('audi_q7.png')}" class="car-img" alt="Audi Q7">
      </div>
    </div>

    <!-- Card 2: BMW X1 -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">BMW - X1</div>
          <div class="car-pill">Automatic &bull; Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2021</strong></div>
          <div class="spec-tag">Panoramic Sunroof &bull; Sport Line</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 15,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 50,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('bmw_x1.png')}" class="car-img" alt="BMW X1">
      </div>
    </div>

    <!-- Card 3: Jeep Wrangler Rubicon -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Jeep Wrangler - Soft Top (Rubicon)</div>
          <div class="car-pill">Automatic &bull; Diesel 4x4</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2022</strong></div>
          <div class="spec-tag">Trail Rated &bull; Open-Air Freedom</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Duration</th>
            <th>Rental Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day)</td>
            <td class="rate rate-gold">₹ 35,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 1,50,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('jeep_wrangler.png')}" class="car-img" alt="Jeep Wrangler Rubicon">
      </div>
    </div>

    <!-- Card 4: Defender -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Land Rover - Defender (Min. 3 Days)</div>
          <div class="car-pill">Automatic &bull; Petrol</div>
        </div>
        <div class="car-specs-row">
          <div class="spec-tag">Model Year: <strong>2025</strong></div>
          <div class="spec-tag">Air Suspension &bull; Flagship Icon</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Rental Package</th>
            <th>Rate</th>
          </tr>
          <tr>
            <td>24 Hours (1 Day with Chauffeur)</td>
            <td class="rate">₹ 65,000/-</td>
          </tr>
          <tr>
            <td>72 Hours (3 Days Self Drive)</td>
            <td class="rate rate-gold">₹ 1,90,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Refundable Security Deposit: <span>₹ 2,50,000/-</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('defender.png')}" class="car-img" alt="Land Rover Defender">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 09 &bull; Premium SUVs Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 10: EXECUTIVE CARS & SPORTS CARS (PHOTOSHOOTS & EVENTS) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Executive & Sports Cars &bull; Photoshoots, Weddings & Events</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">★ Garage to Garage (G2G)</div>
      <div class="limit-badge-alt">Tolls & Taxes Excluded</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: Mercedes CLE 300 Cabriolet AMG -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mercedes-CLE 300 Cabriolet AMG</div>
          <div class="car-pill">Automatic &bull; 2026 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package</th>
            <th>With Chauffeur (Fuel Incl.)</th>
            <th>Self-Drive (Min. 3 Days)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 65,000/-</td>
            <td rowspan="2" class="rate rate-gold">₹ 65,000/- / Day<br><span style="font-size:5.8pt; color:#A6ACB8;">(Fuel Not Incl.)</span></td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate">₹ 70,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Security Deposit: <span>₹ 0 (Chauffeur)</span> &bull; <span>₹ 5,00,000 (Self-Drive)</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('mercedes_cle300_amg.png')}" class="car-img" alt="Mercedes CLE 300 AMG">
      </div>
    </div>

    <!-- Card 2: Mercedes C300 Cabriolet Events -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Mercedes-C300 Cabriolet</div>
          <div class="car-pill">With Driver &bull; 2022 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 22,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 25,000/-</td>
          </tr>
        </table>
        <div class="car-specs-row" style="margin-top:2pt;">
          <div class="spec-tag">Extra per Hour: <strong>₹ 2,000</strong></div>
          <div class="spec-tag">Extra per KM: <strong>₹ 250</strong></div>
        </div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('mercedes_c300_cabrio_events.png')}" class="car-img" alt="Mercedes C300 Cabriolet">
      </div>
    </div>

    <!-- Card 3: Audi A3 Cabriolet -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Audi A3 Cabriolet</div>
          <div class="car-pill">With Driver &bull; 2022 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 18,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 22,000/-</td>
          </tr>
        </table>
        <div class="car-specs-row" style="margin-top:2pt;">
          <div class="spec-tag">Extra per Hour: <strong>₹ 1,800</strong></div>
          <div class="spec-tag">Extra per KM: <strong>₹ 220</strong></div>
        </div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('audi_a3_cabrio.png')}" class="car-img" alt="Audi A3 Cabriolet">
      </div>
    </div>

    <!-- Card 4: GMC Hummer -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">GMC Hummer</div>
          <div class="car-pill">With Driver &bull; 2016 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 50,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 60,000/-</td>
          </tr>
        </table>
        <div class="car-specs-row" style="margin-top:2pt;">
          <div class="spec-tag">Extra per Hour: <strong>₹ 5,000</strong></div>
          <div class="spec-tag">Extra per KM: <strong>₹ 500</strong></div>
        </div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('gmc_hummer.png')}" class="car-img" alt="GMC Hummer">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 10 &bull; Executive Cars & Events Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 11: SUPERCARS & ULTRA-LUXURY (EVENTS & PHOTOSHOOTS) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Supercars & Ultra-Luxury &bull; Photoshoots, Weddings & Events</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">★ Garage to Garage (G2G)</div>
      <div class="limit-badge-alt">Tolls & Taxes Excluded</div>
    </div>
  </div>

  <div class="car-cards-container">
    <!-- Card 1: BMW Z4 -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">BMW - Z4 Roadster</div>
          <div class="car-pill">With Driver &bull; 2024 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 1,11,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 1,22,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Flagship Luxury &bull; <span>VIP Chauffeur Included</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('bmw_z4.png')}" class="car-img" alt="BMW Z4">
      </div>
    </div>

    <!-- Card 2: Porsche Boxster -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Porsche Boxster</div>
          <div class="car-pill">With Driver &bull; 2019 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 1,00,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 1,15,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">Mid-Engine Sports Car &bull; <span>Exotic Convertible</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('porsche_boxster.png')}" class="car-img" alt="Porsche Boxster">
      </div>
    </div>

    <!-- Card 3: Lamborghini Huracan Spyder -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Lamborghini Huracán Spyder</div>
          <div class="car-pill">With Driver &bull; 2023 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 2,00,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 2,20,000/-</td>
          </tr>
        </table>
        <div class="deposit-badge">V10 Supercar Exhilaration &bull; <span>Pure Red Carpet Presence</span></div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('lamborghini_huracan.png')}" class="car-img" alt="Lamborghini Huracan Spyder">
      </div>
    </div>

    <!-- Card 4: Rolls-Royce Ghost -->
    <div class="car-card">
      <div class="car-info">
        <div class="car-header">
          <div class="car-name">Rolls-Royce Ghost</div>
          <div class="car-pill">With Driver &bull; 2016 Model</div>
        </div>
        <table class="pricing-table">
          <tr>
            <th>Package (G2G)</th>
            <th>Rental Rate (Fuel & Driver Incl.)</th>
          </tr>
          <tr>
            <td>8 Hours / 80 KMs</td>
            <td class="rate">₹ 2,00,000/-</td>
          </tr>
          <tr>
            <td>12 Hours / 100 KMs</td>
            <td class="rate rate-gold">₹ 2,20,000/-</td>
          </tr>
        </table>
        <div class="car-specs-row" style="margin-top:2pt;">
          <div class="spec-tag">Extra per Hour: <strong>₹ 5,000</strong></div>
          <div class="spec-tag">Extra per KM: <strong>₹ 500</strong></div>
        </div>
      </div>
      <div class="car-showcase">
        <img src="{img_b64('rolls_royce_ghost.png')}" class="car-img" alt="Rolls-Royce Ghost">
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 11 &bull; Supercars & Ultra-Luxury Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 12: SPORTS BIKES & ADVENTURE BIKES (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Sports Bikes & Superbikes &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 1 Day : 100 KMs (Super Bikes)</div>
      <div class="limit-badge">⚡ 1 Day : 180 KMs (Sports Bikes)</div>
    </div>
  </div>

  <div class="bike-grid">
    <!-- Bike 1: BMW G310-RR -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('bmw_g310_rr.png')}" class="bike-photo" alt="BMW G310-RR">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">BMW G310-RR</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2024</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 2,100/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 15,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 2: BMW G310-R -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('bmw_g310_r.png')}" class="bike-photo" alt="BMW G310-R">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">BMW G310-R</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2023</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 1,900/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 10,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 3: Suzuki Hayabusa -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('suzuki_hayabusa.png')}" class="bike-photo" alt="Suzuki Hayabusa">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Suzuki - Hayabusa 1300</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2021</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 11,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 50,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 4: Kawasaki Ninja ZX-10R -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('kawasaki_zx10r.png')}" class="bike-photo" alt="Kawasaki Ninja ZX-10R">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Kawasaki Ninja ZX-10R</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2024</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 20,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 50,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 5: Aprilia RS 457 -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('aprilia_rs457.png')}" class="bike-photo" alt="Aprilia RS 457">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Aprilia - RS 457</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2024</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 5,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 20,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 6: Triumph Daytona 660 -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('triumph_daytona660.png')}" class="bike-photo" alt="Triumph Daytona 660">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Triumph Daytona 660</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2024</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 9,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 30,000/-</strong></div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 12 &bull; Sports Bikes Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 13: ADVENTURE BIKES & NAKED STREETFIGHTERS (SELF-DRIVE) -->
<div class="page">
  <div class="page-header">
    <div class="header-titles">
      <div class="header-main-title gold-gradient-text">Explore The Fleet</div>
      <div class="header-sub-title">Adventure Bikes & Naked Street &bull; Self-Drive</div>
    </div>
    <div class="header-limits">
      <div class="limit-badge">⚡ 1 Day : 180 KMs (Adventure Bikes)</div>
      <div class="limit-badge">⚡ 1 Day : 180 KMs (Street Bikes)</div>
    </div>
  </div>

  <div class="bike-grid">
    <!-- Bike 1: BMW R 1300GS -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('bmw_r1300gs.png')}" class="bike-photo" alt="BMW R 1300GS">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">BMW R 1300GS</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2024</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 15,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 50,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 2: KTM Adventure 390 -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('ktm_adventure390.png')}" class="bike-photo" alt="KTM Adventure 390">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">KTM Adventure 390</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2025</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 3,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 15,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 3: Himalayan 411 -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('himalayan411.png')}" class="bike-photo" alt="Royal Enfield Himalayan 411">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Royal Enfield Himalayan 411</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2022</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 1,500/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 7,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 4: Triumph Speed 400 -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('triumph_speed400.png')}" class="bike-photo" alt="Triumph Speed 400">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Triumph Speed 400</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2025</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 2,000/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 12,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 5: Kawasaki Z900 (New) -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('kawasaki_z900_new.png')}" class="bike-photo" alt="Kawasaki Z900 (New)">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Kawasaki Z900 (New)</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2024</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 9,500/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 30,000/-</strong></div>
      </div>
    </div>

    <!-- Bike 6: Kawasaki Z900 (Old) -->
    <div class="bike-card">
      <div class="bike-photo-container">
        <img src="{img_b64('kawasaki_z900_old.png')}" class="bike-photo" alt="Kawasaki Z900 (Old)">
      </div>
      <div class="bike-info-box">
        <div class="bike-title">Kawasaki Z900 (Old)</div>
        <div class="bike-spec-pill-row">
          <div class="bike-pill">Year: 2021</div>
          <div class="bike-pill">Fuel: Petrol</div>
        </div>
        <div class="bike-pricing-strip">
          <div class="bike-rate-label">24 Hrs Rent (1 Day)</div>
          <div class="bike-rate-value gold-gradient-text">₹ 8,500/-</div>
        </div>
        <div class="bike-deposit">Refundable Security Deposit: <strong>₹ 30,000/-</strong></div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 13 &bull; Adventure Bikes Fleet</div>
    <div>Delhi NCR</div>
  </div>
</div>

<!-- PAGE 14: BACK COVER / BOOKING & CONTACT -->
<div class="page back-cover">
  <div class="back-brand-box">
    <img src="{logo_b64}" class="back-logo-img" alt="RevvRizz Luxe">
    <div class="back-tagline">The Art of Luxury Motoring</div>
  </div>

  <!-- CONTACT GRID -->
  <div class="contact-grid">
    <div class="contact-card">
      <div class="contact-label">📞 Booking Hotline & WhatsApp</div>
      <div class="contact-val"><a href="tel:+919289678449">+91 9289678449</a><br><a href="tel:+919540928227">+91 9540928227</a></div>
    </div>
    <div class="contact-card">
      <div class="contact-label">✉️ Official Email</div>
      <div class="contact-val"><a href="mailto:revvrizzofficial@gmail.com">revvrizzofficial@gmail.com</a></div>
    </div>
    <div class="contact-card" style="grid-column: span 2;">
      <div class="contact-label">📍 Office Address</div>
      <div class="contact-val"><a href="https://maps.google.com/?q=11+Hargobind+Enclave+Delhi+110092" target="_blank">Inside Cocoweave Coworking, 11 Hargobind Enclave, Near Karkardooma Metro Station, opp. Metro Pillar 118, Delhi, 110092</a></div>
    </div>
  </div>

  <!-- QR CODE BOX -->
  <div class="qr-box">
    <div class="qr-img-wrapper">
      <img src="{qr_b64}" class="qr-img" alt="Instagram QR Code">
    </div>
    <div class="qr-info">
      <div class="qr-title">Connect On Instagram</div>
      <div class="qr-desc">Scan to follow us on Instagram for daily fleet stories, exclusive offers, supercars showcase & instant bookings.</div>
      <div class="social-pill">
        <a href="https://instagram.com/revvrizzluxe" target="_blank" style="color:inherit; text-decoration:none;">📸 @revvrizzluxe</a> &bull; <a href="https://instagram.com/revvrizz" target="_blank" style="color:inherit; text-decoration:none;">📸 @revvrizz</a>
      </div>
    </div>
  </div>

  <!-- CHECKLIST STRIP -->
  <div class="checklist-strip">
    <div class="checklist-item"><strong>✓ Documents:</strong> Original DL & Aadhaar / Passport</div>
    <div class="checklist-item"><strong>✓ 24x7 Support:</strong> Pan-Delhi NCR Roadside Assistance</div>
    <div class="checklist-item"><strong>✓ Fast Delivery:</strong> Doorstep Delivery Available</div>
  </div>

  <div class="page-footer" style="width: 100%;">
    <div class="footer-brand">RevvRizz Luxe Pvt Ltd</div>
    <div>Page 14 &bull; Contact & Reservations</div>
    <div>Delhi &bull; NCR &bull; Pan-India</div>
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(WORKSPACE_DIR, "catalog_rendered.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML successfully generated at: {html_path}")

# Now render PDF via Playwright Chromium
pdf_out = os.path.join(WORKSPACE_DIR, "REVVRIZZ_CATALOG_REDESIGNED.pdf")
print("Launching Chromium to generate PDF...")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
    # Wait for fonts to render
    page.wait_for_timeout(2000)
    page.pdf(
        path=pdf_out,
        print_background=True,
        prefer_css_page_size=True
    )
    browser.close()

size_mb = os.path.getsize(pdf_out) / (1024 * 1024)
print(f"PDF generated successfully at: {pdf_out} (Size: {size_mb:.2f} MB)")
