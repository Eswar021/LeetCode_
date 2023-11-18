select one.name as Employee from 
employee one
left join
employee two 
on 
one.managerId=two.id
where one.salary>=two.salary