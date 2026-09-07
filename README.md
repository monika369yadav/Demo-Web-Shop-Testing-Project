# Demo Web Shop — Manual Testing Project

A complete manual testing portfolio project performed on the **Demo Web Shop** (sample e-commerce application by Tricentis), built to demonstrate practical QA skills including test case design, exploratory testing, bug reporting, and requirement traceability.

---

## 📌 Project Overview

This project simulates a real-world QA engagement on an e-commerce platform. The objective was to independently plan, design, and execute manual test cases across key modules of the application, identify defects, document them professionally, and maintain full testing artifacts — the same way a QA Tester would in an actual product team.

---

## 🌐 Application Under Test (AUT)

**Application:** Demo Web Shop
**URL:** [https://demowebshop.tricentis.com](https://demowebshop.tricentis.com)
**Type:** Sample E-Commerce Web Application (built on nopCommerce)
**Provided by:** Tricentis (for public QA practice and training purposes)

---

## 🎯 Testing Scope

- Functional testing of core e-commerce flows (Browse, Cart, Checkout, Account)
- UI/UX validation and usability observations
- Cross-browser sanity checks
- Negative and boundary testing on forms and inputs
- Defect identification, classification, and reporting

**Out of Scope:** Performance testing, security/penetration testing, backend/database testing, automated test execution

---

## 🧩 Modules Tested

| Module | Description |
|---|---|
| Books | Product listing, sorting, filtering, Add to Cart |
| Computers | Category browsing, product comparison |
| Electronics | Product listing and detail pages |
| Shopping Cart | Add/remove items, quantity updates, totals |
| Checkout | Guest checkout, address, payment flow |
| Register / Login | Account creation, authentication, validation |
| Search | Store-wide search functionality |

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Browser DevTools | UI inspection, responsive checks |
| Excel / Markdown | Test case and bug documentation |
| GitHub | Version control & portfolio hosting |
| Screenshots (Snipping Tool) | Visual defect evidence |
| ChatGPT / Claude AI | Assisted in structuring documentation and brainstorming test scenarios |

---

## 🔍 Key Findings and Observations

- **Site-wide pattern:** Products missing the "Add to Cart" button and stock-status message were found across multiple categories — Books, Computers (Desktops), and Electronics (Camera/Photo, Cell phones) — not limited to a single module (see [BUG-001](./Bug-Reports/Bug-Reports.md#bug-001))
- **Critical:** Store search returns "No products found" for every keyword tested, including exact, existing category names like "Books" and "Computers" — the search feature is effectively non-functional (see [BUG-003](./Bug-Reports/Bug-Reports.md#bug-003))
- Manufacturer page ("Tricentis") renders with no products and no empty-state message (see [BUG-002](./Bug-Reports/Bug-Reports.md#bug-002))
- State/Province dropdown does not list actual states when Country = India during checkout (see [BUG-004](./Bug-Reports/Bug-Reports.md#bug-004))
- Registration and Login flows (both positive and negative paths) and Gift Card recipient validation were tested and function correctly
- Cart and pricing calculations, including payment-method additional fees, were verified to be accurate at checkout
- A cart usability gap was also noted — no single-click "Remove" button on cart items (see [Suggestions](./Suggestions/UI-UX-Improvements.md))

*(This section is updated continuously as testing progresses.)*

---

## 📁 Repository Structure

```
Demo-Web-Shop-Manual-Testing-Project/
│
├── README.md
├── Test-Scenarios/
│   └── Test-Scenarios.md
├── Test-Cases/
│   └── Test-Cases.md
├── Bug-Reports/
│   └── Bug-Reports.md
├── RTM/
│   └── Requirement-Traceability-Matrix.md
├── Suggestions/
│   └── UI-UX-Improvements.md
└── Screenshots/
    ├── Defects/
    └── Observations/
```

---

## 👩‍💻 About Me

**Monika Yadav**
QA Tester | Manual Testing | Fresher
🔗 [LinkedIn](https://www.linkedin.com/in/monikayadav10)

This project is part of my QA testing portfolio, built to apply manual testing concepts on a live application as a fresher transitioning into Quality Assurance.
