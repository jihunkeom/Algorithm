-- 코드를 입력하세요
SELECT COUNT(*)
FROM USER_INFO
WHERE (JOINED BETWEEN TO_DATE('2021-01-01', 'YYYY-MM-DD') AND TO_DATE('2021-12-31', 'YYYY-MM-DD')) AND (AGE BETWEEN 20 AND 29)