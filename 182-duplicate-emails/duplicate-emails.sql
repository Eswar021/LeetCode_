# Write your MySQL query statement below
select new.email as Email from (select email,count(email) as cou from person
group by email)as new
where cou>=2