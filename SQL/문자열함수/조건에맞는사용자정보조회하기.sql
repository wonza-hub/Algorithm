-- USED_GOODS_BOARD 
--  BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS는 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수
-- USED_GOODS_USER
-- USER_ID, NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2, TLNO는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호
-- 
-- 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
-- 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력
-- 전화번호의 경우 xxx-xxxx-xxxx 같은 형태  하이픈 문자열(-)을 삽입하여 출력
-- 회원 ID를 기준으로 내림차순 정렬

-- 코드를 입력하세요
SELECT B.USER_ID,	B.NICKNAME, CONCAT(B.CITY, ' ', B.STREET_ADDRESS1, ' ', B.STREET_ADDRESS2) AS '전체주소',	CONCAT_WS('-', SUBSTR(TLNO,1,3), SUBSTR(TLNO,4,4), SUBSTR(TLNO,8,4)) AS '전화번호'
FROM USED_GOODS_BOARD A JOIN USED_GOODS_USER B ON A.WRITER_ID=B.USER_ID
GROUP BY A.WRITER_ID
HAVING COUNT(A.WRITER_ID) >= 3
ORDER BY B.USER_ID DESC