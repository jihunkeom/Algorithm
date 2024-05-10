-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, SUM(b.PRICE)
FROM USED_GOODS_USER a
INNER JOIN USED_GOODS_BOARD b on a.USER_ID = b.WRITER_ID
WHERE b.STATUS = 'DONE'
GROUP BY USER_ID, NICKNAME
HAVING SUM(b.PRICE) >= 700000
ORDER BY SUM(b.PRICE);