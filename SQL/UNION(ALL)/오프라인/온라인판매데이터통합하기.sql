-- ONLINE_SALE 
-- ONLINE_SALE_ID, USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 각각 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일
-- 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재
-- OFFLINE_SALE
-- OFFLINE_SALE_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE는 각각 오프라인 상품 판매 ID, 상품 ID, 판매량, 판매일
-- 동일한 날짜, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재
-- 
-- 2022년 3월의 오프라인/온라인 상품 판매 데이터
-- 판매 날짜, 상품ID, 유저ID, 판매량을 출력
-- OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
--  판매일을 기준으로 오름차순 정렬/상품 ID를 기준으로 오름차순/유저 ID를 기준으로 오름차순 정렬

-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = '2022-03'
UNION ALL
SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = '2022-03'
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC;
