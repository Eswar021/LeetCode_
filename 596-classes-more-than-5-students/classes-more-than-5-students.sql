select class from (select class,count(student) as cnt from courses group by class) as new where new.cnt>=5
