-- FOOD_PRODUCT 
-- PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE는 식품 ID, 식품 이름, 식품코드, 식품분류, 식품 가격
-- 
-- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 식품 가격을 기준으로 내림차순 정렬

-- 코드를 입력하세요
SELECT A.CATEGORY,	B.MAX_PRICE, A.PRODUCT_NAME
FROM FOOD_PRODUCT A INNER JOIN
(
    SELECT CATEGORY,MAX(PRICE) AS MAX_PRICE
    FROM FOOD_PRODUCT 
    GROUP BY CATEGORY
) B
ON A.CATEGORY=B.CATEGORY AND A.PRICE=B.MAX_PRICE
WHERE A.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY A.PRICE DESC 