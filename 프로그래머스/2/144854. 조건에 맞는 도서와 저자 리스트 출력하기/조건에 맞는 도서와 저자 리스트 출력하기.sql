-- 코드를 입력하세요
SELECT b.BOOK_ID, i.AUTHOR_NAME, TO_CHAR(b.PUBLISHED_DATE, 'YYYY-MM-DD')
FROM BOOK b 
INNER JOIN AUTHOR i ON b.AUTHOR_ID = i.AUTHOR_ID
WHERE b.CATEGORY = '경제'
ORDER BY b.PUBLISHED_DATE;