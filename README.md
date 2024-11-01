#CI/CD assignment

![Build Status](https://github.com/Shashank-RC/CI-CD-397/blob/main/.github/workflows/main.yml/badge.svg?event=push)

Project Overview
This project is a Python package for sorting integer lists, developed using DevOps best practices. It includes implementations of Bubble Sort, Quick Sort, and Insertion Sort algorithms and leverages Continuous Integration (CI) to ensure code quality and correctness across different environments.

The repository has a fully automated CI/CD pipeline that performs:

Linting with black and flake8
Automated testing using pytest
Cross-platform support for Linux, macOS, and Windows, and compatibility with Python versions 3.9 and 3.10
Features
Sorting Algorithms: Efficient and well-documented implementations of common sorting algorithms:
Bubble Sort
Quick Sort
Insertion Sort
Automated Quality Checks:
Code linting with black and flake8
Unit tests to verify sorting functionality
Cross-platform Compatibility: Tested on Ubuntu, macOS, and Windows.
CI/CD Workflow
The CI/CD pipeline is implemented with GitHub Actions and consists of three main jobs:

Linting: Checks code style using black and flake8.
Testing: Runs unit tests with pytest across multiple OS (Linux, macOS, Windows) and Python versions (3.9, 3.10).
Packaging: Builds the package and uploads the build artifacts to GitHub.
Workflow Configuration
The workflow file is located in .github/workflows/main.yml. Here’s a breakdown of each job:

Linting: Ensures code follows consistent style guidelines.
Testing: Tests each sorting function on multiple OS and Python versions to guarantee compatibility and correctness.
Packaging: Builds the package on successful test completion and verifies the dist directory for output.
Usage:

Clone the repository:
bash

git clone https://github.com/Shashank-RC/CI-CD-397.git
cd REPOSITORY
Install dependencies:
bash
Copy code
pip install -r requirements-dev.txt
Run the sorting functions:
Example:
python

from sort_lib import bubble, quick, insertion
sorted_list = bubble([3, 1, 4, 1, 5])
Development Workflow
Pre-Commit Hooks
This project uses pre-commit hooks for linting and security checks:

File size checks to prevent large files from being added.
Linting with black and flake8.
Security checks to detect private keys or credentials.
Install pre-commit hooks:

bash

pre-commit install
Running Tests Locally
Run pytest to execute tests:

bash

pytest

Individual Project for me to get more understanding of CI/CD pipeline beyond assignment
Reflection on CI/CD
Using a CI/CD workflow enhanced the reliability of the codebase by:

Ensuring code quality through automated linting.
Running cross-platform tests to verify compatibility.
Automating builds to produce and verify package artifacts.
This DevOps approach, especially with tools like GitHub Actions and pre-commit hooks, streamlined collaboration and provided immediate feedback, ensuring high-quality software development.