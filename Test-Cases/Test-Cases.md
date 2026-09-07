# Test Cases — Demo Web Shop

Detailed test cases derived from [Test-Scenarios.md](../Test-Scenarios/Test-Scenarios.md). Each test case follows a standard QA format used in real-world test management tools.

---

## TC-001

| Field | Details |
|---|---|
| **Test Case ID** | TC-001 |
| **Module** | Books |
| **Title** | Verify "Add to Cart" button visibility for all listed products |
| **Preconditions** | User is on the Demo Web Shop homepage |
| **Steps** | 1. Navigate to Books category 2. Observe each product card 3. Check for "Add to Cart" button on every product |
| **Test Data** | N/A |
| **Expected Result** | "Add to Cart" button should be visible on every product, OR a clear stock-status message should be shown if unavailable |
| **Actual Result** | Some products (e.g., "Fiction", "Fiction EX") do not display the "Add to Cart" button, and no stock message is shown |
| **Status** | ❌ Fail (linked to BUG-001) |

---

## TC-002

| Field | Details |
|---|---|
| **Test Case ID** | TC-002 |
| **Module** | Books |
| **Title** | Verify "Add to Cart" functionality for an in-stock product |
| **Preconditions** | User is on the Books category page |
| **Steps** | 1. Select a product with "Add to Cart" button visible (e.g., "Computing and Internet") 2. Click "Add to Cart" 3. Verify cart icon/count updates |
| **Test Data** | Product: Computing and Internet |
| **Expected Result** | Product should be added to cart and cart count should increase by 1 |
| **Actual Result** | Cart updated correctly with product and count |
| **Status** | ✅ Pass |

---

## TC-003

| Field | Details |
|---|---|
| **Test Case ID** | TC-003 |
| **Module** | Books |
| **Title** | Verify sorting functionality on Books page |
| **Preconditions** | User is on the Books category page |
| **Steps** | 1. Select "Price: Low to High" from Sort by dropdown 2. Observe product order |
| **Test Data** | Sort option: Price Low to High |
| **Expected Result** | Products should be reordered from lowest to highest price |
| **Actual Result** | *(To be filled after execution)* |
| **Status** | ⏳ Not Executed |

---

## TC-004

| Field | Details |
|---|---|
| **Test Case ID** | TC-004 |
| **Module** | Shopping Cart |
| **Title** | Verify cart total updates correctly when quantity is changed |
| **Preconditions** | At least one item is added to cart |
| **Steps** | 1. Go to Shopping Cart page 2. Change quantity of an item 3. Click "Update cart" |
| **Test Data** | Quantity: 2 |
| **Expected Result** | Item subtotal and cart total should recalculate correctly based on new quantity |
| **Actual Result** | *(To be filled after execution)* |
| **Status** | ⏳ Not Executed |

---

## TC-005

| Field | Details |
|---|---|
| **Test Case ID** | TC-005 |
| **Module** | Register/Login |
| **Title** | Verify registration fails with invalid email format |
| **Preconditions** | User is on the Register page |
| **Steps** | 1. Enter all valid details except email 2. Enter invalid email format (e.g., "test@@test") 3. Click Register |
| **Test Data** | Email: test@@test |
| **Expected Result** | System should display a validation error and not create the account |
| **Actual Result** | *(To be filled after execution)* |
| **Status** | ⏳ Not Executed |

---

## TC_JEW_001

| Field | Details |
|---|---|
| **Test Case ID** | TC_JEW_001 |
| **Module** | Jewelry |
| **Title** | Verify "Display per page" behavior when selected value exceeds total available products |
| **Preconditions** | User is on the Jewelry category page |
| **Steps** | 1. Navigate to Jewelry category 2. Select a "Display per page" value greater than the total number of available products (e.g., 8 or more) 3. Observe the products displayed |
| **Test Data** | Display per page: 8 (Jewelry category contains only 5 products) |
| **Expected Result** | All available products should be displayed |
| **Actual Result** | Only 5 products are displayed because the Jewelry category contains only 5 products |
| **Status** | ✅ Pass |
| **Remarks** | Expected behavior. Not a bug. |

---

## TC-006

| Field | Details |
|---|---|
| **Test Case ID** | TC-006 |
| **Module** | Register/Login |
| **Scenario ID** | TS-AUTH-02 |
| **Title** | Verify registration fails when email already exists |
| **Preconditions** | User is on the Register page |
| **Steps** | 1. Enter valid First name, Last name 2. Enter an email that is already registered 3. Enter password and confirm password 4. Click Register |
| **Test Data** | Email: testing@gmail.com (already registered) |
| **Expected Result** | System should show an error and not create a duplicate account |
| **Actual Result** | System displayed "The specified email already exists" and did not register the account |
| **Status** | ✅ Pass |
| **Screenshot Evidence** | `/Screenshots/Observations/OBS-001.png`, `/Screenshots/Observations/OBS-002.png` |

---

## TC-007

| Field | Details |
|---|---|
| **Test Case ID** | TC-007 |
| **Module** | Register/Login |
| **Scenario ID** | TS-AUTH-01 |
| **Title** | Verify successful registration with valid, unique details |
| **Preconditions** | User is on the Register page |
| **Steps** | 1. Enter First name, Last name 2. Enter a new/unused email 3. Enter password and confirm password 4. Click Register |
| **Test Data** | Name: Mona Singh, Email: mona10august@gmail.com |
| **Expected Result** | Account should be created successfully and user should be auto logged in |
| **Actual Result** | "Your registration completed" message shown, user auto logged in (email shown at top) |
| **Status** | ✅ Pass |
| **Screenshot Evidence** | `/Screenshots/Observations/OBS-003.png`, `/Screenshots/Observations/OBS-004.png` |

---

## TC-008

| Field | Details |
|---|---|
| **Test Case ID** | TC-008 |
| **Module** | Register/Login |
| **Scenario ID** | TS-AUTH-04 |
| **Title** | Verify login fails with incorrect password |
| **Preconditions** | User has a registered account (mona10august@gmail.com) |
| **Steps** | 1. Go to Log in page 2. Enter registered email 3. Enter an incorrect password 4. Click Log in |
| **Test Data** | Email: mona10august@gmail.com, Password: (incorrect) |
| **Expected Result** | System should show an error and not log the user in |
| **Actual Result** | "Login was unsuccessful... The credentials provided are incorrect" error shown correctly |
| **Status** | ✅ Pass |
| **Screenshot Evidence** | `/Screenshots/Observations/OBS-005.png` |

---

## TC-009

| Field | Details |
|---|---|
| **Test Case ID** | TC-009 |
| **Module** | Register/Login |
| **Scenario ID** | TS-AUTH-03 |
| **Title** | Verify successful login with correct credentials |
| **Preconditions** | User has a registered account |
| **Steps** | 1. Log out if logged in 2. Go to Log in page 3. Enter correct email and correct password 4. Click Log in |
| **Test Data** | Email: mona10august@gmail.com, Password: (correct) |
| **Expected Result** | User should log in successfully and see their email at the top of the page |
| **Actual Result** | Successfully logged in, email shown at the top |
| **Status** | ✅ Pass |
| **Screenshot Evidence** | `/Screenshots/Observations/OBS-009.png` |

---

## TC-010

| Field | Details |
|---|---|
| **Test Case ID** | TC-010 |
| **Module** | Gift Cards |
| **Scenario ID** | N/A |
| **Title** | Verify Gift Card requires recipient details before it can be added to cart |
| **Preconditions** | User is on the "$5 Virtual Gift Card" product page |
| **Steps** | 1. Leave Recipient's Name and Recipient's Email empty 2. Click "Add to cart" |
| **Test Data** | Recipient Name: (empty), Recipient Email: (empty) |
| **Expected Result** | System should show a validation error and not add the gift card to cart until recipient details are filled |
| **Actual Result** | System displayed "Enter valid recipient name" and "Enter valid recipient email" and blocked the add-to-cart action |
| **Status** | ✅ Pass |
| **Remarks** | Expected validation behavior. Not a bug. |
| **Screenshot Evidence** | `/Screenshots/Observations/OBS-008.png` |

---

## TC-011

| Field | Details |
|---|---|
| **Test Case ID** | TC-011 |
| **Module** | Computers, Electronics |
| **Scenario ID** | N/A |
| **Title** | Verify "Add to Cart" button visibility across Computers and Electronics categories |
| **Preconditions** | User is browsing product categories |
| **Steps** | 1. Navigate to Computers → Desktops 2. Navigate to Electronics → Camera, photo 3. Navigate to Electronics → Cell phones 4. Observe each product card for "Add to Cart" button |
| **Test Data** | Categories: Desktops, Camera/Photo, Cell phones |
| **Expected Result** | "Add to Cart" button should be visible on every product, OR a clear stock-status message should be shown if unavailable |
| **Actual Result** | Missing "Add to Cart" button on: Desktop PC with CDRW, Elite Desktop PC, Simple Computer (Desktops); all 4 products in Camera/Photo; Used phone (Cell phones). No stock message shown for any of these |
| **Status** | ❌ Fail (linked to BUG-001) |
| **Screenshot Evidence** | `/Screenshots/Defects/BUG-001-2.png` (Desktops), `/Screenshots/Defects/BUG-001-3.png` (Camera/Photo), `/Screenshots/Observations/OBS-006.png` (Cell phones — partial), `/Screenshots/Observations/OBS-007.png` (Apparel & Shoes — for comparison, all buttons visible here) |

---

## TC-012

| Field | Details |
|---|---|
| **Test Case ID** | TC-012 |
| **Module** | Manufacturer / Navigation |
| **Scenario ID** | N/A |
| **Title** | Verify manufacturer page displays products or an appropriate message |
| **Preconditions** | User is on any page with the Manufacturers sidebar visible |
| **Steps** | 1. Click "Tricentis" under Manufacturers in the left sidebar 2. Observe the page content |
| **Test Data** | Manufacturer: Tricentis |
| **Expected Result** | Page should show all products from this manufacturer, or a message like "No products found for this manufacturer" |
| **Actual Result** | Page loads with only the "Tricentis" heading; no products and no explanatory message shown |
| **Status** | ❌ Fail (linked to BUG-002) |

---

## TC-013

| Field | Details |
|---|---|
| **Test Case ID** | TC-013 |
| **Module** | Checkout / Billing Address |
| **Scenario ID** | TS-CHK-03 |
| **Title** | Verify State/Province list is available for India during checkout |
| **Preconditions** | User has items in cart and reached the Billing Address step of checkout |
| **Steps** | 1. Select Country = India 2. Check the State/province dropdown options |
| **Test Data** | Country: India |
| **Expected Result** | State/province dropdown should list actual Indian states to choose from |
| **Actual Result** | Only "Other (Non US)" is shown; no real state list is available |
| **Status** | ❌ Fail (linked to BUG-004) |

---

## TC-014

| Field | Details |
|---|---|
| **Test Case ID** | TC-014 |
| **Module** | Checkout |
| **Scenario ID** | TS-CHK-02 |
| **Title** | Verify registered user checkout flow completes successfully with valid details |
| **Preconditions** | User is logged in and has items in cart |
| **Steps** | 1. Go to cart and click Checkout 2. Accept Terms of Service 3. Fill Billing Address with valid details 4. Continue through Shipping Address, Shipping Method, and Payment Method (Check/Money Order) 5. Confirm Order |
| **Test Data** | Payment Method: Check / Money Order |
| **Expected Result** | Order should be placed successfully, with the order total correctly reflecting item subtotal, shipping, tax, and any payment method fee |
| **Actual Result** | Order confirmed successfully. Total correctly increased from ₹1768.00 to ₹1773.00 due to a ₹5.00 "Payment Method additional fee" for Check/Money Order — calculation is accurate |
| **Status** | ✅ Pass |
| **Screenshot Evidence** | `/Screenshots/Observations/OBS-010.png` through `OBS-014.png` (Mini-cart, Terms of Service validation, Billing Address, Shipping Address, Order Confirmation) |

---

## TC-015

| Field | Details |
|---|---|
| **Test Case ID** | TC-015 |
| **Module** | Search |
| **Scenario ID** | TS-SRCH-01 |
| **Title** | Verify search returns relevant results for a valid keyword |
| **Preconditions** | User is on any page with access to the Search bar |
| **Steps** | 1. Enter a valid, existing category name in the search box (e.g., "Books") 2. Click Search 3. Repeat for "Computers", "Electronics", "Gift cards" |
| **Test Data** | Keywords: Books, Computers, Electronics, Gift cards |
| **Expected Result** | Search should return relevant products or categories matching each keyword |
| **Actual Result** | "No products were found that matched your criteria" shown for every keyword tested, even valid, existing category names |
| **Status** | ❌ Fail (linked to BUG-003) |

---

*New test cases will be added here as more modules are tested.*

**Status Legend:** ✅ Pass &nbsp;|&nbsp; ❌ Fail &nbsp;|&nbsp; ⏳ Not Executed &nbsp;|&nbsp; 🚫 Blocked
