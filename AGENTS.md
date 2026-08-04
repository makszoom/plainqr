---
name: plainqr
version: 1.0.0
updated: 2026-07-28
---

# AGENTS.md — plainqr

> Static QR Code Generator. No watermark. No server. 12 types (WiFi, vCard, URL, etc.). Lifetime $5.

## Basic Data

| Key | Value |
|-----|-------|
| Domain | ⏳ Not purchased |
| Temp URL | https://makszoom.github.io/plainqr/ |
| Repo | makszoom/plainqr |
| Hosting | GitHub Pages |
| Payment | ⏳ Not integrated |
| GSC | ⏳ Not set up |
| Git | ✅ Initialized (1 commit) |

## Architecture

```
plainqr/
├── index.html              # Main QR generator
├── static/
│   ├── css/                # Styles
│   ├── js/                 # qrcode.js + app logic
│   └── qr/                 # Generated QR assets
├── business-card.html      # SEO landing
├── contact.html            # SEO landing
├── event.html              # SEO landing
├── instagram.html          # SEO landing
├── location.html           # SEO landing
├── menu.html               # SEO landing
├── payment.html            # SEO landing
├── pdf.html                # SEO landing
├── wifi.html               # SEO landing
├── youtube.html            # SEO landing
├── template.html           # Generic template
├── templates/              # Template components
├── audit.py                # SEO audit script
├── LICENSE                 # MIT
└── .gitignore
```

## Stack

| Layer | Tech | Cost |
|-------|------|------|
| Frontend | HTML + CSS + vanilla JS | $0 |
| QR engine | qrcode.js (CDN) | $0 |
| Hosting | GitHub Pages | $0 |
| Domain | Cloudflare Registrar | ~$12/yr (pending) |
| Payment | ⏳ Not started |

## Key Decisions

- **qrcode.js** — lightweight, no watermark, CDN-loaded.
- **12 QR types** — URL, WiFi, vCard, email, phone, SMS, event, location, payment, PDF, Instagram, YouTube.
- **Each type = landing page** — 12 SEO pages for organic traffic.
- **Static generation** — no server, no API calls. Pure HTML/CSS/JS.
- **Git initialized** — but only 1 commit. Needs active development.

## Status

| Component | Status |
|-----------|--------|
| Core QR generator | ✅ Live |
| 12 types + landings | ✅ Live |
| Styling + responsive | ✅ Live |
| PWA manifest | ❌ Not added |
| Payment integration | ❌ Not started |
| Custom domain | ❌ Not purchased |
| GSC | ❌ Not set up |

## Next Steps

1. Add PWA manifest + icon
2. Integrate payment (reuse pdf-merge Worker pattern)
3. Buy domain + DNS + GSC
4. Update all canonical URLs

## Documentation Update Rule

**After significant changes — update this file before ending session.**

Significant:
- New QR type added
- Payment integrated
- Domain purchased
- PWA added

Not significant:
- Content edits in landings
- Color changes
