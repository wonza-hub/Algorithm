-- BOOK
-- BOOK_SALES
-- 
-- 2022년 1월의 카테고리 별 도서 판매량을 합산
-- 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력
-- 카테고리명을 기준으로 오름차순 정렬

-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK A, BOOK_SALES B
WHERE A.BOOK_ID=B.BOOK_ID
AND DATE_FORMAT(SALES_DATE, '%Y-%m')="2022-01"
GROUP BY CATEGORY
ORDER BY CATEGORY ASC