# ⚖️ LexiNLP — Legal Document NLP & Contract Intelligence Platform

A full-stack, enterprise-grade **Natural Language Processing (NLP)** platform designed for automated legal document analysis, clause extraction, legal named entity recognition (NER), quantitative contract risk scoring (0–100), deontic modality analysis, semantic redlining/comparison, and conversational legal Q&A.

---

## 🌟 Key Features & NLP Capabilities

### 1. 📑 Multi-Format Document Ingestion & Parsing
- Supports **PDF** (via PyMuPDF), **DOCX**, **TXT**, and markdown documents.
- Cleans and normalizes headers, footers, and legal typography.
- Pre-loaded with **5 realistic sample contracts**:
  - *Mutual Non-Disclosure Agreement (NDA)*
  - *Enterprise SaaS Master Services Agreement*
  - *Executive Employment & Inventions Agreement*
  - *Commercial Real Estate Lease*
  - *Unilateral High-Risk Vendor Agreement*

### 2. 🏛️ Clause Segmentation & Classification (15+ Taxonomies)
- Structural parsing of contract clauses, preambles, recitals, and signature blocks.
- **Hybrid classification** leveraging domain-specific regex heuristics, spaCy linguistic parsing, and **TF-IDF vector cosine similarity** against curated legal anchor corpora:
  - *Confidentiality, Termination, Indemnification, Limitation of Liability, Intellectual Property, Governing Law, Dispute Resolution/Arbitration, Non-Compete/Non-Solicit, Payment Terms, Force Majeure, Warranties, Severability, Entire Agreement, Data Privacy, Assignment, Preamble, Signatures*.

### 3. 🏷️ Legal Named Entity Recognition (NER) & Deontic Modality
- Extracts:
  - **Parties & Corporate Roles**: Disclosing Party, Receiving Party, Provider, Customer, Employer, Executive.
  - **Dates & Notice Windows**: Effective dates, expiration deadlines, notice periods (e.g. 30 days), survival periods.
  - **Financials & Caps**: Monetary consideration, liability caps, hourly rates, daily delay penalties.
  - **Jurisdictions & Forums**: Governing states, courts, and arbitration forums (JAMS, AAA).
  - **Deontic Modals**: Categorizes clauses into **Mandatory Duties** (*shall, must*), **Prohibitions** (*shall not, may not*), and **Discretionary Rights** (*may, is entitled to*).

### 4. 🚨 Contract Risk & Red-Flag Audit Engine (0–100 Score)
- Quantifies contract risk on a calibrated 0–100 scale (*Low, Moderate, High, Critical Risk*).
- Audits for **12+ severe legal hazards**:
  - Uncapped indemnities & unlimited liability waivers.
  - Unilateral immediate termination clauses (e.g. 24-hour termination without cause).
  - Overly broad global non-compete covenants (> 2 years or worldwide scope).
  - Pre-existing and future IP surrender without payment condition.
  - Silent unilateral contract amendment rights.
  - Punitive liquidated damages and payment withholding.
  - Predatory auto-renewal trap windows.
  - Distant foreign dispute venues.
- Identifies **missing standard safeguards** (Missing Severability, Missing Force Majeure, Missing Arbitration).
- Supplies actionable, lawyer-grade **mitigation recommendations**.

### 5. 📊 Executive Summarization & Obligations Matrix
- **Executive TL;DR**: 5-point executive briefing on parties, term, economics, governing law, and risk profile.
- **Key Terms Card**: Rapid operational reference card.
- **Obligations Matrix**: Clear table assigning who owes what duty to whom.

### 6. 🤖 Interactive Legal Assistant (QA with RAG)
- Natural Language Question Answering over contract contents using **TF-IDF semantic retrieval and evidence citation**.
- Cites exact clause numbers, titles, and highlighted text snippets.
- **Optional Google Gemini AI integration** for enriched generative reasoning when an API key is provided.

### 7. 🔍 Semantic Contract Redline & Diff Engine
- Clause-by-clause comparison between two contract versions (e.g. Doc A vs Doc B).
- Identifies **Unchanged**, **Modified**, **Added**, and **Deleted** provisions.
- Inline visual redline rendering with `<ins>` insertions and `<del>` deletions.
- Calculates overall document similarity percentage and **Risk Delta (B − A)**.

### 8. 📄 Audit Export & Reporting
- Downloadable standalone **Printable HTML / PDF Audit Certificate**.
- Structured **JSON dataset export** for automated legal pipelines and compliance APIs.

---

## 🏗️ Architecture & Technology Stack

| Layer | Technologies Used |
|---|---|
| **NLP Core** | `spaCy (en_core_web_sm)`, `scikit-learn (TF-IDF & Cosine Similarity)`, `PyMuPDF (fitz)` |
| **Backend API** | `FastAPI`, `Uvicorn`, `Pydantic` |
| **Generative AI (Optional)** | `Google Generative AI (Gemini 1.5)` |
| **Frontend UI** | HTML5, Modern Vanilla CSS (Glassmorphism, Dark/Light mode), Vanilla JS SPA |
| **Testing** | `unittest`, `pytest` suite |

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10+ installed

### 2. Installation
```bash
# Clone or navigate to the project directory
cd Nlp-Project

# Install required dependencies
pip install -r requirements.txt
```

### 3. Running the Application on Localhost

#### Option A: Python Command Line
```bash
# Launch server on localhost:8000 and automatically open browser
python run.py

# Or specify custom host / port / live reload:
python run.py --host localhost --port 8000 --reload

# Run in background without opening browser:
python run.py --no-browser
```

#### Option B: Windows 1-Click Launch (Batch Script)
Double click **`run_localhost.bat`** (or run `.\run_localhost.ps1` in PowerShell).

#### Option C: Node / NPM Scripts
```bash
npm start       # Launches server on http://localhost:8000
npm run dev     # Launches with live reload enabled
```

#### Accessing the Local Application
- 🌐 **Web Dashboard**: [http://localhost:8000](http://localhost:8000) (or `http://127.0.0.1:8000`)
- 📚 **Interactive Swagger API Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- 📖 **ReDoc API Specifications**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- 🩺 **API Health Check**: [http://localhost:8000/api/health](http://localhost:8000/api/health)

---

## 🧪 Running Tests

Run the full automated test suite covering all NLP modules, parsers, classifiers, risk scorers, and QA engines:
```bash
pytest
```
Or test live localhost server endpoints:
```bash
python tests/test_full_server.py
```

---

## 📂 Project Structure

```
Nlp-Project/
│
├── backend/
│   ├── app.py                     # Main FastAPI server & REST endpoints
│   ├── nlp/
│   │   ├── __init__.py
│   │   ├── parser.py              # Multi-format document parser (PDF, DOCX, TXT)
│   │   ├── segmenter.py           # Clause & section boundary detector
│   │   ├── clause_classifier.py   # Hybrid rule & TF-IDF clause classifier (15+ categories)
│   │   ├── legal_ner.py           # Legal NER (Parties, Dates, Caps, Jurisdictions, Modals)
│   │   ├── risk_analyzer.py       # Risk scoring (0-100) & 12+ red flag detectors
│   │   ├── summarizer.py          # Executive TL;DR & Rights/Obligations matrix
│   │   ├── contract_diff.py       # Semantic redline & version comparison engine
│   │   └── legal_qa.py            # Local RAG QA engine + optional Gemini LLM
│   ├── samples/                   # 5 Pre-loaded realistic sample contracts
│   │   ├── sample_nda.txt
│   │   ├── sample_saas_agreement.txt
│   │   ├── sample_employment_agreement.txt
│   │   ├── sample_commercial_lease.txt
│   │   └── sample_high_risk_contract.txt
│   └── utils/
│       ├── __init__.py
│       └── report_generator.py    # Formatted HTML/PDF printable audit generator
│
├── frontend/                      # Web User Interface
│   ├── index.html                 # Single Page Application
│   ├── styles.css                 # Dark/Light glassmorphic design system
│   └── app.js                     # Interactive frontend logic, charts, QA, diff
│
├── tests/
│   ├── run_tests.py               # Unit test runner
│   ├── test_nlp_pipeline.py       # Pipeline test suite
│   ├── test_api.py                # REST API test suite
│   └── test_full_server.py        # Live endpoint validation
│
├── run.py                         # Single-command application launcher
├── requirements.txt               # Dependencies list
└── README.md                      # Complete project documentation
```
