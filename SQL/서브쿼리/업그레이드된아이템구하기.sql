-- 'ITEM_A'->'ITEM_B'와 같이 업그레이드가 가능할 때 'ITEM_A'를 'ITEM_B' 의 PARENT 아이템,
-- PARENT 아이템이 없는 아이템을 ROOT 아이템
-- 
-- ITEM_INFO 
-- ITEM_ID, ITEM_NAME, RARITY, PRICE는 각각 아이템 ID, 아이템 명, 아이템의 희귀도, 아이템의 가격
-- 
-- ITEM_TREE 
-- ITEM_ID, PARENT_ITEM_ID는 각각 아이템 ID, PARENT 아이템의 ID
-- 
--  아이템들은 오직 하나의 PARENT 아이템 ID를 가지며, ROOT 아이템의 PARENT 아이템 ID는 NULL
-- ROOT 아이템이 없는 경우는 존재하지 않습니다.
-- 
-- 아이템의 희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템의
-- 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)를 출력
-- 아이템 ID를 기준으로 내림차순 정렬

-- 코드를 작성해주세요
SELECT A.ITEM_ID,	A.ITEM_NAME,	A.RARITY
FROM ITEM_INFO A, ITEM_TREE B
WHERE A.ITEM_ID = B.ITEM_ID
AND B.PARENT_ITEM_ID IN
(
    SELECT ITEM_ID
    FROM ITEM_INFO 
    WHERE RARITY = 'RARE'
)
ORDER BY A.ITEM_ID DESC;