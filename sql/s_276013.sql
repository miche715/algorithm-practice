-- https://school.programmers.co.kr/learn/courses/30/lessons/276013
-- Python 개발자 찾기

SELECT
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM
    DEVELOPER_INFOS
WHERE
    'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY
    ID ASC