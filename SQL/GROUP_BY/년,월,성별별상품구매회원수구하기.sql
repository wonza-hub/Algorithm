-- USER_INFO 
-- USER_ID, GENDER, AGE, JOINED는 각각 회원 ID, 성별, 나이, 가입일
-- GENDER 컬럼은 비어있거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우는 여자
-- ONLINE_SALE
-- ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 각각 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일
-- 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재
-- 
-- 년, 월, 성별 별로 상품을 구매한 회원수를 집계
-- 년, 월, 성별을 기준으로 오름차순 정렬
-- 이때, 성별 정보가 없는 경우 결과에서 제외

-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) MONTH, A.GENDER, COUNT(DISTINCT A.USER_ID) AS USERS
FROM USER_INFO A JOIN ONLINE_SALE B ON A.USER_ID=B.USER_ID
WHERE A.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER
