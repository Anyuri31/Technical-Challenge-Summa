-- query.sql
SELECT
    u.id AS user_id,
    u.name AS user_name,
    u.email,
    SUM(o.total_amount) AS total_spent
FROM
    Users u
JOIN
    Orders o
    ON u.id = o.user_id
WHERE
    o.status = 'completed'
    AND o.purchase_date >= CURRENT_DATE - INTERVAL 30 DAY
GROUP BY
    u.id, u.name, u.email
HAVING
    SUM(o.total_amount) > 500
ORDER BY
    total_spent DESC;
