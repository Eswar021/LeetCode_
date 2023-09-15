# select class from (select class,count(student) as cnt from courses group by class) as new where new.cnt>=5
# --------------
# select class from(
# select class,count(student) as std from courses
# group by class
# having std>=5) as new
# --------------
select class from courses
group by class
having count(student)>=5