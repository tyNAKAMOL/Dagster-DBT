with load_ as (
    select * 
    from {{ ref('transform') }}

)
select *
from load_