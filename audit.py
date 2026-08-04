#!/usr/bin/env python3
"""
PlainQR Site Auditor
Автоматическая проверка всех страниц сайта.
Проверяет: HTTP статус, title, ссылки, QR генератор, Schema.org, размеры.
"""

import urllib.request
import urllib.error
import re
import json
from datetime import datetime

BASE_URL = "https://makszoom.github.io/plainqr"
PAGES = [
    "index.html", "menu.html", "wifi.html", "business-card.html",
    "pdf.html", "youtube.html", "instagram.html", "contact.html",
    "event.html", "location.html", "payment.html"
]

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

results = []
issues = []

def check_page(page):
    """Проверка одной страницы"""
    url = f"{BASE_URL}/{page}"
    page_results = {"page": page, "checks": {}}
    
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Cache-Control': 'no-cache'
        })
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8')
            size_kb = len(content) / 1024
            
            # 1. HTTP Status
            page_results["checks"]["http_status"] = response.status == 200
            
            # 2. Title tag
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            page_results["checks"]["title"] = bool(title_match)
            page_results["title_text"] = title_match.group(1) if title_match else "N/A"
            
            # 3. Meta description
            desc_match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', content, re.IGNORECASE)
            page_results["checks"]["meta_desc"] = bool(desc_match)
            
            # 4. QR Generator (qrcode.js)
            page_results["checks"]["qr_generator"] = "qrcode.min.js" in content or "QRCode" in content
            
            # 5. Schema.org
            page_results["checks"]["schema_org"] = "schema.org" in content.lower() or "application/ld+json" in content
            
            # 6. FAQ section
            page_results["checks"]["faq"] = "FAQ" in content or "frequently asked" in content.lower()
            
            # 7. Canonical URL
            page_results["checks"]["canonical"] = "canonical" in content.lower()
            
            # 8. Responsive viewport
            page_results["checks"]["viewport"] = "width=device-width" in content
            
            # 9. File size
            page_results["checks"]["size_ok"] = size_kb < 100  # Under 100KB
            page_results["size_kb"] = size_kb
            
            # 10. Internal links check (only for index.html)
            if page == "index.html":
                broken_links = []
                # Find all .html links
                links = re.findall(r'href="([^"]*\.html)"', content)
                for link in links:
                    if link.startswith('/'):
                        link = link[1:]
                    if link not in PAGES and link != "index.html":
                        broken_links.append(link)
                page_results["checks"]["internal_links"] = len(broken_links) == 0
                page_results["broken_links"] = broken_links
            
            # 11. Check for canvas.toDataURL (bug fix)
            page_results["checks"]["download_fix"] = "canvas.toDataURL('image/png')" in content
            
            # 12. Geist font (Vercel design)
            page_results["checks"]["geist_font"] = "Geist" in content
            
            # 13. H1 tag
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            page_results["checks"]["h1"] = bool(h1_match)
            
    except urllib.error.HTTPError as e:
        page_results["checks"]["http_status"] = False
        page_results["error"] = f"HTTP {e.code}"
        issues.append({"page": page, "severity": "High", "issue": f"HTTP Error {e.code}"})
    except Exception as e:
        page_results["checks"]["http_status"] = False
        page_results["error"] = str(e)
        issues.append({"page": page, "severity": "Critical", "issue": str(e)})
    
    results.append(page_results)
    return page_results

def print_results():
    """Вывод результатов"""
    print("=" * 70)
    print("   PLAINQR SITE AUDIT REPORT")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"   URL: {BASE_URL}")
    print("=" * 70)
    
    total_checks = 0
    passed_checks = 0
    
    for r in results:
        page = r["page"]
        checks = r["checks"]
        
        print(f"\n📄 {page}")
        print("-" * 50)
        
        if "error" in r:
            print(f"  {Colors.RED}❌ ERROR: {r['error']}{Colors.END}")
            continue
        
        for check_name, passed in checks.items():
            total_checks += 1
            if passed:
                passed_checks += 1
                symbol = f"{Colors.GREEN}✅{Colors.END}"
            else:
                symbol = f"{Colors.RED}❌{Colors.END}"
                issues.append({"page": page, "severity": "Medium", "issue": f"Failed: {check_name}"})
            
            label = {
                "http_status": "HTTP 200",
                "title": "Title tag",
                "meta_desc": "Meta description",
                "qr_generator": "QR Generator",
                "schema_org": "Schema.org",
                "faq": "FAQ Section",
                "canonical": "Canonical URL",
                "viewport": "Mobile responsive",
                "size_ok": "File size < 100KB",
                "internal_links": "Internal links",
                "download_fix": "QR download fix",
                "geist_font": "Geist font",
                "h1": "H1 heading"
            }.get(check_name, check_name)
            
            print(f"  {symbol} {label}")
        
        if "size_kb" in r:
            print(f"  📊 Size: {r['size_kb']:.1f} KB")
        if "title_text" in r:
            print(f"  📝 Title: {r['title_text'][:50]}...")
        if "broken_links" in r and r["broken_links"]:
            print(f"  {Colors.RED}⚠️  Broken links: {', '.join(r['broken_links'])}{Colors.END}")
    
    # Summary
    print("\n" + "=" * 70)
    print("   SUMMARY")
    print("=" * 70)
    print(f"\n  Total checks: {total_checks}")
    print(f"  Passed: {Colors.GREEN}{passed_checks}{Colors.END}")
    print(f"  Failed: {Colors.RED}{total_checks - passed_checks}{Colors.END}")
    print(f"  Success rate: {passed_checks/total_checks*100:.1f}%")
    
    if issues:
        print(f"\n  {Colors.YELLOW}Issues found: {len(issues)}{Colors.END}")
        for issue in issues:
            severity_color = Colors.RED if issue["severity"] == "Critical" else Colors.YELLOW
            print(f"    {severity_color}[{issue['severity']}]{Colors.END} {issue['page']}: {issue['issue']}")
    else:
        print(f"\n  {Colors.GREEN}🎉 No issues found!{Colors.END}")
    
    # SEO Score
    seo_score = passed_checks / total_checks * 100
    if seo_score >= 95:
        grade = "A+"
    elif seo_score >= 90:
        grade = "A"
    elif seo_score >= 80:
        grade = "B"
    elif seo_score >= 70:
        grade = "C"
    else:
        grade = "D"
    
    print(f"\n  SEO Score: {seo_score:.1f}% — Grade {grade}")
    print("=" * 70)

if __name__ == "__main__":
    print("🔍 Starting PlainQR site audit...\n")
    
    for page in PAGES:
        check_page(page)
        print(f"  ✅ Checked {page}")
    
    print_results()
    
    # Save report
    report = {
        "date": datetime.now().isoformat(),
        "url": BASE_URL,
        "pages_tested": len(PAGES),
        "results": results,
        "issues": issues
    }
    
    with open("plainqr_audit_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("\n📄 Report saved: plainqr_audit_report.json")
