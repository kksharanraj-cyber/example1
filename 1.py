print("welcome to college")
print("ajay rapper")
name: Run Python Script
on: [push]
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: python 1.py
