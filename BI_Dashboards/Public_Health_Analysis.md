# Public Health Trend Analysis

**Goal**: Track the spread of an infectious disease over time and correlate it with vaccination rates to inform public policy.

## 📂 Dataset
- `Datasets/public_health_trends.csv`

## 📊 Analysis Steps (Excel / Power BI)
1.  **Trend Line**: Plot `NewCases` over time (`WeekEnding`).
    - *Insight*: Identify seasonal peaks (Winter months).
2.  **Correlation**: Compare `VaccinationRate` vs `Hospitalizations`.
    - *Insight*: As Vaccination Rate increases > 60%, Hospitalizations should show a declining trend regardless of Case counts.
3.  **Recovery Rate**: Calculate `Recoveries / (Recoveries + Deaths)` (Proxy using Hospitalizations if death data missing).

## 🖼 Visuals
- **Area Chart**: New Cases vs. Hospitalizations.
- **Dual Axis Chart**: Vaccination Rate (Line) vs. New Cases (Bar).

*(This project demonstrates ability to handle Time Series data and sensitive public sector metrics.)*
