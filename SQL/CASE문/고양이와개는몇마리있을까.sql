-- ANIMAL_INS 
-- ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부
-- 
-- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회
-- 고양이를 개보다 먼저 조회

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY 
    CASE
        WHEN ANIMAL_TYPE='Cat' THEN 1
        WHEN ANIMAL_TYPE='Dog' THEN 2
        ELSE 3
    END