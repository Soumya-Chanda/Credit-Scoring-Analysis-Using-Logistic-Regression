# Credit Risk Prediction using Logistic Regression

## Overview

Credit risk assessment is one of the most important problems in banking and financial services. Financial institutions must determine whether a loan applicant is likely to repay their obligations or default, balancing profitability against risk exposure.

This project develops an interpretable credit risk prediction framework using the Statlog (German Credit Data) dataset from the UCI Machine Learning Repository. The study combines exploratory data analysis, statistical hypothesis testing, logistic regression modeling, model selection, and cost-sensitive classification to identify the key determinants of creditworthiness and predict borrower risk. The primary focus is not only predictive performance but also model interpretability, allowing credit decisions to be explained through statistically significant risk factors.

---

## Objectives

The main objectives of this project are:

* Analyze demographic and financial characteristics associated with credit risk.
* Identify statistically significant predictors of borrower default.
* Develop interpretable logistic regression models for credit risk classification.
* Compare full and reduced models using formal statistical testing.
* Evaluate predictive performance using multiple classification metrics.
* Incorporate asymmetric lending costs into decision-making through threshold optimization.

---

## Dataset

### Source

Statlog (German Credit Data)

### Repository

UCI Machine Learning Repository

### Dataset Characteristics

* 1,000 loan applicants
* 20 predictor variables
* 7 numerical features
* 13 categorical features
* Binary target variable:

  * Good Credit Risk
  * Bad Credit Risk

### Examples of Features

* Checking Account Status
* Credit History
* Loan Duration
* Credit Amount
* Savings Account Status
* Employment Duration
* Housing Status
* Age
* Existing Credit Accounts
* Number of Dependents

The dataset contains approximately 70% good-risk applicants and 30% bad-risk applicants, creating a moderately imbalanced classification problem.

---

## Project Workflow

```text
Credit Data Collection
          │
          ▼
Data Cleaning & Validation
          │
          ▼
Exploratory Data Analysis
          │
          ▼
Statistical Hypothesis Testing
          │
          ▼
Feature Engineering
          │
          ▼
Logistic Regression Modeling
          │
          ▼
Backward Elimination
          │
          ▼
Model Evaluation
          │
          ▼
Threshold Optimization
          │
          ▼
Business Interpretation
```

---

## Exploratory Data Analysis

A comprehensive EDA was performed before model development.

### Data Quality Assessment

* Missing Value Analysis
* Duplicate Record Detection
* Category Consistency Checks

### Numerical Feature Analysis

Studied:

* Distribution Shapes
* Summary Statistics
* Skewness
* Kurtosis
* Outlier Detection

### Categorical Feature Analysis

Examined relationships between:

* Credit History
* Savings Account Status
* Employment Duration
* Housing Status
* Checking Account Status

and borrower risk outcomes.

### Correlation Analysis

Constructed correlation heatmaps and multicollinearity diagnostics to understand relationships among predictors.

---

## Statistical Inference

To formally identify variables associated with credit risk, multiple hypothesis tests were conducted.

### Chi-Square Test of Independence

Used for categorical predictors:

* Credit History
* Checking Account Status
* Savings Account
* Employment Status
* Housing

### Mann–Whitney U Test

Used for numerical variables due to non-normal distributions:

* Credit Amount
* Loan Duration
* Age
* Installment Rate

Key findings indicated that loan duration, credit amount, credit history, checking account status, and savings account characteristics were strongly associated with borrower risk.

---

## Logistic Regression Modeling

### Why Logistic Regression?

Logistic Regression was selected because:

* It produces interpretable probability estimates.
* Coefficients can be interpreted through odds ratios.
* Statistical significance of predictors can be directly evaluated.
* It is widely used in credit scoring and risk modeling.

The model estimates the probability that a borrower belongs to the bad-credit-risk category.

---

## Data Preparation

### Target Encoding

* Good Risk = 0
* Bad Risk = 1

### Feature Engineering

* One-Hot Encoding for categorical variables
* Numerical Feature Standardization
* Train-Test Split (80/20)
* Stratified Sampling

The final design matrix contained 48 predictors after encoding.

---

## Full Logistic Regression Model

A full logistic regression model containing all encoded variables was estimated using Maximum Likelihood Estimation.

### Model Statistics

* 48 Predictors
* Log-Likelihood = -356.53
* McFadden Pseudo R² = 0.270

Several variables emerged as significant predictors of borrower risk, including:

* Checking Account Status
* Credit History
* Credit Amount
* Loan Duration
* Housing Status
* Savings Account Status

These variables demonstrated strong predictive power after controlling for all other features.

---

## Feature Selection: Backward Elimination

To improve interpretability and reduce model complexity, backward elimination was performed.

### Procedure

1. Fit Full Model
2. Remove Least Significant Variable
3. Refit Model
4. Repeat Until All Remaining Predictors Are Significant

### Results

* Initial Predictors: 48
* Final Predictors: 17
* Variables Removed: 31

The resulting reduced model maintained strong predictive performance while substantially improving interpretability.

---

## Model Comparison

The Full and Reduced models were compared using:

### Likelihood Ratio Test

Used to determine whether removed variables contributed meaningful predictive information.

### Information Criteria

* AIC
* BIC

Results indicated that the reduced model was statistically comparable to the full model while being substantially simpler.

---

## Model Evaluation

Performance was assessed on an unseen test dataset.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

### Test Performance

| Metric    | Full Model | Reduced Model |
| --------- | ---------- | ------------- |
| Accuracy  | 0.780      | 0.760         |
| Precision | 0.643      | 0.630         |
| Recall    | 0.600      | 0.483         |
| F1 Score  | 0.621      | 0.547         |
| ROC-AUC   | 0.799      | 0.787         |

The reduced model achieved performance close to the full model while requiring significantly fewer predictors.

---

## Cost-Sensitive Classification

Traditional classification thresholds assume equal costs for all prediction errors.

In lending applications, however:

* Approving a risky borrower can be far more expensive than rejecting a safe borrower.

The German Credit dataset provides an asymmetric cost matrix where false negatives are substantially more costly than false positives.

### Threshold Optimization

Rather than using the default threshold of 0.50, optimal thresholds were selected by minimizing expected classification cost.

Results showed:

* Reduced Model Optimal Threshold ≈ 0.26
* Full Model Optimal Threshold ≈ 0.33

This significantly improved practical decision-making performance for lending applications.

---

## Key Findings

* Credit history is one of the strongest predictors of future credit risk.
* Loan duration and credit amount increase the likelihood of default.
* Savings and checking account characteristics provide substantial predictive information.
* Housing status significantly influences borrower risk.
* A reduced model with only 17 predictors performs nearly as well as the full 48-variable model.
* Cost-sensitive threshold optimization substantially improves lending decisions.

---

## Technologies Used

### Programming Language

* Python

### Libraries

```python
pandas
numpy
scipy
statsmodels
scikit-learn
matplotlib
seaborn
```

---

## Skills Demonstrated

* Credit Risk Modeling
* Logistic Regression
* Statistical Inference
* Maximum Likelihood Estimation
* Hypothesis Testing
* Feature Selection
* Cost-Sensitive Classification
* Explainable Machine Learning
* Predictive Analytics
* Financial Risk Analysis

---

## Applications

This framework can be applied to:

* Credit Scoring Systems
* Loan Approval Models
* Banking Risk Analytics
* Consumer Finance
* Default Prediction
* Explainable AI in Finance
* Model Risk Management

---

## Future Enhancements

Potential improvements include:

* Random Forest and Gradient Boosting Models
* XGBoost-Based Credit Scoring
* Cross-Validation-Based Model Selection
* Probability Calibration
* SHAP Explainability Analysis
* Ensemble Credit Risk Models
* Basel-Compliant Risk Modeling Frameworks

---

## Conclusion

This project demonstrates how statistical modeling and interpretable machine learning can be applied to credit risk assessment. Through exploratory analysis, hypothesis testing, logistic regression, feature selection, and cost-sensitive optimization, the study identifies the primary drivers of borrower risk while maintaining transparency and interpretability. The resulting framework provides a practical foundation for credit scoring and financial risk management applications.
