# 🧪 Selenium Python Automation Framework

A clean, scalable **Selenium + PyTest** automation framework built to test **[https://the-internet.herokuapp.com](https://the-internet.herokuapp.com)**.
This project follows the **Page Object Model (POM)** design pattern and is fully integrated with **GitHub Actions** and **Jenkins CI**.

---

## ✨ Key Highlights

* 🔹 Python + Selenium WebDriver
* 🔹 PyTest test runner
* 🔹 Page Object Model (POM)
* 🔹 Headless execution for CI
* 🔹 GitHub Actions CI pipeline
* 🔹 Jenkins pipeline support
* 🔹 Allure-ready screenshot capture on failures
* 🔹 Cross-platform (Windows / macOS / Linux)

---

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions pipeline
│
├── base_pages/                    # Page Object classes
│   ├── base_class.py
│   ├── Home_Page.py
│   ├── login_admin_page.py
│   ├── geo_location_page.py
│   ├── checkboxes_page.py
│   └── ...
│
├── configuration/
│   └── logger_config.py           # Centralised logging
│
├── module/
│   └── open_a_page.py              # Page navigation helper
│
├── test_cases/                    # Test classes
│   ├── base_test_class.py
│   ├── test_home_page.py
│   ├── test_login_page.py
│   ├── test_geo_location_page.py
│   ├── test_checkboxes_page.py
│   └── ...
│
├── screenshots/                   # Failure screenshots
├── reports/                       # Test reports (optional)
├── logs/                          # Execution logs
│
├── conftest.py                    # PyTest hooks & screenshots
├── requirements.txt               # Python dependencies
├── Jenkinsfile                    # Jenkins pipeline
├── README.md
└── .gitignore
```

---

## 🧱 Framework Design

### Page Object Model (POM)

* Each web page has its **own class**
* Locators and actions are encapsulated
* Tests stay **clean and readable**

Example:

* `Home_Page` → Home page actions
* `Login_Admin_Page` → Login page actions
* `Geo_Location_Page` → Geolocation page actions

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Joshi-Tech/TheInternetPythonSelenium
cd TheInternetPythonSelenium
```

---

### 2️⃣ Create & Activate Virtual Environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests Locally

### Run all tests

```bash
pytest -q
```

### Run with verbose output

```bash
pytest -v
```

---

## 🖥️ Headless Execution

Headless mode is automatically enabled in CI.

To run headless locally:

```bash
export HEADLESS=true
pytest
```

(Windows PowerShell)

```powershell
$env:HEADLESS="true"
pytest
```

---

## 🧪 CI with GitHub Actions

GitHub Actions runs automatically on:

* `push` to `main`
* `pull_request` to `main`

### CI Features

* Ubuntu runner
* Python 3.13
* Headless Chrome
* Automatic test execution

Pipeline file:

```
.github/workflows/ci.yml
```

---

## 🧩 Jenkins Integration

A complete **Jenkinsfile** is provided.

### Jenkins Pipeline Stages

1. Checkout code
2. Create virtual environment
3. Install dependencies
4. Run PyTest
5. Publish JUnit results

Test results are stored as:

```
test-results/junit.xml
```

---

## 📸 Screenshots on Failure

* Screenshots are automatically captured on test failure
* Stored under:

```
/screenshots
```

Handled via `pytest_runtest_makereport` hook in `conftest.py`

Allure attachment support is already wired.

---

## 📝 Logging

* Centralised logger configuration
* Logs include:

  * Page actions
  * Clicks
  * Assertions

Logs are stored under:

```
/logs
```

---

## 🔐 Test Coverage

Currently automated:

* ✅ Home Page validation
* ✅ Login functionality
* ✅ Checkbox interactions
* ✅ Geo-location feature
* ✅ Secure area validation

---

## 📌 Best Practices Used

* ✔️ Page Object Model
* ✔️ Single Responsibility Principle
* ✔️ Headless CI execution
* ✔️ Screenshot on failure
* ✔️ CI-ready architecture
* ✔️ Clean folder structure

---

## 🛠️ Tech Stack

* **Language**: Python 3.13
* **Automation**: Selenium WebDriver
* **Test Runner**: PyTest
* **CI/CD**: GitHub Actions, Jenkins
* **Reporting**: PyTest + JUnit XML

---

## 🙌 Author

**Lakshmi Kant Joshi**
Quality Engineer | Test Automation Enthusiast

---

## ⭐ Final Note

This framework is designed to be **learning-friendly**, **CI-ready**, and **easily extensible**.
Perfect for demonstrating real-world Selenium automation best practices.

Happy Testing 🚀
