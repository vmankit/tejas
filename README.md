# RevvRizz Luxe - Luxury Automotive & Superbike Rentals Delhi NCR

A state-of-the-art luxury rental web application and fleet management platform for **RevvRizz Luxe Pvt Ltd** (Delhi NCR).

---

## 🌟 Features

- **48+ Premium Machines**: Complete fleet covering Economic Cars, Compact & Full-size SUVs (Thar, Scorpio N, Defender, Fortuner), Executive Sedans (Mercedes, BMW, Audi), Red Carpet Convertibles & Exotics (Rolls-Royce Ghost, Lamborghini Huracán), and High-Performance Superbikes (Suzuki Hayabusa, Kawasaki ZX-10R, BMW R 1300GS).
- **Instant Rental Cost Estimator**: Live calculator dynamically estimating 12h, 24h, 48h, and 72h packages, mileage limits, and doorstep delivery addons.
- **Deep Obsidian & Liquid Gold Design System**: High-contrast glassmorphism, responsive micro-animations, and fluid typography.
- **Vehicle Details Modal**: Interactive full-screen inspection modal with instant rate breakdown, specifications, and 1-click WhatsApp reservation.
- **Direct WhatsApp Concierge Integration**: Pre-filled booking messages routing straight to the 24/7 concierge hotline.
- **100% Mobile & Desktop Responsive**: Tested across desktop viewports and modern mobile screens.

---

## 🛠️ Project Structure

```text
tejas/
├── index.html              # Main application markup & landing experience
├── styles.css              # Master styling & responsive design system
├── app.js                  # Frontend fleet rendering, filtering, modal & calculator logic
├── generate_app_js.py      # Source catalog compiler (generates app.js)
├── assets/                 # High-resolution vehicle cutouts, logo, and icons
├── REVVRIZZ CAT.pdf        # Official verified vehicle rate catalog
├── test_website.py         # Automated Playwright test suite
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

Simply open `index.html` in any modern web browser or serve via a local HTTP server:

```bash
# Using Python built-in server:
python -m http.server 8000
```

Then visit: `http://localhost:8000`

---

## 🔄 Recompiling Fleet Catalog

When updates are made to rates, models, or terms in `generate_app_js.py`:

```bash
python generate_app_js.py
```

This compiles and updates `app.js` with the full verified fleet data.

---

## 🧪 Running Tests

To run the automated Playwright test suite:

```bash
python test_website.py
```
