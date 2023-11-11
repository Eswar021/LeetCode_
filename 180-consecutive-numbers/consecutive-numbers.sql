with new as (select *, lead(num,1) over() as next1,lead(num,2) over() as next2 from logs)

select distinct num as ConsecutiveNums 
from new
where num=next1 and num=next2