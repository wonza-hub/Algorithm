-- FIRST_HALF 
-- SHIPMENT_ID, FLAVOR, TOTAL_ORDER 는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량
-- 
-- ICECREAM_INFO 
-- FLAVOR, INGREDITENT_TYPE 은 각각 아이스크림 맛, 아이스크림의 성분 타입
-- 
-- 상반기 아이스크림 총주문량이 3,000보다 높으면서
-- 아이스크림의 주 성분이 과일인
-- 아이스크림의 맛
-- 총주문량이 큰 순서대로 조회

-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF A, ICECREAM_INFO B
WHERE A.FLAVOR=B.FLAVOR
AND A.TOTAL_ORDER>3000
AND B.INGREDIENT_TYPE='fruit_based'
ORDER BY A.TOTAL_ORDER DESC