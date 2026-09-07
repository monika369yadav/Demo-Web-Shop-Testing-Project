# Test Scenarios — Demo Web Shop

High-level test scenarios covering all major modules of the application. Each scenario will be broken down into detailed test cases in [Test-Cases.md](../Test-Cases/Test-Cases.md).

---

## 1. Books / Product Listing Module

| Scenario ID | Scenario Description |
|---|---|
| TS-BOOK-01 | Verify all products under the Books category load correctly with image, title, and price |
| TS-BOOK-02 | Verify "Add to Cart" button is available and functional for all in-stock products |
| TS-BOOK-03 | Verify products with no stock status display an appropriate availability message |
| TS-BOOK-04 | Verify sorting functionality (Position, Name, Price Low-High, Price High-Low) |
| TS-BOOK-05 | Verify "Filter by Price" functionality returns correct results |
| TS-BOOK-06 | Verify pagination / "Display per page" option works correctly |

## 2. Shopping Cart Module

| Scenario ID | Scenario Description |
|---|---|
| TS-CART-01 | Verify items can be added to cart from product listing and product detail pages |
| TS-CART-02 | Verify cart quantity can be updated and totals recalculate correctly |
| TS-CART-03 | Verify items can be removed from cart |
| TS-CART-04 | Verify cart persists data correctly within a session |
| TS-CART-05 | Verify empty cart displays appropriate message |

## 3. Checkout Module

| Scenario ID | Scenario Description |
|---|---|
| TS-CHK-01 | Verify guest checkout flow completes successfully |
| TS-CHK-02 | Verify registered user checkout flow completes successfully |
| TS-CHK-03 | Verify mandatory field validations on billing/shipping address |
| TS-CHK-04 | Verify order summary displays correct items, quantity, and total price |

## 4. Register / Login Module

| Scenario ID | Scenario Description |
|---|---|
| TS-AUTH-01 | Verify new user registration with valid details |
| TS-AUTH-02 | Verify registration form validation for invalid/empty inputs |
| TS-AUTH-03 | Verify login with valid credentials |
| TS-AUTH-04 | Verify login failure with invalid credentials shows correct error message |
| TS-AUTH-05 | Verify "Forgot Password" flow |

## 5. Search Module

| Scenario ID | Scenario Description |
|---|---|
| TS-SRCH-01 | Verify search returns relevant results for valid keywords |
| TS-SRCH-02 | Verify search behavior for invalid/no-match keywords |
| TS-SRCH-03 | Verify search behavior for empty search input |

---

*Status: Scenarios added are based on testing performed so far and will be expanded as new modules are explored.*
