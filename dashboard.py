import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "data" / "customers.csv")

st.set_page_config(page_title="Customer Churn Analytics", layout="wide")
st.title("Customer Churn & Retention Analytics")
st.caption("Portfolio project — Python • SQL • Pandas • Plotly • Streamlit")

with st.sidebar:
    st.header("Filters")
    contracts = st.multiselect(
        "Contract",
        sorted(df.contract.unique()),
        default=sorted(df.contract.unique())
    )
    services = st.multiselect(
        "Internet Service",
        sorted(df.internet_service.unique()),
        default=sorted(df.internet_service.unique())
    )

filtered = df[
    df.contract.isin(contracts) &
    df.internet_service.isin(services)
]

churn = filtered.churned.mean() if len(filtered) else 0
risk = filtered.estimated_annual_revenue_at_risk.sum()
customers = len(filtered)
avg = filtered.monthly_charge.mean() if len(filtered) else 0

a,b,c,d = st.columns(4)
a.metric("Customers", f"{customers:,}")
b.metric("Churn Rate", f"{churn:.1%}")
c.metric("Revenue at Risk", f"${risk:,.0f}")
d.metric("Avg Monthly Charge", f"${avg:,.2f}")

left, right = st.columns(2)

contract = filtered.groupby("contract", as_index=False).agg(
    churn_rate=("churned","mean")
)
contract["churn_pct"] = contract.churn_rate * 100
left.plotly_chart(
    px.bar(
        contract,
        x="contract",
        y="churn_pct",
        title="Churn Rate by Contract",
        labels={"churn_pct":"Churn Rate (%)"}
    ),
    use_container_width=True
)

tenure = filtered.copy()
tenure["tenure_band"] = pd.cut(
    tenure.tenure_months,
    [0,6,12,24,48,72],
    labels=["0-6","7-12","13-24","25-48","49-72"]
)
tenure = tenure.groupby("tenure_band", observed=False, as_index=False).churned.mean()
tenure["churn_pct"] = tenure.churned * 100
right.plotly_chart(
    px.line(
        tenure,
        x="tenure_band",
        y="churn_pct",
        markers=True,
        title="Churn Rate by Tenure",
        labels={"churn_pct":"Churn Rate (%)"}
    ),
    use_container_width=True
)

st.subheader("Highest Revenue-at-Risk Customers")
risk_table = filtered[filtered.churned.eq(1)].nlargest(
    15, "estimated_annual_revenue_at_risk"
)[[
    "customer_id","contract","tenure_months","monthly_charge",
    "satisfaction_score","estimated_annual_revenue_at_risk"
]]
st.dataframe(risk_table, use_container_width=True, hide_index=True)
