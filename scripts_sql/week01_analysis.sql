SELECT AVG(minutes_per_user) AS avg_minutes
FROM app_metrics;


SELECT
    SUM((minutes_per_user - (SELECT AVG(minutes_per_user)
    FROM app_metrics)) * 
      (minutes_per_user - (SELECT AVG(minutes_per_user)
    FROM app_metrics))) 
  / (COUNT(*) - 1) AS var_minutes
FROM app_metrics;


SELECT
    SQRT(
    SUM((minutes_per_user - (SELECT AVG(minutes_per_user)
    FROM app_metrics)) * 
        (minutes_per_user - (SELECT AVG(minutes_per_user)
    FROM app_metrics))) 
    / (COUNT(*) - 1)
  ) AS std_minutes
FROM app_metrics;