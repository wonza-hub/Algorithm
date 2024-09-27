-- DOCTOR
-- DR_NAME, DR_ID, LCNS_NO, HIRE_YMD, MCDP_CD, TLNO는 각각 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 전화번호
-- 진료과가 흉부외과(CS)이거나 일반외과(GS)
-- 의사의 이름, 의사ID, 진료과, 고용일자를 조회
-- 고용일자를 기준으로 내림차순 정렬/고용일자가 같다면 이름을 기준으로 오름차순 정렬
-- 날짜 포맷은 예시와 동일하게 나와야합니다.

-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d')
FROM DOCTOR
WHERE MCDP_CD='CS' OR MCDP_CD='GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC