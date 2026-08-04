# PlainQR → BrandedQR — План апгрейда

> Апгрейд существующего PlainQR до Branded QR Generator с killer features из крон-ниши (99/100 Suggest score).
> Методология: Игорь Зуев. Стек: $0. Базa: существующий MVP + 10 SEO landing pages.

---

## Текущее состояние PlainQR

| Компонент | Статус |
|-----------|--------|
| QR генератор (qrcode.js) | ✅ Live |
| 12 типов QR | ✅ Live |
| 10 SEO landing pages | ✅ Live |
| QR download (canvas.toDataURL) | ✅ Fixed |
| Git | ✅ Initialized |
| Домен | ❌ Не куплен |
| Оплата | ❌ Не интегрирована |
| GSC | ❌ Не настроен |
| Logo embedding | ❌ Нет |
| Custom dot styles | ❌ Нет |
| Gradient fills | ❌ Нет |
| Bulk CSV → PDF | ❌ Нет |

## Целевое состояние BrandedQR

| Компонент | План |
|-----------|------|
| QR движок | `qr-code-styling` (CDN) — замена qrcode.js |
| Logo embedding | Upload → overlay на QR |
| Custom dot styles | Square, rounded, heart, pixel |
| Gradient fills | Linear/radial для dots + background |
| Bulk CSV → PDF | jsPDF, n-per-page, print-ready |
| Оплата | Cloudflare Worker + USDT TRC-20 ($7 lifetime) |
| Домен | plainqr.com или branded-qr.com |
| GSC | Добавить + sitemap + индексация |

---

## Этапы апгрейда

### Этап 1: QR Engine Swap (1 день)
- [ ] Заменить `qrcode.js` на `qr-code-styling` (CDN)
- [ ] Адаптировать generateQR() под новый API
- [ ] Сохранить все 12 типов QR (URL, WiFi, vCard, etc.)
- [ ] Тест: базовый QR генерируется, скачивается PNG

### Этап 2: Logo + Custom Styles (2 дня)
- [ ] Logo upload (FileReader → Image → overlay)
- [ ] Logo positioning (center, size slider)
- [ ] Dot styles: square, rounded, heart, pixel
- [ ] Gradient fills (linear/radial) для dots
- [ ] Background color + transparent option
- [ ] Тест: QR с логотипом сканируется

### Этап 3: Bulk CSV → PDF (1 день)
- [ ] Bulk mode: textarea/CSV paste → массив данных
- [ ] Генерация N QR-кодов из CSV
- [ ] PDF export: A4 layout, n-per-page, labels
- [ ] ZIP export: индивидуальные PNG/SVG файлы
- [ ] Прогресс-бар для batch

### Этап 4: Paywall + Payment (1 день)
- [ ] Счётчик: 5 free QR (single mode, PNG only, basic colors)
- [ ] Paywall modal: $7 lifetime (USDT TRC-20)
- [ ] Cloudflare Worker `plainqr-payment` (по аналогии с csvtojson)
- [ ] После оплаты: SVG export, custom dots, gradient, bulk, PDF
- [ ] Telegram bot уведомления

### Этап 5: Деплой + Домен + GSC (1 день)
- [ ] Деплой на GitHub Pages
- [ ] Домен: plainqr.com (или branded-qr.com)
- [ ] DNS: A-записи GitHub Pages + CNAME www
- [ ] Обновить canonical URLs во всех HTML
- [ ] robots.txt + sitemap.xml
- [ ] GSC: добавить + verify + sitemap

### Итого: 6 дней

---

## Монетизация

| Уровень | Цена | Что |
|---------|------|-----|
| Free | $0 | 5 QR (PNG, basic colors, no logo) |
| Lifetime | **$7** | SVG, custom dots, gradient, logo, bulk CSV, PDF |
| Pro Pack (future) | $15 | Animated QR (WebM), API access, brand kit |

## Скиллы

| Скилл | Зачем |
|-------|------|
| `zuev-micro-saas-launch` | Umbrella: Apple Design CSS, payment Worker template |
| `micro-saas-static-frontend` | Static frontend + payment patterns |
| `crypto-payment-tron-worker` | Payment Worker для $7 USDT |
| `static-site-crypto-payments` | Frontend paywall modal |
| `seo-landing-pages` | Обновить landing pages под новые фичи |

---

*План составлен 1 августа 2026. Методология: Игорь Зуев. Базa: существующий PlainQR MVP.*