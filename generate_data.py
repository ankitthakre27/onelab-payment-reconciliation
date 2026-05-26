# generate_data.py

import pandas as pd

platform = pd.DataFrame([
    ["TXN1001", 100.00, "2026-05-28", "PAYMENT"],
    ["TXN1002", 250.50, "2026-05-29", "PAYMENT"],
    ["TXN1003", 75.25, "2026-05-31", "PAYMENT"],  # settles next month
    ["TXN1004", 33.335, "2026-05-30", "PAYMENT"],
    ["TXN1005", 33.335, "2026-05-30", "PAYMENT"],
    ["TXN1006", 33.335, "2026-05-30", "PAYMENT"],
])

platform.columns = ["txn_id", "amount", "txn_date", "type"]

bank = pd.DataFrame([
    ["SETT1", "TXN1001", 100.00, "2026-05-29"],
    ["SETT2", "TXN1002", 250.50, "2026-05-30"],
    ["SETT3", "TXN1003", 75.25, "2026-06-01"],  # delayed settlement
    ["SETT4", "TXN1004", 33.33, "2026-05-31"],
    ["SETT5", "TXN1005", 33.33, "2026-05-31"],
    ["SETT6", "TXN1005", 33.33, "2026-05-31"],  # duplicate
    ["SETT7", "REF999", -50.00, "2026-05-31"],  # orphan refund
])

bank.columns = ["settlement_id", "txn_id", "amount", "settlement_date"]

platform.to_csv("platform_transactions.csv", index=False)
bank.to_csv("bank_settlements.csv", index=False)

print("Mock data generated")