# AdNab Automation Test

## Project Overview
AdNab Automation Test is a Python-based automation testing project designed to test the AdNab Shopify store. This project uses Selenium WebDriver for browser automation and Pytest as the testing framework to ensure robust and reliable test execution.

## Project Structure
```
AdNab_Automationtest/
├── pages/              # Page Object Models for different pages
├── tests/              # Test cases
├── utils/              # Utility functions and helpers
├── test_results/       # Test execution reports
├── config.json         # Configuration file with base URL and credentials
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/jibinjoy77398/AdNab_Automationtest.git
cd AdNab_Automationtest
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
Install all required dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Dependencies
The project uses the following Python packages:

| Package | Purpose |
|---------|---------|
| **selenium** | Browser automation and web testing |
| **pytest** | Test framework for writing and executing tests |
| **webdriver-manager** | Automatic management of WebDriver binaries |

## Configuration

### config.json
Update the `config.json` file with your test environment details:
```json
{
  "base_url": "https://your-store.myshopify.com",
  "password": "your-password"
}
```

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Run Tests with HTML Report
```bash
pytest --html=test_results/report.html
```

### Run Specific Test File
```bash
pytest tests/test_filename.py
```

### Run Tests with Specific Markers
```bash
pytest -m marker_name
```

## Project Features
- ✅ Page Object Model (POM) architecture for maintainability
- ✅ Automated browser testing using Selenium
- ✅ Pytest framework for comprehensive test management
- ✅ Automatic WebDriver management
- ✅ Configuration file support for environment variables
- ✅ Organized test results directory

## Best Practices
- Always use the virtual environment for development
- Keep page objects in the `pages/` directory
- Write tests in the `tests/` directory
- Place utility functions in the `utils/` directory
- Update `config.json` with appropriate test environment URLs and credentials

## Troubleshooting

### Issue: WebDriver not found
**Solution:** Ensure `webdriver-manager` is installed. Run:
```bash
pip install --upgrade webdriver-manager
```

### Issue: Tests not running
**Solution:** Verify pytest is installed:
```bash
pip install --upgrade pytest
```

### Issue: Connection timeout
**Solution:** Check your internet connection and verify the `base_url` in `config.json` is correct and accessible.

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please reach out to the project maintainer.