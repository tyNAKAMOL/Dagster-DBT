with extract as (
    select *
    from {{ source('public', 'data_raw') }}

)
select *
from extract

