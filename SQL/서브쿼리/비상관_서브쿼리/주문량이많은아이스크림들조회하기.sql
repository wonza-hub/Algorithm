-- FIRST_HALF 
-- SHIPMENT_ID, FLAVOR, TOTAL_ORDER는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량
-- JULY 
--  SHIPMENT_ID, FLAVOR, TOTAL_ORDER 은 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 7월 아이스크림 총주문량
-- 
-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회

-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF A JOIN
(
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
) B
ON A.FLAVOR=B.FLAVOR
ORDER BY A.TOTAL_ORDER + B.TOTAL_ORDER DESC
LIMIT 3;