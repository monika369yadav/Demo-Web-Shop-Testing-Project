# Requirement Traceability Matrix (RTM) — Demo Web Shop

The RTM maps each requirement/feature to its corresponding test scenarios, test cases, and execution status — ensuring complete test coverage across the application.

| Req ID | Requirement / Feature | Test Scenario ID(s) | Test Case ID(s) | Linked Bug(s) | Coverage Status |
|---|---|---|---|---|---|
| REQ-01 | Users can view all products under Books category | TS-BOOK-01 | TC-001 | BUG-001 | ✅ Covered |
| REQ-02 | Users can add an available product to cart | TS-BOOK-02 | TC-002 | — | ✅ Covered |
| REQ-03 | Unavailable products clearly indicate stock status | TS-BOOK-03 | TC-001 | BUG-001 | ⚠️ Covered — Failed |
| REQ-04 | Users can sort products by price/name | TS-BOOK-04 | TC-003 | — | ⏳ In Progress |
| REQ-05 | Users can update item quantity in cart | TS-CART-02 | TC-004 | — | ⏳ In Progress |
| REQ-06 | Registration form validates incorrect email format | TS-AUTH-02 | TC-005, TC-006 | — | ⏳ In Progress |
| REQ-07 | Guest checkout completes successfully | TS-CHK-01 | — | — | 🔲 Not Started |
| REQ-08 | Login fails gracefully with invalid credentials | TS-AUTH-04 | TC-008 | — | ✅ Covered |
| REQ-09 | Search returns relevant results | TS-SRCH-01 | TC-015 | BUG-003 | ⚠️ Covered — Failed |
| REQ-10 | New user can register with valid, unique details | TS-AUTH-01 | TC-007 | — | ✅ Covered |
| REQ-11 | Registered user can log in with valid credentials | TS-AUTH-03 | TC-009 | — | ✅ Covered |
| REQ-12 | Registered user checkout flow completes successfully | TS-CHK-02 | TC-014 | — | ✅ Covered |
| REQ-13 | Order total correctly reflects payment method fees | TS-CHK-04 | TC-014 | — | ✅ Covered |
| REQ-14 | "Add to Cart" button is visible for all products across all categories | — | TC-001, TC-011 | BUG-001 | ⚠️ Covered — Failed |
| REQ-15 | Manufacturer pages display products or an appropriate empty-state message | — | TC-012 | BUG-002 | ⚠️ Covered — Failed |
| REQ-16 | State/province list is available for supported countries at checkout | TS-CHK-03 | TC-013 | BUG-004 | ⚠️ Covered — Failed |
| REQ-17 | Gift Card requires recipient details before being added to cart | — | TC-010 | — | ✅ Covered |

**Legend:**
✅ Covered & Passed &nbsp;|&nbsp; ⚠️ Covered & Failed &nbsp;|&nbsp; ⏳ In Progress &nbsp;|&nbsp; 🔲 Not Started

---

*This RTM will be updated continuously as new test cases are executed and new requirements are identified.*
