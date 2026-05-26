# reconcile.py

import pandas as pd

platform = pd.read_csv("data/platform_transactions.csv")
bank = pd.read_csv("data/bank_settlements.csv")

issues = []

# Duplicate detection
duplicates = bank[bank.duplicated(subset=["txn_id"], keep="first")]

for _, row in duplicates.iterrows():
    issues.append({
        "txn_id": row["txn_id"],
        "issue": "Duplicate Settlement"
    })

# Missing / delayed settlements
for _, row in platform.iterrows():

    match = bank[bank["txn_id"] == row["txn_id"]]

    if match.empty:
        issues.append({
            "txn_id": row["txn_id"],
            "issue": "Missing Settlement"
        })

    else:
        settlement_date = pd.to_datetime(
            match.iloc[0]["settlement_date"]
        )

        txn_date = pd.to_datetime(row["txn_date"])

        if settlement_date.month != txn_date.month:
            issues.append({
                "txn_id": row["txn_id"],
                "issue": "Delayed Settlement"
            })

# Orphan refund
refunds = bank[bank["amount"] < 0]

for _, row in refunds.iterrows():

    original = platform[
        platform["txn_id"] == row["txn_id"]
    ]

    if original.empty:
        issues.append({
            "txn_id": row["txn_id"],
            "issue": "Orphan Refund"
        })

report = pd.DataFrame(issues)

print(report)

report.to_csv("data/reconciliation_report.csv", index=False)