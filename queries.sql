-- Monthly churn rate by signup month cohort
WITH subs AS (
  SELECT user_id,
         DATE_TRUNC('month', signup_date) AS cohort_month,
         DATE_TRUNC('month', subscription_end) AS cancel_month
  FROM payments
  WHERE subscription_start IS NOT NULL
)
SELECT
  cohort_month,
  cancel_month,
  COUNT(DISTINCT user_id) AS churned_users
FROM subs
WHERE cancel_month IS NOT NULL
GROUP BY cohort_month, cancel_month
ORDER BY cohort_month, cancel_month;
