-- USED_GOODS_BOARD 
-- BOARD_ID, WRITER_ID, TITLE, CONTENTS, PRICE, CREATED_DATE, STATUS, VIEWS은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수
-- USED_GOODS_REPLY 
-- REPLY_ID, BOARD_ID, WRITER_ID, CONTENTS, CREATED_DATE 는 각각 댓글 ID, 게시글 ID, 작성자 ID, 댓글 내용, 작성일
-- 
-- 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
-- 2022년 10월에 작성된 게시글 @@@게시글인지 댓글인지 잘 봐야 함
-- 댓글 작성일을 기준으로 오름차순/게시글 제목을 기준으로 오름차순
-- 
-- CREATED_DATE의 포맷이 예시의 포맷과 일치

-- 코드를 입력하세요
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD A, USED_GOODS_REPLY B
WHERE A.BOARD_ID=B.BOARD_ID
AND DATE_FORMAT(A.CREATED_DATE, "%Y-%m") = "2022-10"
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC;