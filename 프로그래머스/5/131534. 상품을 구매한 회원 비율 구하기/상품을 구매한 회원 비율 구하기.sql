-- 코드를 입력하세요
# SELECT 
SELECT YEAR(T.SALES_DATE) AS YEAR, MONTH(T.SALES_DATE) AS MONTH, COUNT(DISTINCT T.USER_ID) AS PURCHASED_USERS, ROUND(COUNT(DISTINCT T.USER_ID)/(SELECT COUNT(*)
                                                                                                                                                FROM USER_INFO
                                                                                                                                                WHERE YEAR(JOINED) = 2021), 1) AS PUCHASED_RATION 
FROM (SELECT O.USER_ID, O.SALES_DATE
      FROM ONLINE_SALE AS O
      LEFT JOIN USER_INFO AS U ON O.USER_ID = U.USER_ID
      WHERE YEAR(U.JOINED) = 2021) AS T
GROUP BY YEAR(T.SALES_DATE), MONTH(T.SALES_DATE)
ORDER BY YEAR(T.SALES_DATE) ASC, MONTH(T.SALES_DATE) ASC


# SELECT COUNT(*)
# FROM USER_INFO
# WHERE YEAR(JOINED) = 2021