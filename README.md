
# 📌 Project Name

Automated UI testing using **Pytest + Playwright + GitHub Actions**

---

# 🚀 Setup Instructions

## 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

# 🧪 Run Tests Locally

### Run all tests

```bash
pytest -v
```

### Run tests with logs visible

```bash
pytest -v --log-cli-level=INFO
```

### Run tests with full console output

```bash
pytest -v -s
```

---

# 📊 Excel Data Test

The test `test_sync_message_from_excel`:

* Reads data from `fixtures/inputs.xlsx`
* Submits form for each row
* Updates:

  * `Status` (Pass/Fail)
  * `Message`
* Prints result table in console

---

# ⚙️ GitHub Actions (CI)

Unit tests automatically run on push to `main` branch.

Workflow file location:

```
.github/workflows/python-unit-tests.yml
```

---

# 📂 Project Structure

```
project/
│
├── pages/
├── fixtures/
│   ├── test_data.py
│   └── inputs.xlsx
├── tests/
│   └── test_send_message.py
├── requirements.txt
├── pytest.ini
└── .github/workflows/
```

---

# 🛠 Technologies Used

* Python 3.10+
* pytest
* playwright
* pandas
* GitHub Actions

---

# 🔍 View Logs in GitHub

1. Go to Repository
2. Click **Actions**
3. Open latest workflow run
4. Click **Run unit tests**
5. Expand logs

---

# ✅ Expected Output

* ✔️ 3 tests collected
* ✔️ All tests passed
* ✔️ DataFrame markdown printed in logs (if enabled)

