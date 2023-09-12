# Write your MySQL query statement below
select score,dense_rank() over(order by score desc) as 'rank' from scores;

#Select score, dense_rank() over (Order By score DESC) as 'rank' from Scores ;

