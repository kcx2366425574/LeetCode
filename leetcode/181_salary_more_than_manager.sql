-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |

 select e.name as Employee
 from Employee e left join (
     select id, salary
     from Employee
 )m on e.managerId = m.id
 where managerId is not null and  e.salary > m.salary
