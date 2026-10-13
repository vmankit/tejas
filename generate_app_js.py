import json

# Comprehensive Fleet Dataset for RevvRizz Luxe
fleet = [
  # --- ECONOMIC CARS ---
  {
    "id": "baleno-petrol",
    "name": "Maruti Suzuki Baleno",
    "brand": "Maruti Suzuki",
    "category": "economic",
    "type": "car",
    "image": "assets/baleno_petrol.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2024 / 2025",
    "rate12h": 1800,
    "rate24h": 2300,
    "deposit": 5000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "BESTSELLER",
    "isFeatured": True,
    "desc": "Delhi NCR's top choice for city comfort and superior fuel economy. Equipped with 360 camera, cruise control & spacious seating.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 1,800", "automatic": "₹ 2,000"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 2,300", "automatic": "₹ 2,500"},
      {"duration": "48 Hours (500 KMs)", "manual": "₹ 4,500", "automatic": "₹ 4,900"}
    ]
  },
  {
    "id": "baleno-cng",
    "name": "Maruti Suzuki Baleno (CNG)",
    "brand": "Maruti Suzuki",
    "category": "economic",
    "type": "car",
    "image": "assets/baleno_cng.png",
    "fuel": "Petrol + CNG",
    "transmission": "Manual",
    "seats": 5,
    "year": "2025",
    "rate12h": None,
    "rate24h": 2700,
    "deposit": 5000,
    "kmLimit": "24h: 250 km",
    "badge": "MAX SAVINGS",
    "isFeatured": False,
    "desc": "Ultra cost-effective long-distance touring with factory-fitted S-CNG. Drive up to 30 km/kg on highways.",
    "pricing": [
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 2,700", "automatic": "--"},
      {"duration": "48 Hours (500 KMs)", "manual": "₹ 5,300", "automatic": "--"}
    ]
  },
  {
    "id": "ertiga-cng",
    "name": "Maruti Suzuki Ertiga (CNG)",
    "brand": "Maruti Suzuki",
    "category": "economic",
    "type": "car",
    "image": "assets/ertiga_cng.png",
    "fuel": "Petrol + CNG",
    "transmission": "Manual",
    "seats": 7,
    "year": "2023",
    "rate12h": 2700,
    "rate24h": 3500,
    "deposit": 5000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "7 SEATER",
    "isFeatured": True,
    "desc": "Spacious 7-seater family MPV with dual AC vents, massive luggage capacity, and economical CNG running costs.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 2,700", "automatic": "--"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 3,500", "automatic": "--"},
      {"duration": "48 Hours (500 KMs)", "manual": "₹ 6,800", "automatic": "--"}
    ]
  },
  {
    "id": "carens-diesel",
    "name": "Kia Carens (Diesel)",
    "brand": "Kia",
    "category": "economic",
    "type": "car",
    "image": "assets/carens_diesel.png",
    "fuel": "Diesel",
    "transmission": "Both",
    "seats": 7,
    "year": "2025",
    "rate12h": 3000,
    "rate24h": 4000,
    "deposit": 7000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "PREMIUM 7-SEATER",
    "isFeatured": True,
    "desc": "High torque CRDi diesel engine with executive cabin luxury, reclining captain seats and connected features.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 3,000", "automatic": "₹ 3,200"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 4,000", "automatic": "₹ 4,200"}
    ]
  },
  {
    "id": "glanza-petrol",
    "name": "Toyota Glanza",
    "brand": "Toyota",
    "category": "economic",
    "type": "car",
    "image": "assets/glanza_petrol.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2025",
    "rate12h": 2000,
    "rate24h": 2500,
    "deposit": 5000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "TOYOTA RELIABILITY",
    "isFeatured": False,
    "desc": "Refined Toyota hatchback with smart hybrid tech, plush ride quality, and smooth transmission options.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 2,000", "automatic": "₹ 2,200"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 2,500", "automatic": "₹ 2,700"}
    ]
  },
  {
    "id": "glanza-cng",
    "name": "Toyota Glanza (CNG)",
    "brand": "Toyota",
    "category": "economic",
    "type": "car",
    "image": "assets/glanza_cng.png",
    "fuel": "Petrol + CNG",
    "transmission": "Manual",
    "seats": 5,
    "year": "2025",
    "rate12h": None,
    "rate24h": 2800,
    "deposit": 5000,
    "kmLimit": "24h: 250 km",
    "badge": "ECO CHOICE",
    "isFeatured": False,
    "desc": "Toyota reliability combined with factory CNG fuel system. High efficiency for inter-city travel.",
    "pricing": [
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 2,800", "automatic": "--"}
    ]
  },
  {
    "id": "brezza",
    "name": "Maruti Suzuki Brezza",
    "brand": "Maruti Suzuki",
    "category": "economic",
    "type": "car",
    "image": "assets/brezza.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2024",
    "rate12h": 3000,
    "rate24h": 4000,
    "deposit": 7000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "COMPACT SUV",
    "isFeatured": False,
    "desc": "Sturdy compact SUV with high ground clearance, electric sunroof, and effortless city manoeuvrability.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 3,000", "automatic": "₹ 3,300"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 4,000", "automatic": "₹ 4,300"}
    ]
  },
  {
    "id": "taisor",
    "name": "Toyota Urban Cruiser Taisor",
    "brand": "Toyota",
    "category": "economic",
    "type": "car",
    "image": "assets/taisor.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2026",
    "rate12h": None,
    "rate24h": 3200,
    "deposit": 5000,
    "kmLimit": "24h: 250 km",
    "badge": "SPORTY CROSSOVER",
    "isFeatured": False,
    "desc": "Coupe-styled urban crossover featuring aerodynamic lines, paddle shifters, and premium audio.",
    "pricing": [
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 3,200", "automatic": "₹ 3,500"}
    ]
  },
  {
    "id": "fronx",
    "name": "Maruti Suzuki Fronx",
    "brand": "Maruti Suzuki",
    "category": "economic",
    "type": "car",
    "image": "assets/fronx.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2024 / 2025",
    "rate12h": 2500,
    "rate24h": 3200,
    "deposit": 5000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "TURBO LOOKS",
    "isFeatured": False,
    "desc": "Bold geometric styling, LED lightbar, heads-up display, and fun turbo performance.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 2,500", "automatic": "₹ 2,800"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 3,200", "automatic": "₹ 3,500"}
    ]
  },
  {
    "id": "rumion-cng",
    "name": "Toyota Rumion (CNG)",
    "brand": "Toyota",
    "category": "economic",
    "type": "car",
    "image": "assets/rumion_cng.png",
    "fuel": "Petrol + CNG",
    "transmission": "Manual",
    "seats": 7,
    "year": "2025",
    "rate12h": None,
    "rate24h": 4000,
    "deposit": 5000,
    "kmLimit": "24h: 250 km",
    "badge": "7 SEATER LUXURY",
    "isFeatured": False,
    "desc": "Toyota's 7-seater MPV with premium dual-tone interior and ultra-efficient CNG range for group getaways.",
    "pricing": [
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 4,000", "automatic": "--"}
    ]
  },
  {
    "id": "swift",
    "name": "Maruti Suzuki Swift",
    "brand": "Maruti Suzuki",
    "category": "economic",
    "type": "car",
    "image": "assets/swift.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2024",
    "rate12h": 2000,
    "rate24h": 2500,
    "deposit": 5000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "CITY AGILE",
    "isFeatured": False,
    "desc": "The quintessential fun city car with nimble steering, punchy Z-series engine, and great fuel mileage.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 2,000", "automatic": "₹ 2,300"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 2,500", "automatic": "₹ 2,700"}
    ]
  },
  {
    "id": "carens-clavis",
    "name": "Kia Carens Clavis",
    "brand": "Kia",
    "category": "economic",
    "type": "car",
    "image": "assets/carens_clavis.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 7,
    "year": "2026",
    "rate12h": None,
    "rate24h": 3200,
    "deposit": 5000,
    "kmLimit": "24h: 250 km",
    "badge": "NEW EDITION",
    "isFeatured": False,
    "desc": "Special Clavis styling edition with black alloys, ambient lighting, and smooth petrol powertrain.",
    "pricing": [
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 3,200", "automatic": "₹ 3,500"}
    ]
  },

  # --- SUVS & 4X4 ---
  {
    "id": "creta",
    "name": "Hyundai Creta",
    "brand": "Hyundai",
    "category": "suv",
    "type": "car",
    "image": "assets/creta.png",
    "fuel": "Petrol",
    "transmission": "Both",
    "seats": 5,
    "year": "2025 / 2026",
    "rate12h": 3800,
    "rate24h": 5000,
    "deposit": 7000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "POPULAR SUV",
    "isFeatured": True,
    "desc": "India's highest selling mid-size SUV. Panoramic sunroof, Bose sound, ventilated seats & ADAS features.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 3,800", "automatic": "₹ 4,000"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 5,000", "automatic": "₹ 5,500"}
    ]
  },
  {
    "id": "thar-black",
    "name": "Mahindra Thar - R.W.D & 4x4",
    "brand": "Mahindra",
    "category": "suv",
    "type": "car",
    "image": "assets/thar_black.png",
    "fuel": "Diesel / Petrol",
    "transmission": "Both",
    "seats": 4,
    "year": "2024 - 2026",
    "rate12h": 3800,
    "rate24h": 5000,
    "deposit": 10000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "ICONIC 4x4",
    "isFeatured": True,
    "desc": "The undisputed king of road presence. Available in 4x2 RWD Diesel and 4x4 Hard Top Petrol for mountain getaways.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 3,800 - ₹ 4,200", "automatic": "₹ 4,000 - ₹ 4,500"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 5,000 - ₹ 5,500", "automatic": "₹ 5,500 - ₹ 6,000"}
    ]
  },
  {
    "id": "thar-white",
    "name": "Mahindra Thar Roxx",
    "brand": "Mahindra",
    "category": "suv",
    "type": "car",
    "image": "assets/thar_white.png",
    "fuel": "Diesel",
    "transmission": "Both",
    "seats": 5,
    "year": "2025",
    "rate12h": 4000,
    "rate24h": 6500,
    "deposit": 10000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "THAR ROXX 5-DOOR",
    "isFeatured": True,
    "desc": "The sensational Mahindra Thar Roxx 5-door. Premium cabin, panoramic sunroof, refined ride quality and authentic Thar swagger.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 4,000", "automatic": "₹ 4,500"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 6,500", "automatic": "₹ 7,000"}
    ]
  },
  {
    "id": "scorpio-n",
    "name": "Mahindra Scorpio N",
    "brand": "Mahindra",
    "category": "suv",
    "type": "car",
    "image": "assets/scorpio_n.png",
    "fuel": "Diesel / Petrol",
    "transmission": "Both",
    "seats": 7,
    "year": "2024 / 2025",
    "rate12h": 4000,
    "rate24h": 6500,
    "deposit": 10000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "BIG DADDY SUV",
    "isFeatured": True,
    "desc": "Massive road presence with 200 PS mStallion / mHawk engine power, Sony 3D surround sound, and tough ladder-frame chassis.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 4,000", "automatic": "₹ 4,500"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 6,500", "automatic": "₹ 7,000"}
    ]
  },
  {
    "id": "venue",
    "name": "Hyundai Venue",
    "brand": "Hyundai",
    "category": "suv",
    "type": "car",
    "image": "assets/venue.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 5,
    "year": "2025",
    "rate12h": 3000,
    "rate24h": 4000,
    "deposit": 5000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "COMPACT SUV",
    "isFeatured": False,
    "desc": "Urban SUV equipped with modern connectivity, dashcam, sunroof, and commanding high seating position.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 3,000", "automatic": "--"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 4,000", "automatic": "--"}
    ]
  },
  {
    "id": "innova-hycross",
    "name": "Toyota Innova Hycross",
    "brand": "Toyota",
    "category": "suv",
    "type": "car",
    "image": "assets/innova_hycross.png",
    "fuel": "Petrol Hybrid",
    "transmission": "Automatic",
    "seats": 7,
    "year": "2025",
    "rate12h": None,
    "rate24h": 7000,
    "deposit": 10000,
    "kmLimit": "24h: 250 km",
    "badge": "HYBRID LUXURY",
    "isFeatured": True,
    "desc": "First-class lounge on wheels. Ottoman reclining captain seats, panoramic roof, whisper-quiet hybrid electric drive.",
    "pricing": [
      {"duration": "24 Hours (250 KMs)", "manual": "--", "automatic": "₹ 7,000"}
    ]
  },
  {
    "id": "fortuner",
    "name": "Toyota Fortuner (4x2 & 4x4)",
    "brand": "Toyota",
    "category": "suv",
    "type": "car",
    "image": "assets/fortuner.png",
    "fuel": "Diesel / Petrol",
    "transmission": "Both",
    "seats": 7,
    "year": "2023 - 2026",
    "rate12h": 9000,
    "rate24h": 12000,
    "deposit": 15000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "VIP STATUS",
    "isFeatured": True,
    "desc": "The ultimate symbol of authority and muscle across Delhi NCR. 204 BHP 500 Nm torque with legendary off-road domination.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "₹ 9,000 - ₹ 11,500", "automatic": "₹ 10,000 - ₹ 12,000"},
      {"duration": "24 Hours (250 KMs)", "manual": "₹ 12,000 - ₹ 13,500", "automatic": "₹ 12,500 - ₹ 15,000"}
    ]
  },
  {
    "id": "xuv700",
    "name": "Mahindra XUV 700 (AX7L)",
    "brand": "Mahindra",
    "category": "suv",
    "type": "car",
    "image": "assets/xuv_700.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 7,
    "year": "2026",
    "rate12h": 5500,
    "rate24h": 7500,
    "deposit": 10000,
    "kmLimit": "12h: 100 km | 24h: 250 km",
    "badge": "FLAGSHIP AX7L",
    "isFeatured": True,
    "desc": "Fully loaded flagship top variant with twin curved digital displays, Sony 12-speaker audio, smart door handles and ADAS level 2.",
    "pricing": [
      {"duration": "12 Hours (100 KMs)", "manual": "--", "automatic": "₹ 5,500"},
      {"duration": "24 Hours (250 KMs)", "manual": "--", "automatic": "₹ 7,500"}
    ]
  },

  # --- LUXURY SEDANS & FLAGSHIP SUVS ---
  {
    "id": "mercedes-e220d",
    "name": "Mercedes-Benz E220d LWB",
    "brand": "Mercedes-Benz",
    "category": "luxury",
    "type": "car",
    "image": "assets/mercedes_e220d.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2022",
    "rate12h": None,
    "rate24h": 25000,
    "deposit": 70000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "EXECUTIVE CLASS",
    "isFeatured": True,
    "desc": "The gold standard of luxury sedans with long wheelbase rear legroom, Burmester surround sound, and ambient lighting in 64 colors.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 25,000"},
      {"duration": "48 Hours (400 KMs)", "manual": "--", "automatic": "₹ 48,000"},
      {"duration": "72 Hours (Unlimited KMs)", "manual": "--", "automatic": "₹ 70,000"}
    ]
  },
  {
    "id": "mercedes-c300-cabrio",
    "name": "Mercedes-Benz C300 Cabriolet",
    "brand": "Mercedes-Benz",
    "category": "luxury",
    "type": "car",
    "image": "assets/mercedes_c300_cabrio.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 4,
    "year": "2021",
    "rate12h": None,
    "rate24h": 55000,
    "deposit": 200000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "OPEN-TOP LUXURY",
    "isFeatured": True,
    "desc": "Electrifying convertible driving sensation. Acoustic fabric soft-top opens in 20 seconds, sports exhaust note, and diamond grille.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 55,000"}
    ]
  },
  {
    "id": "bmw-520d",
    "name": "BMW 520d Luxury Line",
    "brand": "BMW",
    "category": "luxury",
    "type": "car",
    "image": "assets/bmw_520d.png",
    "fuel": "Diesel",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2020",
    "rate12h": None,
    "rate24h": 20000,
    "deposit": 70000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "SHEER DRIVING PLEASURE",
    "isFeatured": True,
    "desc": "The ultimate sports sedan. 50:50 weight balance, dynamic damping, gesture control, and refined Bavarian performance.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 20,000"},
      {"duration": "48 Hours (400 KMs)", "manual": "--", "automatic": "₹ 38,000"}
    ]
  },
  {
    "id": "audi-a6",
    "name": "Audi A6 Technology",
    "brand": "Audi",
    "category": "luxury",
    "type": "car",
    "image": "assets/audi_a6.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2023",
    "rate12h": None,
    "rate24h": 20000,
    "deposit": 70000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "GERMAN LUXURY",
    "isFeatured": True,
    "desc": "Futuristic dual MMI touchscreens, Matrix LED headlights, Bang & Olufsen sound, and whisper-quiet acoustic double glazing.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 20,000"},
      {"duration": "48 Hours (400 KMs)", "manual": "--", "automatic": "₹ 38,000"}
    ]
  },
  {
    "id": "audi-q7",
    "name": "Audi Q7 Quattro",
    "brand": "Audi",
    "category": "luxury",
    "type": "car",
    "image": "assets/audi_q7.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 7,
    "year": "2024",
    "rate12h": None,
    "rate24h": 35000,
    "deposit": 100000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "7-SEATER LUXURY SUV",
    "isFeatured": True,
    "desc": "Full-size 7-seater German luxury SUV with adaptive air suspension, Quattro all-wheel drive, and massive road presence.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 35,000"}
    ]
  },
  {
    "id": "bmw-x1",
    "name": "BMW X1 sDrive",
    "brand": "BMW",
    "category": "luxury",
    "type": "car",
    "image": "assets/bmw_x1.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2021",
    "rate12h": None,
    "rate24h": 15000,
    "deposit": 50000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "LUXURY COMPACT",
    "isFeatured": False,
    "desc": "Dynamic luxury SAV with curved iDrive display, active sport seats, panoramic glass roof, and sporty agility.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 15,000"}
    ]
  },
  {
    "id": "jeep-wrangler",
    "name": "Jeep Wrangler Rubicon (Soft Top)",
    "brand": "Jeep",
    "category": "luxury",
    "type": "car",
    "image": "assets/jeep_wrangler.png",
    "fuel": "Diesel",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2022",
    "rate12h": None,
    "rate24h": 35000,
    "deposit": 150000,
    "kmLimit": "1 Day: 180 km | 2 Days: 400 km | 3 Days: Unlimited",
    "badge": "RUBICON TRAIL RATED",
    "isFeatured": True,
    "desc": "Legendary off-road machine with removable soft-top roof and doors. Rock-Trac 4x4 system with locking differentials.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "--", "automatic": "₹ 35,000"}
    ]
  },
  {
    "id": "defender",
    "name": "Land Rover Defender 110",
    "brand": "Land Rover",
    "category": "luxury",
    "type": "car",
    "image": "assets/defender.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2025",
    "rate12h": None,
    "rate24h": 65000,
    "deposit": 250000,
    "kmLimit": "24h Chauffeur / 3 Days Self-Drive",
    "badge": "BRITISH BEAST",
    "isFeatured": True,
    "desc": "The most unstoppable 4x4 on Earth. Unrivalled luxury, air suspension, Meridian 3D sound, and unstoppable swagger.",
    "pricing": [
      {"duration": "24 Hours (With Chauffeur)", "manual": "--", "automatic": "₹ 65,000"},
      {"duration": "72 Hours (3 Days Self Drive)", "manual": "--", "automatic": "₹ 1,90,000"}
    ]
  },

  # --- EVENTS & EXOTICS ---
  {
    "id": "cle300-amg",
    "name": "Mercedes-CLE 300 Cabriolet AMG",
    "brand": "Mercedes-Benz",
    "category": "events",
    "type": "car",
    "image": "assets/mercedes_cle300_amg.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 4,
    "year": "2026",
    "rate12h": 65000,
    "rate24h": 70000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "badge": "2026 AMG CABRIO",
    "isFeatured": True,
    "desc": "Brand new 2026 edition AMG convertible with red leather upholstery. Chauffeur & fuel included, self-drive also available for min 3 days.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Chauffeur & Fuel Incl.)", "manual": "--", "automatic": "₹ 65,000"},
      {"duration": "12 Hours / 100 KMs (Chauffeur & Fuel Incl.)", "manual": "--", "automatic": "₹ 70,000"},
      {"duration": "Self-Drive (Min 3 Days)", "manual": "--", "automatic": "₹ 65,000 / Day"}
    ]
  },
  {
    "id": "c300-cabrio-events",
    "name": "Mercedes-Benz C300 Cabriolet (Event Edition)",
    "brand": "Mercedes-Benz",
    "category": "events",
    "type": "car",
    "image": "assets/mercedes_c300_cabrio_events.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 4,
    "year": "2022",
    "rate12h": 22000,
    "rate24h": 25000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "extraCharges": "Extra per Hr: ₹ 2,000 | Extra per KM: ₹ 250",
    "badge": "WEDDING ROADSTER",
    "isFeatured": True,
    "desc": "Drop-top elegance with chauffeur & fuel included. Designed for pre-wedding shoots, vidai ceremonies, and baraat entries.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 22,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 25,000"}
    ]
  },
  {
    "id": "audi-a3-cabrio",
    "name": "Audi A3 Cabriolet",
    "brand": "Audi",
    "category": "events",
    "type": "car",
    "image": "assets/audi_a3_cabrio.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 4,
    "year": "2022",
    "rate12h": 18000,
    "rate24h": 22000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "extraCharges": "Extra per Hr: ₹ 1,800 | Extra per KM: ₹ 220",
    "badge": "POPULAR CONVERTIBLE",
    "isFeatured": False,
    "desc": "Agile compact German convertible with acoustic soft-top. Fuel and professional uniformed chauffeur included.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 18,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 22,000"}
    ]
  },
  {
    "id": "gmc-hummer",
    "name": "GMC Hummer",
    "brand": "GMC",
    "category": "events",
    "type": "car",
    "image": "assets/gmc_hummer.png",
    "fuel": "Diesel",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2016",
    "rate12h": 50000,
    "rate24h": 60000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "extraCharges": "Extra per Hr: ₹ 5,000 | Extra per KM: ₹ 500",
    "badge": "GIANT ROAD PRESENCE",
    "isFeatured": True,
    "desc": "Gigantic American muscle that creates an unbelievable spectacle at weddings, music shoots, and high-profile parties.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 50,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 60,000"}
    ]
  },
  {
    "id": "bmw-z4",
    "name": "BMW Z4 Roadster",
    "brand": "BMW",
    "category": "events",
    "type": "car",
    "image": "assets/bmw_z4.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 2,
    "year": "2024",
    "rate12h": 111000,
    "rate24h": 122000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "badge": "2-SEATER EXOTIC",
    "isFeatured": True,
    "desc": "Pure sports car DNA. Aggressive roadster aesthetics, low-slung stance, and unforgettable exhaust acoustics.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 1,11,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 1,22,000"}
    ]
  },
  {
    "id": "porsche-boxster",
    "name": "Porsche 718 Boxster",
    "brand": "Porsche",
    "category": "events",
    "type": "car",
    "image": "assets/porsche_boxster.png",
    "fuel": "Petrol",
    "transmission": "Automatic",
    "seats": 2,
    "year": "2019",
    "rate12h": 100000,
    "rate24h": 115000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "badge": "PORSCHE PRECISION",
    "isFeatured": True,
    "desc": "Mid-engine poise with legendary Porsche crest pedigree. The ultimate head-turner for music albums and elite ceremonies.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 1,00,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 1,15,000"}
    ]
  },
  {
    "id": "lamborghini-huracan",
    "name": "Lamborghini Huracán Spyder",
    "brand": "Lamborghini",
    "category": "events",
    "type": "car",
    "image": "assets/lamborghini_huracan.png",
    "fuel": "Petrol V10",
    "transmission": "Automatic",
    "seats": 2,
    "year": "2023",
    "rate12h": 200000,
    "rate24h": 220000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "badge": "NATURALLY ASPIRATED V10",
    "isFeatured": True,
    "desc": "610 HP screaming naturally aspirated Italian V10 supercar. The apex of style, sound, and open-top drama.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 2,00,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 2,20,000"}
    ]
  },
  {
    "id": "rolls-royce-ghost",
    "name": "Rolls-Royce Ghost",
    "brand": "Rolls-Royce",
    "category": "events",
    "type": "car",
    "image": "assets/rolls_royce_ghost.png",
    "fuel": "Petrol V12",
    "transmission": "Automatic",
    "seats": 5,
    "year": "2016",
    "rate12h": 200000,
    "rate24h": 220000,
    "deposit": 0,
    "kmLimit": "8h: 80 km | 12h: 100 km (G2G)",
    "extraCharges": "Extra per Hr: ₹ 5,000 | Extra per KM: ₹ 500",
    "badge": "ROYAL APEX",
    "isFeatured": True,
    "desc": "The Spirit of Ecstasy. Magic Carpet Ride suspension, starlight headliner, and unmistakable royal authority for Delhi's most opulent weddings.",
    "pricing": [
      {"duration": "8 Hours / 80 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 2,00,000"},
      {"duration": "12 Hours / 100 KMs (Fuel & Driver Incl.)", "manual": "--", "automatic": "₹ 2,20,000"}
    ]
  },

  # --- SUPERBIKES & ADVENTURE ---
  {
    "id": "bmw-g310-rr",
    "name": "BMW G310-RR",
    "brand": "BMW Motorrad",
    "category": "bikes",
    "type": "bike",
    "image": "assets/bmw_g310_rr.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2024",
    "rate12h": None,
    "rate24h": 2100,
    "deposit": 15000,
    "kmLimit": "24h: 180 km",
    "badge": "TRACK AGILITY",
    "isFeatured": False,
    "desc": "M-Sport aerodynamic livery, ride-by-wire throttle, 4 riding modes, and aggressive sportbike clip-ons.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 2,100", "automatic": "--"}
    ]
  },
  {
    "id": "bmw-g310-r",
    "name": "BMW G310-R",
    "brand": "BMW Motorrad",
    "category": "bikes",
    "type": "bike",
    "image": "assets/bmw_g310_r.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2023",
    "rate12h": None,
    "rate24h": 1900,
    "deposit": 10000,
    "kmLimit": "24h: 180 km",
    "badge": "NAKED ROADSTER",
    "isFeatured": False,
    "desc": "Lightweight, agile Bavarian roadster perfect for weekend brunch rides and carving through city traffic.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 1,900", "automatic": "--"}
    ]
  },
  {
    "id": "suzuki-hayabusa",
    "name": "Suzuki Hayabusa 1300",
    "brand": "Suzuki",
    "category": "bikes",
    "type": "bike",
    "image": "assets/suzuki_hayabusa.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2021",
    "rate12h": None,
    "rate24h": 11000,
    "deposit": 50000,
    "kmLimit": "24h: 100 km",
    "badge": "LEGENDARY DHOOM BIKE",
    "isFeatured": True,
    "desc": "The ultimate hypersport icon. 1340cc inline-4 powerhouse producing 190 HP with electronic cruise control and launch control.",
    "pricing": [
      {"duration": "24 Hours (100 KMs)", "manual": "₹ 11,000", "automatic": "--"}
    ]
  },
  {
    "id": "kawasaki-zx10r",
    "name": "Kawasaki Ninja ZX-10R",
    "brand": "Kawasaki",
    "category": "bikes",
    "type": "bike",
    "image": "assets/kawasaki_zx10r.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 1,
    "year": "2024",
    "rate12h": None,
    "rate24h": 20000,
    "deposit": 50000,
    "kmLimit": "24h: 100 km",
    "badge": "WSBK CHAMPION",
    "isFeatured": True,
    "desc": "203 HP World Superbike track weapon. Integrated aerodynamic winglets, quickshifter up/down, Showa Balance Free suspension.",
    "pricing": [
      {"duration": "24 Hours (100 KMs)", "manual": "₹ 20,000", "automatic": "--"}
    ]
  },
  {
    "id": "aprilia-rs457",
    "name": "Aprilia RS 457",
    "brand": "Aprilia",
    "category": "bikes",
    "type": "bike",
    "image": "assets/aprilia_rs457.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2024",
    "rate12h": None,
    "rate24h": 5000,
    "deposit": 20000,
    "kmLimit": "24h: 180 km",
    "badge": "ITALIAN TWIN",
    "isFeatured": True,
    "desc": "Parallel twin Italian superbike chassis with dual-beam aluminum frame, 3-level traction control and racing pedigree.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 5,000", "automatic": "--"}
    ]
  },
  {
    "id": "triumph-daytona660",
    "name": "Triumph Daytona 660",
    "brand": "Triumph",
    "category": "bikes",
    "type": "bike",
    "image": "assets/triumph_daytona660.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2024",
    "rate12h": None,
    "rate24h": 9000,
    "deposit": 30000,
    "kmLimit": "24h: 180 km",
    "badge": "TRIPLE CYLINDER",
    "isFeatured": False,
    "desc": "British triple cylinder thrill with intoxicating intake howl. 95 HP power delivery with Showa SFF-BP forks.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 9,000", "automatic": "--"}
    ]
  },
  {
    "id": "bmw-r1300gs",
    "name": "BMW R 1300GS",
    "brand": "BMW Motorrad",
    "category": "bikes",
    "type": "bike",
    "image": "assets/bmw_r1300gs.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2024",
    "rate12h": None,
    "rate24h": 15000,
    "deposit": 50000,
    "kmLimit": "24h: 180 km",
    "badge": "KING OF ADVENTURE",
    "isFeatured": True,
    "desc": "145 HP Boxer twin adventure flagship. Adaptive vehicle height control, dynamic chassis adaptation, and world-conquering stamina.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 15,000", "automatic": "--"}
    ]
  },
  {
    "id": "ktm-adventure390",
    "name": "KTM Adventure 390",
    "brand": "KTM",
    "category": "bikes",
    "type": "bike",
    "image": "assets/ktm_adventure390.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2025",
    "rate12h": None,
    "rate24h": 3000,
    "deposit": 15000,
    "kmLimit": "24h: 180 km",
    "badge": "EXPEDITION READY",
    "isFeatured": False,
    "desc": "Spoke wheels, adjustable WP Apex suspension, cornering ABS, and off-road traction control for Ladakh & Spiti trials.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 3,000", "automatic": "--"}
    ]
  },
  {
    "id": "himalayan-411",
    "name": "Royal Enfield Himalayan 411",
    "brand": "Royal Enfield",
    "category": "bikes",
    "type": "bike",
    "image": "assets/himalayan411.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2022",
    "rate12h": None,
    "rate24h": 1500,
    "deposit": 7000,
    "kmLimit": "24h: 180 km",
    "badge": "MOUNTAIN EXPLORER",
    "isFeatured": False,
    "desc": "Torquey LS410 engine with upright adventure ergonomics and rugged luggage mounting for highway touring.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 1,500", "automatic": "--"}
    ]
  },
  {
    "id": "triumph-speed400",
    "name": "Triumph Speed 400",
    "brand": "Triumph",
    "category": "bikes",
    "type": "bike",
    "image": "assets/triumph_speed400.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2025",
    "rate12h": None,
    "rate24h": 2000,
    "deposit": 12000,
    "kmLimit": "24h: 180 km",
    "badge": "MODERN CLASSIC",
    "isFeatured": False,
    "desc": "Sophisticated British roadster styling with gold anodised USD forks, 40 PS power, and premium fit and finish.",
    "pricing": [
      {"duration": "24 Hours (180 KMs)", "manual": "₹ 2,000", "automatic": "--"}
    ]
  },
  {
    "id": "kawasaki-z900-new",
    "name": "Kawasaki Z900 (New Edition)",
    "brand": "Kawasaki",
    "category": "bikes",
    "type": "bike",
    "image": "assets/kawasaki_z900_new.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2024",
    "rate12h": None,
    "rate24h": 9500,
    "deposit": 30000,
    "kmLimit": "1 Day: 100 km (Superbike Limit)",
    "badge": "SUGOMI BEAST",
    "isFeatured": True,
    "desc": "125 PS inline-4 naked monster. Sugomi design, full TFT color display with smartphone connectivity, and raw throttle roar.",
    "pricing": [
      {"duration": "24 Hours (100 KMs)", "manual": "₹ 9,500", "automatic": "--"}
    ]
  },
  {
    "id": "kawasaki-z900-old",
    "name": "Kawasaki Z900 (Classic Edition)",
    "brand": "Kawasaki",
    "category": "bikes",
    "type": "bike",
    "image": "assets/kawasaki_z900_old.png",
    "fuel": "Petrol",
    "transmission": "Manual",
    "seats": 2,
    "year": "2021",
    "rate12h": None,
    "rate24h": 8500,
    "deposit": 30000,
    "kmLimit": "1 Day: 100 km (Superbike Limit)",
    "badge": "INLINE-4 ROAR",
    "isFeatured": False,
    "desc": "Crisp inline-4 symphony with trellised lightweight frame and exhilarating mid-range acceleration.",
    "pricing": [
      {"duration": "24 Hours (100 KMs)", "manual": "₹ 8,500", "automatic": "--"}
    ]
  }
]

js_code = f"""/**
 * REVVRIZZ LUXE - Dynamic Web Application Logic
 * Delhi NCR's Premier Automotive Fleet
 */

const FLEET_DATA = {json.dumps(fleet, indent=2)};

// DOM Elements
const fleetGrid = document.getElementById('fleetGrid');
const emptyState = document.getElementById('emptyState');
const searchInput = document.getElementById('searchInput');
const transFilterButtons = document.querySelectorAll('#transFilter .trans-btn');
const sortSelect = document.getElementById('sortSelect');
const catPills = document.querySelectorAll('.cat-pill-card');
const resetFiltersBtn = document.getElementById('resetFiltersBtn');

// Calculator Elements
const calcVehicleSelect = document.getElementById('calcVehicleSelect');
const calcDurationSelect = document.getElementById('calcDurationSelect');
const calcTransmissionSelect = document.getElementById('calcTransmissionSelect');
const calcDoorstep = document.getElementById('calcDoorstep');
const calcBaseRent = document.getElementById('calcBaseRent');
const calcKmLimit = document.getElementById('calcKmLimit');
const calcAddons = document.getElementById('calcAddons');
const calcTotalRent = document.getElementById('calcTotalRent');
const calcDeposit = document.getElementById('calcDeposit');
const calcBookBtn = document.getElementById('calcBookBtn');

// Modal Elements
const vehicleModal = document.getElementById('vehicleModal');
const modalBody = document.getElementById('modalBody');
const modalCloseBtn = document.getElementById('modalCloseBtn');

// Mobile Nav Toggle
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

// Active filter state
let currentCategory = 'all';
let currentTransmission = 'all';
let currentSearch = '';
let currentSort = 'featured';

/**
 * INITIALIZATION
 */
document.addEventListener('DOMContentLoaded', () => {{
  populateCalculatorOptions();
  renderFleet();
  setupEventListeners();
  updateCalculator();
}});

/**
 * FORMAT CURRENCY
 */
function formatCurrency(val) {{
  if (val === null || val === undefined) return '--';
  return '₹ ' + val.toLocaleString('en-IN');
}}

/**
 * POPULATE CALCULATOR VEHICLES
 */
function populateCalculatorOptions() {{
  if (!calcVehicleSelect) return;
  calcVehicleSelect.innerHTML = '';
  
  const categories = [
    {{ key: 'suv', label: 'SUVs & 4x4' }},
    {{ key: 'luxury', label: 'Luxury Sedans' }},
    {{ key: 'events', label: 'Events & Exotics' }},
    {{ key: 'economic', label: 'Economic & Hatch' }},
    {{ key: 'bikes', label: 'Superbikes & Adventure' }}
  ];

  categories.forEach(cat => {{
    const group = document.createElement('optgroup');
    group.label = cat.label;
    const catVehicles = FLEET_DATA.filter(v => v.category === cat.key);
    
    catVehicles.forEach(v => {{
      const opt = document.createElement('option');
      opt.value = v.id;
      opt.textContent = `${{v.name}} (${{formatCurrency(v.rate24h)}}/day)`;
      group.appendChild(opt);
    }});
    
    if (catVehicles.length > 0) {{
      calcVehicleSelect.appendChild(group);
    }}
  }});

  // Default to Thar or Baleno
  calcVehicleSelect.value = 'thar-black';
}}

/**
 * RENDER FLEET CARDS
 */
function renderFleet() {{
  if (!fleetGrid) return;

  // Filter
  let filtered = FLEET_DATA.filter(v => {{
    // Category filter
    if (currentCategory !== 'all' && v.category !== currentCategory) {{
      return false;
    }}
    // Transmission filter
    if (currentTransmission !== 'all') {{
      if (v.type === 'bike') {{
        if (currentTransmission === 'Automatic') return false;
      }} else {{
        if (v.transmission !== 'Both' && v.transmission !== currentTransmission) {{
          return false;
        }}
      }}
    }}
    // Search filter
    if (currentSearch.trim() !== '') {{
      const q = currentSearch.toLowerCase();
      const matchName = v.name.toLowerCase().includes(q);
      const matchBrand = v.brand.toLowerCase().includes(q);
      const matchFuel = v.fuel.toLowerCase().includes(q);
      if (!matchName && !matchBrand && !matchFuel) return false;
    }}
    return true;
  }});

  // Sort
  if (currentSort === 'price-asc') {{
    filtered.sort((a, b) => a.rate24h - b.rate24h);
  }} else if (currentSort === 'price-desc') {{
    filtered.sort((a, b) => b.rate24h - a.rate24h);
  }} else if (currentSort === 'name') {{
    filtered.sort((a, b) => a.name.localeCompare(b.name));
  }} else {{
    // featured: featured first, then original order
    filtered.sort((a, b) => (b.isFeatured ? 1 : 0) - (a.isFeatured ? 1 : 0));
  }}

  // Check empty state
  if (filtered.length === 0) {{
    fleetGrid.innerHTML = '';
    if (emptyState) emptyState.style.display = 'block';
    return;
  }}

  if (emptyState) emptyState.style.display = 'none';

  // Build card markup
  const cardsHtml = filtered.map(v => {{
    const waText = encodeURIComponent(`Hi RevvRizz Luxe, I am interested in booking the *${{v.name}}*. Please share availability and booking details.`);
    const waUrl = `https://wa.me/919289678449?text=${{waText}}`;
    
    // Background style for stage: bikes and outdoor event cars are full-bleed photo, studio cars are clean white stage
    const isPhoto = v.type === 'bike' || ['cle300-amg', 'bmw-z4', 'porsche-boxster', 'lamborghini-huracan', 'rolls-royce-ghost', 'gmc-hummer', 'audi-a3-cabrio'].includes(v.id);
    const cardClass = isPhoto ? 'v-card photo-type' : 'v-card';
    
    // Transmission display
    const transText = v.transmission === 'Both' ? 'Manual / Auto' : v.transmission;

    return `
      <div class="${{cardClass}}" data-id="${{v.id}}">
        <div class="v-card-img-stage">
          <span class="v-badge-cat">${{v.badge || v.brand}}</span>
          <img src="${{v.image}}" alt="${{v.name}}" class="v-card-img">
        </div>

        <div class="v-card-body">
          <div>
            <div class="v-card-header">
              <h3 class="v-card-title">${{v.name}}</h3>
              <span class="v-year-pill">${{v.year}}</span>
            </div>

            <div class="v-specs-strip">
              <span class="v-spec-item"><i class="fa-solid fa-gas-pump"></i> ${{v.fuel}}</span>
              <span class="v-spec-item"><i class="fa-solid fa-gear"></i> ${{transText}}</span>
              <span class="v-spec-item"><i class="fa-solid fa-users"></i> ${{v.seats}} Seats</span>
              <span class="v-spec-item"><i class="fa-solid fa-gauge-high"></i> ${{v.kmLimit}}</span>
            </div>

            <div class="v-pricing-box">
              ${{v.rate12h ? `
                <div class="v-rate-unit">
                  <span class="v-rate-label">12 Hours Rent</span>
                  <span class="v-rate-val">${{formatCurrency(v.rate12h)}}</span>
                </div>
                <div class="v-rate-unit">
                  <span class="v-rate-label">24 Hours (1 Day)</span>
                  <span class="v-rate-val highlight gold-gradient-text">${{formatCurrency(v.rate24h)}}</span>
                </div>
              ` : `
                <div class="v-pricing-single">
                  <div class="v-rate-unit">
                    <span class="v-rate-label">24 Hours (1 Day Rent)</span>
                    <span class="v-rate-val highlight gold-gradient-text">${{formatCurrency(v.rate24h)}}</span>
                  </div>
                  <div class="v-rate-unit" style="text-align: right;">
                    <span class="v-rate-label">Security Deposit</span>
                    <span class="v-rate-val" style="font-size: 0.95rem; color: #ECC880;">${{formatCurrency(v.deposit)}}</span>
                  </div>
                </div>
              `}}
            </div>

            <div class="v-deposit-text">
              <i class="fa-solid fa-shield-halved gold-icon"></i>
              Refundable Deposit: <strong>${{formatCurrency(v.deposit)}}</strong>
            </div>
          </div>

          <div class="v-card-actions">
            <a href="${{waUrl}}" target="_blank" class="btn btn-book-card">
              <i class="fa-brands fa-whatsapp"></i> Reserve Now
            </a>
            <button class="btn btn-details-card" onclick="openVehicleModal('${{v.id}}')">
              <i class="fa-solid fa-eye"></i> Details
            </button>
          </div>
        </div>
      </div>
    `;
  }}).join('');

  fleetGrid.innerHTML = cardsHtml;
}}

/**
 * CALCULATOR UPDATE LOGIC
 */
function updateCalculator() {{
  if (!calcVehicleSelect) return;

  const vehicleId = calcVehicleSelect.value;
  const vehicle = FLEET_DATA.find(v => v.id === vehicleId);
  if (!vehicle) return;

  const durationHours = parseInt(calcDurationSelect.value, 10);
  const isDoorstep = calcDoorstep ? calcDoorstep.checked : false;

  let base = 0;
  let kmText = '250 KMs';

  if (durationHours === 12) {{
    base = vehicle.rate12h ? vehicle.rate12h : Math.round(vehicle.rate24h * 0.75);
    kmText = '100 KMs';
  }} else if (durationHours === 24) {{
    base = vehicle.rate24h;
    kmText = vehicle.type === 'bike' ? '180 KMs' : '250 KMs';
  }} else if (durationHours === 48) {{
    base = vehicle.rate24h * 2;
    kmText = vehicle.type === 'bike' ? '360 KMs' : '500 KMs';
  }} else if (durationHours === 72) {{
    if (vehicle.id === 'defender') {{
      base = 190000;
    }} else {{
      base = vehicle.rate24h * 3;
    }}
    kmText = 'Unlimited KMs';
  }}

  const addonTotal = isDoorstep ? 1000 : 0;
  const total = base + addonTotal;

  calcBaseRent.textContent = formatCurrency(base);
  calcKmLimit.textContent = kmText;
  calcAddons.textContent = formatCurrency(addonTotal);
  calcTotalRent.textContent = formatCurrency(total);
  calcDeposit.textContent = formatCurrency(vehicle.deposit);

  // Update book button link
  calcBookBtn.onclick = () => {{
    const durationLabel = calcDurationSelect.options[calcDurationSelect.selectedIndex].text;
    const transChoice = calcTransmissionSelect.value;
    const doorstepText = isDoorstep ? 'Yes (Doorstep Delivery)' : 'No (Hub Pickup)';
    
    const msg = `Hi RevvRizz Luxe, I would like to reserve the *${{vehicle.name}}*:\\n` +
      `• Duration: ${{durationLabel}}\\n` +
      `• Transmission: ${{transChoice}}\\n` +
      `• Estimated Rent: ${{formatCurrency(total)}}\\n` +
      `• Security Deposit: ${{formatCurrency(vehicle.deposit)}} (Refundable)\\n` +
      `• Delivery Option: ${{doorstepText}}\\n\\n` +
      `Please confirm availability for immediate booking.`;
      
    const waUrl = `https://wa.me/919289678449?text=${{encodeURIComponent(msg)}}`;
    window.open(waUrl, '_blank');
  }};
}}

/**
 * OPEN VEHICLE DETAILS MODAL
 */
window.openVehicleModal = function(id) {{
  const v = FLEET_DATA.find(item => item.id === id);
  if (!v || !vehicleModal || !modalBody) return;

  const isPhoto = v.type === 'bike' || ['cle300-amg', 'bmw-z4', 'porsche-boxster', 'lamborghini-huracan', 'rolls-royce-ghost', 'gmc-hummer', 'audi-a3-cabrio'].includes(v.id);
  const stageBg = isPhoto ? '#07080B' : '#FFFFFF';
  const imgFit = isPhoto ? 'cover' : 'contain';
  const waText = encodeURIComponent(`Hi RevvRizz Luxe, I want to book the *${{v.name}}*. Please confirm current availability and process.`);
  const waUrl = `https://wa.me/919289678449?text=${{waText}}`;

  let pricingTableRows = '';
  if (v.pricing && v.pricing.length > 0) {{
    pricingTableRows = v.pricing.map(row => `
      <tr>
        <td><strong>${{row.duration}}</strong></td>
        <td class="rate">${{row.manual || '--'}}</td>
        <td class="rate">${{row.automatic || '--'}}</td>
      </tr>
    `).join('');
  }}

  modalBody.innerHTML = `
    <div class="modal-hero-img-box" style="background: ${{stageBg}};">
      <img src="${{v.image}}" alt="${{v.name}}" style="width: 100%; height: 100%; max-height: 280px; object-fit: ${{imgFit}};">
    </div>

    <div class="modal-inner-content">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; margin-bottom: 0.8rem;">
        <div>
          <span class="v-badge-cat" style="position: static; margin-bottom: 0.5rem; display: inline-block;">${{v.badge || v.brand}}</span>
          <h2 class="modal-v-title gold-gradient-text">${{v.name}}</h2>
        </div>
        <div style="text-align: right;">
          <span style="font-size: 0.75rem; color: #94A3B8; display: block;">Daily Rent</span>
          <span class="gold-gradient-text" style="font-size: 1.5rem; font-weight: 800;">${{formatCurrency(v.rate24h)}}</span>
        </div>
      </div>

      <p style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.6; margin-bottom: 1.2rem;">${{v.desc}}</p>

      <div class="modal-specs-grid">
        <div class="modal-spec-block">
          <span>Fuel / Powertrain</span>
          <strong>${{v.fuel}}</strong>
        </div>
        <div class="modal-spec-block">
          <span>Transmission</span>
          <strong>${{v.transmission === 'Both' ? 'Manual & Automatic' : v.transmission}}</strong>
        </div>
        <div class="modal-spec-block">
          <span>Capacity</span>
          <strong>${{v.seats}} Persons</strong>
        </div>
        <div class="modal-spec-block">
          <span>Model Year</span>
          <strong>${{v.year}}</strong>
        </div>
        <div class="modal-spec-block">
          <span>Mileage Limit</span>
          <strong>${{v.kmLimit}}</strong>
        </div>
        <div class="modal-spec-block">
          <span>Refundable Deposit</span>
          <strong style="color: #ECC880;">${{formatCurrency(v.deposit)}}</strong>
        </div>
      </div>

      <h4 style="font-family: var(--font-royal); font-size: 1.1rem; color: #FFF; margin-top: 1.5rem; margin-bottom: 0.8rem;">
        <i class="fa-solid fa-table-list gold-icon"></i> Rental Rates & Durations
      </h4>

      <table class="modal-pricing-table">
        <thead>
          <tr>
            <th>Rental Duration</th>
            <th>Manual Transmission</th>
            <th>Automatic Transmission</th>
          </tr>
        </thead>
        <tbody>
          ${{pricingTableRows}}
        </tbody>
      </table>

      ${{v.extraCharges ? `
      <div style="background: rgba(212, 175, 55, 0.08); border: 1px dashed rgba(212, 175, 55, 0.4); border-radius: var(--radius-sm); padding: 0.75rem 1rem; margin-top: 0.8rem; font-size: 0.88rem; color: #FFF;">
        <i class="fa-solid fa-clock gold-icon"></i> <strong>Extra Usage Charges:</strong> ${{v.extraCharges}}
      </div>
      ` : ''}}

      ${{v.category === 'events' ? `
      <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: var(--radius-sm); padding: 0.65rem 0.95rem; margin-top: 0.6rem; font-size: 0.8rem; color: #94A3B8;">
        <i class="fa-solid fa-route gold-icon"></i> <strong>Important Terms:</strong> KMs are counted Garage to Garage (G2G) from office location. Tolls, state tax & parking charges are excluded. Fuel & chauffeur fees included in package.
      </div>
      ` : ''}}

      <div style="background: rgba(212, 175, 55, 0.08); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: var(--radius-md); padding: 1rem 1.2rem; margin: 1.5rem 0; display: flex; align-items: center; gap: 1rem;">
        <i class="fa-solid fa-shield-halved gold-icon" style="font-size: 1.8rem;"></i>
        <div>
          <strong style="color: #FFF; font-size: 0.95rem;">100% Refundable Security Deposit: ${{formatCurrency(v.deposit)}}</strong>
          <p style="font-size: 0.8rem; color: #94A3B8; margin-top: 0.2rem;">Processed via instant UPI or IMPS bank transfer within 15 minutes of safe vehicle return inspection.</p>
        </div>
      </div>

      <div class="modal-actions-bar">
        <a href="${{waUrl}}" target="_blank" class="btn btn-gold btn-glow" style="flex: 1; min-width: 200px;">
          <i class="fa-brands fa-whatsapp"></i> Reserve This Vehicle on WhatsApp
        </a>
        <a href="tel:+919289678449" class="btn btn-outline-gold" style="flex: 1; min-width: 180px;">
          <i class="fa-solid fa-phone"></i> Call Hotline (+91 9289678449)
        </a>
      </div>
    </div>
  `;

  vehicleModal.classList.add('open');
  vehicleModal.classList.add('active');
  document.body.style.overflow = 'hidden';
}};

function closeVehicleModal() {{
  if (!vehicleModal) return;
  vehicleModal.classList.remove('open');
  vehicleModal.classList.remove('active');
  document.body.style.overflow = '';
}}


/**
 * SETUP ALL EVENT LISTENERS
 */
function setupEventListeners() {{
  // Search input
  if (searchInput) {{
    searchInput.addEventListener('input', (e) => {{
      currentSearch = e.target.value;
      renderFleet();
    }});
  }}

  // Transmission buttons
  transFilterButtons.forEach(btn => {{
    btn.addEventListener('click', () => {{
      transFilterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentTransmission = btn.getAttribute('data-trans');
      renderFleet();
    }});
  }});

  // Sort dropdown
  if (sortSelect) {{
    sortSelect.addEventListener('change', (e) => {{
      currentSort = e.target.value;
      renderFleet();
    }});
  }}

  // Category pills (Quick Category Pills + Footer Links)
  catPills.forEach(pill => {{
    pill.addEventListener('click', () => {{
      const cat = pill.getAttribute('data-cat');
      catPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      currentCategory = cat;
      renderFleet();
      
      // Smooth scroll to fleet
      const fleetEl = document.getElementById('fleet');
      if (fleetEl) {{
        fleetEl.scrollIntoView({{ behavior: 'smooth' }});
      }}
    }});
  }});

  // Footer category links
  document.querySelectorAll('.footer-links-col a[data-cat]').forEach(link => {{
    link.addEventListener('click', (e) => {{
      e.preventDefault();
      const cat = link.getAttribute('data-cat');
      catPills.forEach(p => {{
        if (p.getAttribute('data-cat') === cat) {{
          p.classList.add('active');
        }} else {{
          p.classList.remove('active');
        }}
      }});
      currentCategory = cat;
      renderFleet();
      document.getElementById('fleet').scrollIntoView({{ behavior: 'smooth' }});
    }});
  }});

  // Reset filters
  if (resetFiltersBtn) {{
    resetFiltersBtn.addEventListener('click', () => {{
      currentCategory = 'all';
      currentTransmission = 'all';
      currentSearch = '';
      currentSort = 'featured';
      
      if (searchInput) searchInput.value = '';
      if (sortSelect) sortSelect.value = 'featured';
      
      transFilterButtons.forEach(b => {{
        b.classList.toggle('active', b.getAttribute('data-trans') === 'all');
      }});
      
      catPills.forEach(p => {{
        p.classList.toggle('active', p.getAttribute('data-cat') === 'all');
      }});
      
      renderFleet();
    }});
  }}

  // Calculator change events
  if (calcVehicleSelect) calcVehicleSelect.addEventListener('change', updateCalculator);
  if (calcDurationSelect) calcDurationSelect.addEventListener('change', updateCalculator);
  if (calcTransmissionSelect) calcTransmissionSelect.addEventListener('change', updateCalculator);
  if (calcDoorstep) calcDoorstep.addEventListener('change', updateCalculator);

  // Modal close handlers
  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeVehicleModal);
  if (vehicleModal) {{
    vehicleModal.addEventListener('click', (e) => {{
      if (e.target === vehicleModal) closeVehicleModal();
    }});
  }}
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') closeVehicleModal();
  }});

  // Mobile nav toggle
  if (navToggle && navLinks) {{
    navToggle.addEventListener('click', () => {{
      navLinks.classList.toggle('open');
    }});
    navLinks.querySelectorAll('a').forEach(a => {{
      a.addEventListener('click', () => {{
        navLinks.classList.remove('open');
      }});
    }});
  }}

  // FAQ Accordion
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {{
    const btn = item.querySelector('.faq-question');
    if (btn) {{
      btn.addEventListener('click', () => {{
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
      }});
    }}
  }});

  // Quick Inquiry Form submission -> WhatsApp
  const quickForm = document.getElementById('quickInquiryForm');
  if (quickForm) {{
    quickForm.addEventListener('submit', (e) => {{
      e.preventDefault();
      const name = document.getElementById('formName').value;
      const phone = document.getElementById('formPhone').value;
      const vehicle = document.getElementById('formVehicle').value;
      const date = document.getElementById('formDate').value || 'Immediate / Flexible';
      const msg = document.getElementById('formMessage').value || 'Standard rental inquiry';

      const text = `Hi RevvRizz Luxe, new booking inquiry from website:\\n` +
        `• Name: ${{name}}\\n` +
        `• Phone: ${{phone}}\\n` +
        `• Vehicle: ${{vehicle}}\\n` +
        `• Date: ${{date}}\\n` +
        `• Requirements: ${{msg}}`;

      const waUrl = `https://wa.me/919289678449?text=${{encodeURIComponent(text)}}`;
      window.open(waUrl, '_blank');
    }});
  }}
}}
"""

with open("app.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print(f"app.js written successfully with {len(fleet)} vehicles!")
