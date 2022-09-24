# Write your MySQL query statement below
select p.product_id, p.product_name from (
    select distinct(product_id) from Sales t where t.product_id not in (
        select distinct(product_id) from Sales where Sales.sale_date > date("2019-03-31") or
        Sales.sale_date < date("2019-01-01")
    ) and t.sale_date >= date("2019-01-01") and t.sale_date <= date("2019-03-31")
)s left join Product p
on p.product_id = s.product_id



select
    a.product_id,
    b.product_name,
from
(
select
    product_id,
    min(sale_date) as min_sale_date,
    max(sale_date) as max_sale_date,
from Sales
group by 1
) a
left join Product b on a.product_id = b.product_id
where a.min_sale_date >= date('2019-01-01') and a.max_sale_date <= date('2019-03-01')