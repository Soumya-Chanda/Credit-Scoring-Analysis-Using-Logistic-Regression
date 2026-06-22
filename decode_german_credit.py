"""Decode UCI German Credit data (german.data) into a labeled CSV using german.doc mappings."""
import pandas as pd

COLUMNS = [
    "checking_account_status", "duration_months", "credit_history", "purpose",
    "credit_amount", "savings_account", "employment_since", "installment_rate_pct",
    "personal_status_sex", "other_debtors_guarantors", "present_residence_since",
    "property", "age_years", "other_installment_plans", "housing",
    "existing_credits_count", "job", "num_dependents", "telephone",
    "foreign_worker", "credit_risk",
]

MAPPINGS = {
    "checking_account_status": {
        "A11": "< 0 DM", "A12": "0-200 DM", "A13": ">= 200 DM", "A14": "no checking account",
    },
    "credit_history": {
        "A30": "no credits taken/all paid duly", "A31": "all credits at this bank paid duly",
        "A32": "existing credits paid duly till now", "A33": "delay in paying off in the past",
        "A34": "critical account/other credits existing",
    },
    "purpose": {
        "A40": "car (new)", "A41": "car (used)", "A42": "furniture/equipment",
        "A43": "radio/television", "A44": "domestic appliances", "A45": "repairs",
        "A46": "education", "A47": "vacation", "A48": "retraining", "A49": "business",
        "A410": "others",
    },
    "savings_account": {
        "A61": "< 100 DM", "A62": "100-500 DM", "A63": "500-1000 DM",
        "A64": ">= 1000 DM", "A65": "unknown/no savings account",
    },
    "employment_since": {
        "A71": "unemployed", "A72": "< 1 year", "A73": "1-4 years",
        "A74": "4-7 years", "A75": ">= 7 years",
    },
    "personal_status_sex": {
        "A91": "male: divorced/separated", "A92": "female: divorced/separated/married",
        "A93": "male: single", "A94": "male: married/widowed", "A95": "female: single",
    },
    "other_debtors_guarantors": {
        "A101": "none", "A102": "co-applicant", "A103": "guarantor",
    },
    "property": {
        "A121": "real estate", "A122": "building society savings/life insurance",
        "A123": "car or other", "A124": "unknown/no property",
    },
    "other_installment_plans": {
        "A141": "bank", "A142": "stores", "A143": "none",
    },
    "housing": {
        "A151": "rent", "A152": "own", "A153": "for free",
    },
    "job": {
        "A171": "unemployed/unskilled non-resident", "A172": "unskilled resident",
        "A173": "skilled employee/official",
        "A174": "management/self-employed/highly qualified",
    },
    "telephone": {
        "A191": "none", "A192": "yes, registered",
    },
    "foreign_worker": {
        "A201": "yes", "A202": "no",
    },
    "credit_risk": {
        1: "good", 2: "bad",
    },
}

df = pd.read_csv("german.data", sep=r"\s+", header=None, names=COLUMNS)

for col, mapping in MAPPINGS.items():
    df[col] = df[col].map(mapping)

df.to_csv("german_credit_labeled.csv", index=False)
print(f"Wrote german_credit_labeled.csv with {len(df)} rows and {len(df.columns)} columns")
print(df.head())
