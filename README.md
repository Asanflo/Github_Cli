# GitHub CLI

A simple Command-Line Interface (CLI) tool to fetch and display GitHub user information such as recent events. Built with Python, Click, and the GitHub public API.

---

## Features

- Display the latest public events of a GitHub user.

---

## Requirements

- Python 3.7 or higher
- Git
- `pip` (Python package manager)
- Python dependencies:
  - [Click](https://click.palletsprojects.com/)  
  - [Requests](https://requests.readthedocs.io/)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/github_cli.git
cd github_cli
```
2. (Optional) Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```
3. Install the package in editable mode:

```bash
pip install --editable .
```
This will make the github command available globally in your terminal.

---
## Usage
The CLI provides multiple commands under the main github command.

1. View Recent Events
```bash
github <username> --limit 10
```
username: GitHub username
--limit: Optional, number of events to display (default is 10)

```text
Last activities:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```
---
## Contributing
Contributions are welcome! You can add new commands, improve the formatting, or enhance API handling. Please follow these steps:

Fork the repository.

Create a new branch for your feature.

Submit a pull request with a clear description.