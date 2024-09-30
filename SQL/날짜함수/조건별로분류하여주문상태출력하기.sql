-- FOOD_ORDER 
-- ORDER_ID, PRODUCT_ID, AMOUNT, PRODUCE_DATE, IN_DATE,OUT_DATE,FACTORY_ID, WAREHOUSE_ID는 각각 주문 ID, 제품 ID, 주문양, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID
-- 
-- 2022년 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회
-- 출고여부는 2022년 5월 1일까지 출고완료로, 이 후 날짜는 출고 대기로, 미정이면 출고미정으로 출력
-- 주문 ID를 기준으로 오름차순 정렬

-- 코드를 입력하세요
SELECT ORDER_ID,	PRODUCT_ID,	DATE_FORMAT(OUT_DATE, '%Y-%m-%d') OUT_DATE,	
CASE 
    WHEN DATEDIFF('2022-05-01', OUT_DATE) >= 0 THEN '출고완료'
    WHEN DATEDIFF('2022-05-01', OUT_DATE) < 0 THEN '출고대기'
    WHEN OUT_DATE IS NULL THEN '출고미정'
END '출고여부'
FROM FOOD_ORDER