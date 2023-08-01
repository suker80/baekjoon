-- 코드를 입력하세요
SELECT PRODUCT_CODE , (sum(sales_amount) * price) as SALES
# select product_code , sum(sales_amount)
from product as p 
inner join offline_sale as os on p.product_id = os.product_id
group by product_code
order by SALES desc, PRODUCT_CODE asc;