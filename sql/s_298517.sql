-- https://school.programmers.co.kr/learn/courses/30/lessons/298517
-- 가장 큰 물고기 10마리 구하기

SELECT
    ID, IFNULL(LENGTH, 10) AS LENGTH
FROM
    FISH_INFO
ORDER BY
    LENGTH DESC, 
    ID ASC
LIMIT 10