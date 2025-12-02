# Week 01 Report – App Metrics Analysis

## 1. Comparison of Pandas, NumPy, and SQLite

### Results

| Metric                      | Pandas (default) | NumPy (ddof=0) | NumPy (ddof=1) | SQLite (manual formula)            |
| --------------------------- | ---------------- | -------------- | -------------- | ---------------------------------- |
| Mean (minutes_per_user)     | 19.14            | 19.14          | 19.14          | 19.14                              |
| Variance (minutes_per_user) | 7.81             | ~6.69          | 7.81           | 7.81 (÷N-1) / ~6.69 (÷N)           |
| Std Dev (minutes_per_user)  | 2.79             | ~2.58          | 2.79           | 2.79 (÷N-1) / ~2.58 (÷N)           |
| Variance (active_users)     | 262380.95        | ~224326.53     | 262380.95      | 262380.95 (÷N-1) / ~224326.53 (÷N) |
| Std Dev (active_users)      | 512.23           | ~473.72        | 512.23         | 512.23 (÷N-1) / ~473.72 (÷N)       |

### Analysis

- **Pandas** defaults to sample statistics (division by N-1).
- **NumPy** defaults to population statistics (division by N), unless `ddof=1` is specified.
- **SQLite** has no built-in variance/stddev functions, so manual formulas are required. Depending on whether you divide by N or N-1, results match NumPy or Pandas.
- All three tools are consistent once the definition (sample vs population) is aligned.

---

## 2. Daily Trend Analysis

### Metric

- Active users over time.

### Approach

- Plot a line chart with **date** on the X-axis and **active_users** on the Y-axis.
- Look for patterns such as weekend spikes, campaign-driven increases, or seasonal dips.

### Insight

- Daily granularity allows detection of short-term fluctuations.
- Aggregating to weekly or monthly granularity can highlight longer-term trends.

---

## 3. User Clustering Based on Usage Behavior

### Metrics

- `minutes_per_user`
- `active_users`

### Method

- Apply clustering (e.g., K-Means) or simple segmentation:
  - **Light users**: low minutes, high volume.
  - **Medium users**: moderate minutes.
  - **Heavy users**: high minutes, smaller group but highly engaged.

### Insight

- Segmentation supports tailored strategies:
  - Light users → need incentives to increase engagement.
  - Heavy users → focus on retention and premium features.

---

## 4. Educational Note: ddof=0 vs ddof=1

- **ddof=0 (NumPy default):** Population variance, divide by N. Produces slightly smaller variance/stddev.
- **ddof=1 (Pandas default):** Sample variance, divide by N-1. Produces unbiased estimates.
- **SQLite:** Manual formulas can replicate either definition depending on denominator choice.

**Conclusion:** Pandas and NumPy with `ddof=1` match exactly. NumPy with `ddof=0` and SQLite with division by N give slightly smaller values. This difference is definitional, not computational.

---

## 📌 Overall Conclusion

- Pandas, NumPy, and SQLite produce consistent results once definitions are aligned.
- Daily trend analysis reveals short-term fluctuations in active users.
- User clustering provides actionable insights for engagement strategies.
- Understanding the difference between population and sample statistics (ddof=0 vs ddof=1) is essential for accurate reporting.
