-- https://school.programmers.co.kr/learn/courses/30/lessons/298516
-- 한 해에 잡은 물고기 수 구하기

SELECT
    COUNT(*) AS FISH_COUNT
FROM
    FISH_INFO
WHERE
    SUBSTR(TIME, 1, 4) = '2021'
    -- TIME BETWEEN '2021/01/01' AND '2021/12/31'