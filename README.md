# AI-Assisted Payment Reconciliation Engine

## Problem Statement
Built a reconciliation system to compare platform transactions with bank settlements and identify discrepancies.

## Features
- Delayed settlement detection
- Duplicate settlement detection
- Missing settlement detection
- Orphan refund detection
- Dashboard visualization

## Assumptions
- Settlements may occur 1-2 days later
- Transaction IDs should be unique
- Refunds require valid source transactions

## Tech Stack
- Python
- Pandas
- Streamlit

## How to Run

pip install -r requirements.txt

python generate_data.py

python reconcile.py

streamlit run app.py

## Production Limitations
1. No handling for partial settlements
2. Assumes transaction IDs are reliable
3. Batch-oriented reconciliation only
