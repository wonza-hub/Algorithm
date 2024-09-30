-- USED_GOODS_BOARD 
-- BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수
-- USED_GOODS_FILE 
-- FILE_ID, FILE_EXT, FILE_NAME, BOARD_ID는 각각 파일 ID, 파일 확장자, 파일 이름, 게시글 ID
-- 
-- 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
-- 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬
-- 기본적인 파일경로는 /home/grep/src/ 이며, 게시글 ID를 기준으로 디렉토리가 구분되고, 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성
-- 
-- 조회수가 가장 높은 게시물은 하나만 존재

-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID =
(
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD 
    ORDER BY VIEWS DESC 
    LIMIT 1
)
ORDER BY FILE_ID DESC