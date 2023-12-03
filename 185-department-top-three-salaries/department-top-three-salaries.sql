/* Write your T-SQL query statement below */
select Department,Employee,salary from (select department.name as Department,employee.name as Employee, employee.salary as Salary,dense_rank() over(partition by departmentid order by salary desc) as new from 
employee
left join
department
on
employee.departmentid=department.id) as new_table
where new_table.new=1 or new_table.new=2 or new_table.new=3



