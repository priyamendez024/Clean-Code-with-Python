# Chapter 17: Automation and CI/CD Pipelines

# GitHub Actions example snippet for testing
# ---
# name: Test
#
# on: [push, pull_request]
#
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - uses: actions/checkout@v3
#       - name: Setup Python
#         uses: actions/setup-python@v4
#         with:
#           python-version: 3.8
#       - name: Install dependencies
#         run: pip install -r requirements.txt
#       - name: Run tests
#         run: pytest
# ---