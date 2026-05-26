
import streamlit as st
import pandas as pd

report = pd.read_csv("data/reconciliation_report.csv")

platform = pd.read_csv("data/platform_transactions.csv")

total_transactions = len(platform)
total_issues = len(report)
matched = total_transactions - total_issues

st.metric("Total Transactions", total_transactions)
st.metric("Matched Transactions", matched)
st.metric("Total Issues", total_issues)

st.title("Payment Reconciliation Dashboard")

st.metric("Total Issues", len(report))

st.dataframe(report)

issue_counts = report["issue"].value_counts()

st.subheader("Issue Distribution")

st.bar_chart(issue_counts)

accuracy = (matched / total_transactions) * 100

st.metric(
    "Reconciliation Accuracy",
    f"{accuracy:.2f}%"
)