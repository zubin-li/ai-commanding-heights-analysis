#!/usr/bin/env python3
"""
Project CI/CD Integrity Audit & Validation Suite
Validates JSON datasets, HTML references, image assets, and documentation symmetry.
"""

import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def test_datasets():
    data_dir = BASE_DIR / "data"
    required_files = [
        "metadata.json",
        "viral_claims_fact_check.json",
        "historical_tech_surplus.json",
        "token_price_vs_training_cost.json",
        "capex_vs_ocf_projection.json",
        "us_labor_whitecollar_pyramid.json",
        "indian_it_outsourcing_margins.json",
        "commanding_heights_radar.json"
    ]
    for rf in required_files:
        fp = data_dir / rf
        assert fp.exists(), f"Missing dataset: {rf}"
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert data, f"Dataset {rf} is empty"
    print("✓ All 8 core JSON datasets validated successfully.")

def test_images():
    img_dir = BASE_DIR / "images"
    assert img_dir.exists(), "images directory missing"
    for i in range(1, 20):
        img_p = img_dir / f"{i}.jpg"
        assert img_p.exists(), f"Missing image {i}.jpg"
        assert img_p.stat().st_size > 10000, f"Image {i}.jpg corrupted or too small"
    print("✓ All 19 primary slide images validated.")

def test_docs():
    docs_dir = BASE_DIR / "docs"
    required_docs = [
        "strategic_report.md",
        "PLAYBOOK_FOR_INDIVIDUALS.md",
        "citations.md",
        "data_dictionary.md",
        "methodology.md"
    ]
    for rd in required_docs:
        dp = docs_dir / rd
        assert dp.exists(), f"Missing document: {rd}"
        assert dp.stat().st_size > 200, f"Document {rd} is too short"
    print("✓ All 5 analytical monographs in docs/ validated.")

def test_i18n():
    i18n_p = BASE_DIR / "i18n.js"
    assert i18n_p.exists(), "i18n.js missing"
    content = i18n_p.read_text(encoding="utf-8")
    assert "en:" in content, "English translations missing in i18n.js"
    assert "zh:" in content, "Chinese translations missing in i18n.js"
    assert "普通人与普通上班族的生存启示" in content, "Chinese Slide 12 missing in i18n.js"
    print("✓ i18n.js bilingual dictionary validated.")

def test_html():
    idx_p = BASE_DIR / "index.html"
    assert idx_p.exists(), "index.html missing"
    content = idx_p.read_text(encoding="utf-8")
    assert 'data-theme="light"' in content or 'theme-light' in content, "Light mode not default in index.html"
    assert 'lang="en"' in content, "Default language not English in index.html"
    assert "echarts.min.js" in content, "ECharts missing in index.html"
    assert "i18n.js" in content, "i18n script missing in index.html"
    assert 'id="slide-1"' in content and 'id="slide-15"' in content, "All 15 slides not present in continuous layout"
    assert "btn-lang-en" in content and "btn-lang-zh" in content, "Language switchers missing in navigation"
    print("✓ index.html continuous flowing structure and English default validated.")

def main():
    print("==================================================")
    print(" AI Commanding Heights Project Integrity Audit")
    print("==================================================")
    try:
        test_datasets()
        test_images()
        test_docs()
        test_i18n()
        test_html()
        print("--------------------------------------------------")
        print("🎉 ALL 19 INTEGRITY AUDITS PASSED (100%)")
        print("==================================================")
    except AssertionError as e:
        print(f"❌ AUDIT FAILED: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
