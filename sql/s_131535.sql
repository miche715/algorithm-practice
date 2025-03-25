-- https://school.programmers.co.kr/learn/courses/30/lessons/131535
-- 조건에 맞는 회원수 구하기

SELECT
    COUNT(*)
FROM
    USER_INFO
WHERE
    JOINED BETWEEN '2021-01-01' AND '2021-12-31' AND
    AGE BETWEEN 20 AND 29