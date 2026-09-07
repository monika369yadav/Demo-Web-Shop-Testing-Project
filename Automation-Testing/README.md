# Automation Testing — Demo Web Shop (Python + Selenium + pytest)

This folder contains the automated test suite for the Demo Web Shop project, built as a natural next step after completing manual testing. It automates the same core scenarios documented in [Test-Cases.md](../Test-Cases/Test-Cases.md), using industry-standard tools and the Page Object Model (POM) design pattern.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.9+ | Programming language |
| Selenium WebDriver | Browser automation |
| pytest | Test runner and assertions |
| webdriver-manager | Automatically downloads the correct ChromeDriver version |

---

## 📁 Folder Structure

```
Automation-Testing/
├── README.md
├── requirements.txt
├── conftest.py              → shared pytest fixture (opens/closes the browser)
├── pages/                   → Page Object Model classes
│   ├── base_page.py         → common reusable methods (click, type, wait, logout)
│   ├── register_page.py
│   ├── login_page.py
│   └── search_page.py
└── tests/                   → actual test cases (pytest files)
    ├── test_register.py     → TC-006, TC-007
    ├── test_login.py        → TC-008, TC-009
    └── test_search.py       → TC-015 (known bug — BUG-003)
```

---

## ⚙️ Setup Instructions

1. Make sure Python 3.9+ and Google Chrome are installed on your machine.
2. Open a terminal inside this `Automation-Testing/` folder.
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Tests

Run all tests:
```
pytest -v
```

Run a specific test file:
```
pytest tests/test_login.py -v
```

Run a specific test:
```
pytest tests/test_login.py::test_login_succeeds_with_correct_credentials -v
```

---

## 🧪 Test Coverage Mapping

| Manual Test Case | Automated Test | File |
|---|---|---|
| TC-006 | `test_registration_fails_with_duplicate_email` | `test_register.py` |
| TC-007 | `test_registration_with_valid_details` | `test_register.py` |
| TC-008 | `test_login_fails_with_incorrect_password` | `test_login.py` |
| TC-009 | `test_login_succeeds_with_correct_credentials` | `test_login.py` |
| TC-015 | `test_search_returns_results_for_valid_keyword` | `test_search.py` |

---

## ⚠️ Important Notes

- **`test_login.py`** uses a fixed test account (`TEST_EMAIL` / `TEST_PASSWORD` at the top of the file). Update these values to match a real registered account on the demo site before running, since the demo site occasionally resets its data.
- **`test_search.py`** is intentionally marked `@pytest.mark.xfail` — it documents a known, currently-open bug (BUG-003). The test is *expected* to fail until the underlying application bug is fixed. This is a common real-world QA automation practice: automated tests can capture and track known defects, not just passing scenarios.
- These tests run against the **live public demo site**, so occasional flakiness (slow load, site resets) is possible — this is normal for a shared public training environment, not a flaw in the test code itself.

---

## 🚀 Next Steps (Planned)

- Automate Add to Cart flow (TC-002, TC-011)
- Automate Checkout flow (TC-014)
- Add HTML test reports (`pytest-html`)
- Set up GitHub Actions to run tests automatically on each commit (CI/CD)
