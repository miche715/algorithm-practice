-- https://school.programmers.co.kr/learn/courses/30/lessons/301646
-- 특정 형질을 가지는 대장균 찾기

SELECT
    COUNT(*)
FROM
    ECOLI_DATA
WHERE
    (SUBSTRING(REVERSE(CONVERT(CONV(GENOTYPE, 10, 2), CHAR)), 1, 1) = '1' OR SUBSTRING(REVERSE(CONVERT(CONV(GENOTYPE, 10, 2), CHAR)), 3, 3)) AND 
    SUBSTRING(REVERSE(CONVERT(CONV(GENOTYPE, 10, 2), CHAR)), 1, 1) != '1' OR 