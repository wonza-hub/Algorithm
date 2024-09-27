-- REST_INFO 
-- REST_ID, REST_NAME, FOOD_TYPE, VIEWS, FAVORITES, PARKING_LOT, ADDRESS, TEL은 식당 ID, 식당 이름, 음식 종류, 조회수, 즐겨찾기수, 주차장 유무, 주소, 전화번호
-- 
-- REST_REVIEW 
-- REVIEW_ID, REST_ID, MEMBER_ID, REVIEW_SCORE, REVIEW_TEXT,REVIEW_DATE는 각각 리뷰 ID, 식당 ID, 회원 ID, 점수, 리뷰 텍스트, 리뷰 작성일
-- 
-- 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회
--  서울에 위치
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림
-- 평균점수를 기준으로 내림차순 정렬/즐겨찾기수를 기준으로 내림차순 정렬

-- 코드를 입력하세요
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO A, REST_REVIEW B
WHERE A.REST_ID=B.REST_ID
AND A.ADDRESS LIKE '서울%'
GROUP BY A.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC