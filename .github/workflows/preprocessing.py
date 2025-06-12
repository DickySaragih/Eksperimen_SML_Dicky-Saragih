name: Preprocessing Workflow

on:
  push:
    paths:
      - preprocessing/automate_dicky_saragih.py
      - namadataset_raw/WineQT.csv

jobs:
  preprocessing:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install pandas numpy scikit-learn

      - name: Run preprocessing script
        run: |
          python preprocessing/automate_dicky_saragih.py

      - name: Commit processed file
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "actions@github.com"
          git add preprocessing/namadataset_preprocessing/WineQT_processed.csv
          git commit -m "Update processed dataset"
          git push
