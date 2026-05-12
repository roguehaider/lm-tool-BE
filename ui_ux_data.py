"""
LVRG Engine — UI/UX Data Layer.

Lazy-loaded, LRU-cached CSV loaders for all design data sets.
Provides lookup functions consumed by design_system.py.
"""

import csv
import os
from functools import lru_cache
from typing import Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "design_data")


# ───────────────────────────────────────────────────────────────────────────
# CSV LOADERS — each loaded once per process lifetime via lru_cache
# ───────────────────────────────────────────────────────────────────────────

def _load_csv(filename: str) -> list[dict]:
    path = os.path.join(DATA_DIR, filename)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@lru_cache(maxsize=1)
def styles() -> list[dict]:
    """67 design style rows from styles.csv."""
    return _load_csv("styles.csv")


@lru_cache(maxsize=1)
def colors() -> list[dict]:
    """96 industry palette rows from colors.csv."""
    return _load_csv("colors.csv")


@lru_cache(maxsize=1)
def typography() -> list[dict]:
    """56 font pairing rows from typography.csv."""
    return _load_csv("typography.csv")


@lru_cache(maxsize=1)
def ui_reasoning() -> list[dict]:
    """100 UI reasoning rows from ui-reasoning.csv."""
    return _load_csv("ui-reasoning.csv")


@lru_cache(maxsize=1)
def ux_guidelines() -> list[dict]:
    """98 UX guideline rows from ux-guidelines.csv."""
    return _load_csv("ux-guidelines.csv")


# ───────────────────────────────────────────────────────────────────────────
# INDUSTRY MAP — maps intel business_type → list of UI_Category strings
# matching rows in ui-reasoning.csv (uses exact category strings from CSV)
# ───────────────────────────────────────────────────────────────────────────

INDUSTRY_MAP: dict[str, list[str]] = {
    "restaurant":       ["Restaurant/Food"],
    "catering":         ["Restaurant/Food", "Event Management"],
    "coffee_shop":      ["Coffee Shop", "Bakery/Cafe"],
    "bar":              ["Music/Entertainment", "Restaurant/Food"],
    "craft_beverage":   ["Brewery/Winery"],
    "brewery":          ["Brewery/Winery"],
    "bakery":           ["Bakery/Cafe"],
    "fitness":          ["Fitness/Gym App"],
    "gym":              ["Fitness/Gym App"],
    "wellness":         ["Wellness/Mental Health", "Beauty/Spa/Wellness Service"],
    "spa":              ["Beauty/Spa/Wellness Service", "Wellness/Mental Health"],
    "salon":            ["Beauty/Spa/Wellness Service"],
    "beauty":           ["Beauty/Spa/Wellness Service"],
    "healthcare":       ["Healthcare App", "Medical Clinic"],
    "medical":          ["Medical Clinic", "Healthcare App"],
    "dental":           ["Dental Practice"],
    "vet":              ["Veterinary Clinic"],
    "veterinary":       ["Veterinary Clinic"],
    "pharmacy":         ["Pharmacy/Drug Store"],
    "law":              ["Legal Services"],
    "legal":            ["Legal Services"],
    "finance":          ["Fintech (Banking)", "Banking/Traditional Finance"],
    "fintech":          ["Fintech/Crypto", "Fintech (Banking)"],
    "insurance":        ["Insurance Platform"],
    "tech":             ["SaaS (General)", "AI/Chatbot Platform"],
    "saas":             ["SaaS (General)", "Micro SaaS", "B2B SaaS Enterprise"],
    "startup":          ["Startup Landing", "Micro SaaS"],
    "retail":           ["E-commerce", "Marketplace (P2P)"],
    "ecommerce":        ["E-commerce", "E-commerce Luxury"],
    "luxury":           ["Luxury/Premium Brand", "E-commerce Luxury"],
    "creative":         ["Creative Agency", "Portfolio/Personal"],
    "agency":           ["Marketing Agency", "Creative Agency"],
    "photography":      ["Photography Studio", "Portfolio/Personal"],
    "real_estate":      ["Real Estate"],
    "hotel":            ["Hotel/Hospitality"],
    "hospitality":      ["Hotel/Hospitality", "Restaurant/Food"],
    "travel":           ["Travel/Tourism"],
    "automotive":       ["Automotive/Car Dealership"],
    "construction":     ["Construction/Architecture"],
    "architecture":     ["Architecture/Interior"],
    "interior":         ["Architecture/Interior"],
    "event":            ["Event Management", "Conference/Webinar Platform"],
    "wedding":          ["Wedding/Event Planning"],
    "childcare":        ["Childcare/Daycare"],
    "education":        ["Education", "Online Course/E-learning"],
    "florist":          ["Florist/Plant Shop"],
    "cleaning":         ["Cleaning Service"],
    "home_service":     ["Home Services"],
    "consulting":       ["Consulting Firm", "B2B Service"],
    "non_profit":       ["Non-profit/Charity"],
    "church":           ["Church/Religious Organization"],
    "sports":           ["Sports Team/Club"],
    "entertainment":    ["Music/Entertainment", "Event Management"],
    "fun center":       ["Music/Entertainment", "Event Management"],
    "amusement":        ["Music/Entertainment", "Event Management"],
    "museum":           ["Museum/Gallery"],
    "plumbing":         ["Home Services"],
    "plumber":          ["Home Services"],
    "electrician":      ["Home Services"],
    "hvac":             ["Home Services"],
    "roofing":          ["Construction/Architecture"],
    "contractor":       ["Construction/Architecture"],
    "mechanic":         ["Automotive/Car Dealership"],
    "auto repair":      ["Automotive/Car Dealership"],
    "ecommerce":        ["E-commerce", "Marketplace (P2P)"],
    "e commerce":       ["E-commerce", "Marketplace (P2P)"],
    "online store":     ["E-commerce"],
    "childcare":        ["Childcare/Daycare"],
    "daycare":          ["Childcare/Daycare"],
    "preschool":        ["Childcare/Daycare"],
    "nonprofit":        ["Non-profit/Charity"],
    "charity":          ["Non-profit/Charity"],
    "other":            ["Service Landing Page"],
    "professional":     ["B2B Service", "Consulting Firm"],
}


# ───────────────────────────────────────────────────────────────────────────
# PERSONALITY TYPOGRAPHY MAP — maps personality name → list of font pairing
# names from typography.csv "Font Pairing Name" column.
# ───────────────────────────────────────────────────────────────────────────

PERSONALITY_TYPOGRAPHY_MAP: dict[str, list[str]] = {
    "minimal": [
        "Minimal Swiss",
        "Minimalist Portfolio",
        "Luxury Minimalist",
        "Accessibility First",
    ],
    "modern_saas": [
        "Tech Startup",
        "Friendly SaaS",
        "Modern Professional",
        "Geometric Modern",
    ],
    "corporate": [
        "Corporate Trust",
        "Financial Trust",
        "Legal Professional",
        "Modern Professional",
    ],
    "dark_premium": [
        "Fashion Forward",
        "Luxury Serif",
        "Classic Elegant",
        "Kinetic Motion",
    ],
    "editorial": [
        "Classic Elegant",
        "Editorial Classic",
        "Magazine Style",
        "News Editorial",
    ],
    "bento": [
        "Tech Startup",
        "Fashion Forward",
        "Geometric Modern",
        "Minimalist Portfolio",
    ],
    "gradient_modern": [
        "Tech Startup",
        "Bold Statement",
        "Startup Bold",
        "Geometric Modern",
    ],
    "warm_artisan": [
        "Wellness Calm",
        "Indie/Craft",
        "Restaurant Menu",
        "Retro Vintage",
    ],
    # New personalities
    "glassmorphism": [
        "Tech Startup",
        "Friendly SaaS",
        "Spatial Clear",
        "Luxury Serif",
    ],
    "neo_brutalism": [
        "Brutalist Raw",
        "Neubrutalist Bold",
        "Gen Z Brutal",
        "Bold Statement",
    ],
    "aurora": [
        "Fashion Forward",
        "Luxury Minimalist",
        "Kinetic Motion",
        "Geometric Modern",
    ],
    "claymorphism": [
        "Playful Creative",
        "Soft Rounded",
        "Kids/Education",
        "E-commerce Clean",
    ],
    "flat_minimal": [
        "Minimal Swiss",
        "Corporate Trust",
        "Financial Trust",
        "Accessibility First",
    ],
    "vibrant_block": [
        "Bold Statement",
        "Sports/Fitness",
        "Music/Entertainment",
        "E-commerce Clean",
    ],
    "luxury_glass": [
        "Classic Elegant",
        "Real Estate Luxury",
        "Luxury Serif",
        "Luxury Minimalist",
    ],
    "organic_nature": [
        "Wellness Calm",
        "Indie/Craft",
        "Soft Rounded",
        "Restaurant Menu",
    ],
    "soft_ui": [
        "Medical Clean",
        "Wellness Calm",
        "Soft Rounded",
        "Friendly SaaS",
    ],
    "dark_oled": [
        "Crypto/Web3",
        "Gaming Bold",
        "Tech/HUD Mono",
        "Fashion Forward",
    ],
}


# ───────────────────────────────────────────────────────────────────────────
# NON-GOOGLE FONTS — fonts NOT available on Google Fonts; exclude from
# font selection to avoid broken @import URLs.
# ───────────────────────────────────────────────────────────────────────────

NON_GOOGLE_FONTS: set[str] = {
    "Satoshi",
    "General Sans",
    "Clash Display",
    "Recoleta",
}


# ───────────────────────────────────────────────────────────────────────────
# LOOKUP FUNCTIONS
# ───────────────────────────────────────────────────────────────────────────

def _resolve_categories(business_type: str) -> list[str]:
    """Resolve INDUSTRY_MAP categories for a business_type string.

    Tries exact match first, then substring matching (normalising underscores
    to spaces so "home_service" matches "home services").  Returns
    ["Service Landing Page"] when nothing matches.
    """
    bt = business_type.lower().strip().replace("_", " ").replace("-", " ")
    # 1. Exact match (both normalised)
    norm_map = {k.replace("_", " ").replace("-", " "): v for k, v in INDUSTRY_MAP.items()}
    if bt in norm_map:
        return norm_map[bt]
    # 2. Longest-key-first substring: "real estate" beats "agency" for "real estate agency"
    for key in sorted(norm_map, key=len, reverse=True):
        if key in bt:
            return norm_map[key]
    # 3. Any word of business_type contained in a map key (single-word fallback)
    for word in bt.split():
        if len(word) >= 5:  # skip short words
            for key in sorted(norm_map, key=len, reverse=True):
                if word in key:
                    return norm_map[key]
    return ["Service Landing Page"]


def get_ui_reasoning_for_industry(business_type: str) -> list[dict]:
    """Return ui_reasoning rows matching business_type via INDUSTRY_MAP.

    Returns the first matched category's rows. Falls back to Service Landing Page
    if no mapping found.
    """
    categories = _resolve_categories(business_type)
    rows = ui_reasoning()
    results = []
    for cat in categories:
        for row in rows:
            if row.get("UI_Category", "").strip() == cat:
                results.append(row)
                break  # one row per category
    return results


def get_palette_for_industry(business_type: str) -> Optional[dict]:
    """Return best matching colors row for the given business_type, or None.

    Matches by Product Type against the categories listed in INDUSTRY_MAP.
    Returns the first match found.
    """
    categories = _resolve_categories(business_type)
    if categories == ["Service Landing Page"]:
        return None

    # Build a normalised lookup of color rows by their product type
    palette_rows = colors()
    # Map normalised lower-case product type -> row for quick access
    palette_map: dict[str, dict] = {}
    for row in palette_rows:
        key = row.get("Product Type", "").strip().lower()
        if key:
            palette_map[key] = row

    # Try each mapped category in priority order
    for cat in categories:
        row = palette_map.get(cat.lower())
        if row:
            return row

    # Fuzzy fallback: partial substring match
    for cat in categories:
        cat_lower = cat.lower()
        for key, row in palette_map.items():
            if cat_lower in key or key in cat_lower:
                return row

    return None


def get_typography_for_personality(personality_name: str) -> list[dict]:
    """Return typography rows matching the personality via PERSONALITY_TYPOGRAPHY_MAP.

    Excludes any pairings that use NON_GOOGLE_FONTS. Returns all matched rows,
    falling back to a generic set if none found.
    """
    pairing_names = PERSONALITY_TYPOGRAPHY_MAP.get(personality_name.lower(), [])
    typo_rows = typography()

    # Build lookup of pairing name -> row
    pairing_map: dict[str, dict] = {}
    for row in typo_rows:
        name = row.get("Font Pairing Name", "").strip()
        if name:
            pairing_map[name] = row

    results = []
    for name in pairing_names:
        row = pairing_map.get(name)
        if not row:
            continue
        # Exclude non-Google-Fonts pairings
        heading = row.get("Heading Font", "").strip()
        body = row.get("Body Font", "").strip()
        if heading in NON_GOOGLE_FONTS or body in NON_GOOGLE_FONTS:
            continue
        results.append(row)

    if not results:
        # Generic fallback: return first 3 pairings that are Google-Fonts safe
        for row in typo_rows:
            heading = row.get("Heading Font", "").strip()
            body = row.get("Body Font", "").strip()
            if heading not in NON_GOOGLE_FONTS and body not in NON_GOOGLE_FONTS:
                results.append(row)
            if len(results) >= 3:
                break

    return results


def get_ux_rules(categories: Optional[list[str]] = None) -> list[dict]:
    """Return up to 8 high-severity rules from ux_guidelines().

    Filtered by Category list if provided. Always prioritises High severity rows,
    then Medium, to return the most impactful constraints first.
    """
    rows = ux_guidelines()

    if categories:
        cats_lower = {c.lower() for c in categories}
        filtered = [
            r for r in rows
            if r.get("Category", "").strip().lower() in cats_lower
        ]
    else:
        filtered = rows

    # Sort: High first, then Medium, then Low
    severity_order = {"high": 0, "medium": 1, "low": 2}
    filtered.sort(
        key=lambda r: severity_order.get(r.get("Severity", "").strip().lower(), 3)
    )

    return filtered[:8]


def get_style_data(personality_name: str) -> Optional[dict]:
    """Return the styles() row whose Style Category best matches personality_name.

    Matches by case-insensitive substring of the Style Category column.
    """
    style_rows = styles()
    # Map personality names to approximate style category substrings
    STYLE_HINTS: dict[str, str] = {
        "minimal":          "minimalism",
        "modern_saas":      "flat",
        "corporate":        "minimalism",
        "dark_premium":     "dark",
        "editorial":        "editorial",
        "bento":            "bento",
        "gradient_modern":  "gradient",
        "warm_artisan":     "organic",
        "glassmorphism":    "glassmorphism",
        "neo_brutalism":    "brutalism",
        "aurora":           "aurora",
        "claymorphism":     "claymorphism",
        "flat_minimal":     "flat",
        "vibrant_block":    "vibrant",
        "luxury_glass":     "liquid glass",
        "organic_nature":   "organic",
        "soft_ui":          "soft ui",
        "dark_oled":        "dark",
    }
    hint = STYLE_HINTS.get(personality_name.lower(), personality_name.lower())

    for row in style_rows:
        cat = row.get("Style Category", "").lower()
        if hint in cat:
            return row

    # Secondary pass: check keywords column
    for row in style_rows:
        keywords = row.get("AI Prompt Keywords", "").lower()
        if hint in keywords:
            return row

    return None
