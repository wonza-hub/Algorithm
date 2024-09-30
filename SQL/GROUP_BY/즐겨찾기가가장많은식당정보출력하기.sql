-- REST_INFO 
-- REST_ID, REST_NAME, FOOD_TYPE, VIEWS, FAVORITES, PARKING_LOT, ADDRESS, TEL은 식당 ID, 식당 이름, 음식 종류, 조회수, 즐겨찾기수, 주차장 유무, 주소, 전화번호
-- 
-- 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회
-- 음식 종류를 기준으로 내림차순 정렬

-- 코드를 입력하세요
SELECT FOOD_TYPE,	REST_ID,	REST_NAME,	FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES)
IN
(
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC