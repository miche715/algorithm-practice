-- https://school.programmers.co.kr/learn/courses/30/lessons/144853
-- 조건에 맞는 도서 리스트 출력하기

SELECT
    BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM
    BOOK
WHERE
    PUBLISHED_DATE BETWEEN '2021-01-01' AND '2021-12-31' AND
    CATEGORY = '인문'
ORDER BY
    PUBLISHED_DATE ASC