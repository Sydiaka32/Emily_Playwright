# 🎯 Emily Playwright UI Testing Framework

This project is a robust **UI test automation framework** built with [**Playwright**](https://playwright.dev/python/), [**Pytest**](https://docs.pytest.org/), and enhanced with [**Allure**](https://docs.qameta.io/allure/) for detailed test reporting. It is designed to test end-to-end user flows in web applications across Chromium, Firefox, and WebKit browsers.

The framework supports:
- Cross-browser automation
- Test tagging and filtering
- Readable reporting via Allure
- Parametrization and modular page object pattern

# 🛠 Tech Stack

| Tool                    | Description |
|-------------------------|-------------|
| `allure-pytest`        | Allure reporting with Pytest for better reporting |
| `playwright`           | Python library to automate Chromium, WebKit, and Firefox through a single API. |
| `pytest`              | Popular testing framework for Python |
| `pytest-playwright`   | Pytest plugin for Playwright integration for browser automation testing |
| `requests`           | Versatile library for making HTTP requests in Python |

# ⚙️ Setup Instructions

## Clone the Project
```sh
git clone https://github.com/Sydiaka32/Emily_Playwright.git
cd <your-project-folder>
```

## Create and Activate a Virtual Environment
### Windows:
```sh
py -m pip install --user virtualenv
py -m venv env
.env\Scripts\activate
```

### Mac/Linux:
```sh
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies
```sh
pip install -r requirements.txt
```

## Install Playwright Browsers
```sh
playwright install
```

# 🏃‍♂️ Running Tests

Run all tests:
```sh
pytest
```

Run tests with specific tags:
```sh
pytest -m <tag_name>
```

Run tests with Allure reports:
```sh
pytest --alluredir=reports/allure-results
```

Generate and view Allure report:
```sh
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

To remove previous Allure results:
```sh
Remove-Item -Path "reports/allure-results/*" -Recurse -Force
```

# 📊 Viewing Test Results

### Install Allure Commandline Tool
#### Windows:
1. Install [Scoop](https://scoop.sh/)
2. Run:
   ```sh
   scoop install allure
   ```

#### Mac:
```sh
brew install allure
```

### View Results Locally:
```sh
allure serve allure-results
```

### View Results Online:
You can set up GitHub Pages or another hosting service to share reports online.

# ℹ️ Additional Help

View available Pytest options:
```sh
pytest --help
```

