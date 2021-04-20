-- --------------- all record select ----------
SELECT *
from ANIMAL_INS
order by ANIMAL_ID asc

-- ------------ reverse sort ---------------
SELECT NAME, DATETIME
from ANIMAL_INS
order by ANIMAL_ID desc

-- ------------ sick animal find --------------
SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where INTAKE_CONDITION = 'Sick'
order by ANIMAL_ID asc

-- -------------- young animal find --------------
SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where INTAKE_CONDITION != 'Aged'
order by ANIMAL_ID asc

-- ---------------- find animal id and name ----------------
SELECT ANIMAL_ID, NAME
from ANIMAL_INS
order by ANIMAL_ID asc

-- ------------- sort using conditions ---------------
SELECT ANIMAL_ID, NAME, DATETIME
from ANIMAL_INS
order by NAME, DATETIME desc

-- ----------- top record limit n --------------------
SELECT NAME
from ANIMAL_INS
order by DATETIME asc limit 1

-- ---------- get max value ---------------------
SELECT max(DATETIME) as 시간
from ANIMAL_INS

-- ---------- get min value ---------------------
SELECT min(DATETIME) as 시간
from ANIMAL_INS

-- ---------- get animal count ---------------
SELECT count(ANIMAL_ID) as count
from ANIMAL_INS

-- ------------ double exception --------------
SELECT count (distinct NAME) as count
from ANIMAL_INS
where NAME != 'NULL'

-- ------------ find animal id missing name -----------
SELECT ANIMAL_ID
from ANIMAL_INS
where NAME is null

-- ------------ find animal id having name -------------
SELECT ANIMAL_ID
from ANIMAL_INS 
where NAME is not null
order by ANIMAL_ID

-- ----------- null handling ------------
SELECT 
    ANIMAL_TYPE, 
    case 
        when NAME is NULL then "No name" 
        else NAME
    
    end as name,
    SEX_UPON_INTAKE
from ANIMAL_INS

-- ------------ how many cat and dog ------------
select ANIMAL_TYPE, count(ANIMAL_ID)
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE

-- ---------- find animal which has same name ----------
SELECT NAME, count(ANIMAL_ID) as count
from ANIMAL_INS 
group by NAME having NAME != '' and count >=2
order by NAME

-- ----------- find missing tables ---------------
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
from ANIMAL_OUTS 
ANIMAL_OUTS left join ANIMAL_INS 
ANIMAL_INS on ANIMAL_OUTS.ANIMAL_ID=ANIMAL_INS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID is null

-- --------- find lucy and ella ------------------
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
where NAME = 'Lucy' or NAME = 'Ella' or NAME = 'Pickle' or NAME = 'Rogan' or NAME = 'Sabrina' or NAME = 'Mitty'

-- ----------- find name which include 'el' --------------
SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where ANIMAL_TYPE = 'Dog' and NAME like '%el%'
order by name

-- ----------- find sec upon intake ---------------
SELECT ANIMAL_ID, NAME, if(SEX_UPON_INTAKE like 'Intact%', 'X', 'O')
from ANIMAL_INS
order by ANIMAL_ID

-- ----------- change datetype to date --------------
SELECT ANIMAL_ID, NAME, date_format(datetime, '%Y-%m-%d') as 날짜
from ANIMAL_INS 
order by ANIMAL_ID


