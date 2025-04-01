-- https://school.programmers.co.kr/learn/courses/30/lessons/133025
-- 과일로 만든 아이스크림 고르기

SELECT
    T1.FLAVOR
FROM
    FIRST_HALF T1
LEFT JOIN
    ICECREAM_INFO J1
ON
    T1.FLAVOR = J1.FLAVOR
WHERE
    T1.TOTAL_ORDER > 3000 AND
    J1.INGREDIENT_TYPE = 'fruit_based'
ORDER BY
    T1.TOTAL_ORDER DESC