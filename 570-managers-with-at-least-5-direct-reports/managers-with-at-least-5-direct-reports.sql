# Write your MySQL query statement below
select a.name from employee as a 
cross join employee  as b
on 
a.id=b.managerid
group by a.id
having count(b.managerid)>=5
