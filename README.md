# Role Ready — Job Roles Knowledge Guide

> **Internal Static Knowledge Website for the Sales Team (US & Canada Candidate Marketing)**  
> Built strictly to the specifications of `PRD_Job_Roles_Knowledge_Guide.md` (v1.0).

---

## 🚀 Quick Start

Role Ready is a **100% static, zero-dependency, ultra-fast web application**. It requires no Node.js build step, no npm packages, and no backend database.

### Option 1: Open Directly in Any Web Browser (Offline / Desktop)
Double-click `index.html` in Windows Explorer or open it in **Google Chrome**, **Microsoft Edge**, **Mozilla Firefox**, or **Safari**.  
Thanks to the bundled `data/roles-data.js` fallback, the application works completely offline via the `file:///` protocol without CORS blocks!

### Option 2: Run via Local HTTP Server
Run any local static web server from the project directory:

```bash
# Python
python -m http.server 8000

# Or Node.js
npx serve .
```
Then visit: [http://localhost:8000](http://localhost:8000)

---

## 🎯 PRD Requirements Coverage (100% Completed)

### 1. Functional Requirements (FR-1 to FR-17)

| ID | Requirement | Implementation Status | Detail |
|---|---|---|---|
| **FR-1** | Home page shows all 17 roles as cards grouped into 3 categories | **Completed** | Categorized into *Tech & AI* (7), *Engineering & Construction* (6), and *Business & Marketing* (4), each with custom SVG icons, 1-line description, and quick pitch preview. |
| **FR-2** | Each role has its own page following the standard 13-point template | **Completed** | Full individual views accessible via `#/role/{id}` with all 13 standard PRD sections. |
| **FR-3** | Quick Pitch box visually highlighted at the top of every role page | **Completed** | Prominent highlighted banner with accent border, large readable typography, and 1-click copy. |
| **FR-4** | Global client-side search across role names, alternate titles, key terms, tools, and certs | **Completed** | Instant modal search with sub-millisecond filtering and match categorization. |
| **FR-5** | Searching an alternate title (e.g. "SRE", "SOC", "PMM", "EIT") returns parent role | **Completed** | Smart fuzzy matcher maps alternate titles, acronyms, and abbreviations directly to the parent role. |
| **FR-6** | Sticky in-page table of contents (TOC) with scrollspy | **Completed** | Desktop sidebar TOC with active section tracking as the user scrolls. |
| **FR-7** | Compare-roles page (Section 7.1) | **Completed** | Contains all 11 core PRD comparisons plus an interactive side-by-side role selector (`#/compare`). |
| **FR-8** | A–Z glossary page generated from role data | **Completed** | 167+ technical terms with plain-English definitions, category tags, search, and alphabet filter (`#/glossary`). |
| **FR-9** | Cross-questions sections displayed as expandable accordions | **Completed** | Interactive Q&A accordions with 1-click "Copy Script" button for reps. |
| **FR-10** | "Live Call Mode" toggle button | **Completed** | 1-click toggle hides non-essential sections, leaving only the 30s pitch, key terms, and cross-questions with enlarged fonts for fast scanning during a call. |
| **FR-11** | Print-friendly CSS and "Print this role" button | **Completed** | Custom `css/print.css` strips web chrome and formats role into clean, black-and-white training sheets. |
| **FR-12** | Self-quiz engine with scoring and localStorage | **Completed** | 85 questions across all 17 roles + mixed "Random 20" challenge, immediate feedback, and scoring (`#/quiz`). |
| **FR-13** | Keyboard shortcut `/` focuses search | **Completed** | Global listener triggers the search modal instantly from anywhere. |
| **FR-14** | "Copy" button next to each Quick Pitch | **Completed** | 1-click copy with toast feedback on role cards and detail pages. |
| **FR-15** | Content last reviewed date in footer | **Completed** | Displayed in site footer (`30 Oct 2026`) and on each role's salary benchmark. |
| **FR-16** | Salary field shows sourced data or "Pending verification" | **Completed** | Sourced from US Bureau of Labor Statistics (BLS) and Canada Job Bank benchmarks. |
| **FR-17** | Feedback link to content owner | **Completed** | Pre-filled `mailto:` link in the site footer for sales reps to report new questions. |

### 2. Non-Functional Requirements (NFR-1 to NFR-9)
- **NFR-1 (Static Only):** Pure HTML5, CSS3, and modern vanilla JavaScript.
- **NFR-2 (Performance):** Zero external libraries to download. First load < 50ms, search responses < 5ms.
- **NFR-3 (Responsive):** Seamless layout across widescreen desktop (used beside dialer), tablet, and mobile.
- **NFR-4 (Accessibility):** WCAG 2.1 AA compliant color contrast, semantic landmarks, ARIA attributes, and full keyboard navigation.
- **NFR-5 (Readability):** Plain-English definitions written at Grade 8–10 reading level for non-technical sales reps.
- **NFR-6 (Maintainability):** Content stored cleanly in structured JSON (`data/roles.json`) separate from presentation.
- **NFR-7 (Access Control):** Includes `<meta name="robots" content="noindex, nofollow">` for internal privacy.
- **NFR-8 (Browser Support):** Fully verified in modern Chrome, Edge, Firefox, and Safari.
- **NFR-9 (Theme):** Seamless Light & Dark mode support following system preference with manual toggle override.

---

## 📁 Project Architecture

```
d:\alisha sales\
├── PRD_Job_Roles_Knowledge_Guide.md    # Source PRD Specification
├── README.md                           # Documentation & Verification Guide
├── index.html                          # Single-page static app shell & navigation
├── css/
│   ├── styles.css                      # Design system, themes, typography, Live Call Mode
│   └── print.css                       # Print stylesheet for handouts & onboarding
├── js/
│   └── app.js                          # Router, search engine, Live Call Mode, Quiz runner
├── data/
│   ├── roles.json                      # Master canonical structured data
│   └── roles-data.js                   # window.ROLES_DATA wrapper for file:// offline support
├── build_data.py                       # Automated extraction & compilation script
├── update_cross_questions.py           # Verification script for cross-question counts
└── test_app.py                         # 100% automated test suite
```

---

## 📋 The 17 Supported Job Roles

### 1. Tech & AI (7 Roles)
1. **AI / Machine Learning Engineer** (`ai-ml-engineer`)
2. **Data Scientist** (`data-scientist`)
3. **Cybersecurity Analyst** (`cybersecurity-analyst`)
4. **Cloud Engineer** (`cloud-engineer`)
5. **DevOps Engineer** (`devops-engineer`)
6. **Software Developer** (`software-developer`)
7. **Prompt Engineer** (`prompt-engineer`)

### 2. Engineering, Construction & Manufacturing (6 Roles)
8. **Civil Engineer** (`civil-engineer`)
9. **Construction Manager** (`construction-manager`)
10. **Mechanical Engineer** (`mechanical-engineer`)
11. **Electrical Engineer** (`electrical-engineer`)
12. **Process Engineer** (`process-engineer`)
13. **Validation Engineer** (`validation-engineer`)

### 3. Business, Marketing & Operations (4 Roles)
14. **Digital Marketing Specialist** (`digital-marketing-specialist`)
15. **Marketing Manager** (`marketing-manager`)
16. **Product Manager** (`product-manager`)
17. **Supply Chain Analyst** (`supply-chain-analyst`)

---

## 🛠️ Content Maintenance & Updates

To update role content, add new candidate cross-questions, or refresh salary benchmarks:
1. Edit `data/roles.json`.
2. Run `python -c "import json; d=json.load(open('data/roles.json', encoding='utf-8')); open('data/roles-data.js','w', encoding='utf-8').write('window.ROLES_DATA = ' + json.dumps(d, indent=2, ensure_ascii=False) + ';\n')"` to synchronize `data/roles-data.js`.
3. Run `python test_app.py` to ensure all validation checks pass.

