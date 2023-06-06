with transform as (
    SELECT 
    INITCAP(TRIM(REGEXP_REPLACE(first_name, '[^a-zA-Z0-9]', '', 'g'))) as first_name,
    INITCAP(TRIM(REGEXP_REPLACE(last_name, '[^a-zA-Z0-9]', '', 'g'))) as last_name,
    CAST(unnest(regexp_matches(age, '\d+', 'g')) as int) as age,
    case
        WHEN UPPER(sex) LIKE 'MAN' THEN 'M'
        WHEN UPPER(sex) LIKE 'MALE' THEN 'M'
        WHEN upper(sex) LIKE 'GIRL' THEN 'F'
        WHEN upper(sex) LIKE 'FEMALE' THEN 'F'
        WHEN upper(sex) LIKE 'BOTH' THEN 'LGBT'
        WHEN upper(sex) LIKE 'FM' THEN 'LGBT'
        WHEN upper(sex) LIKE 'MF' THEN 'LGBT'
        WHEN upper(sex) LIKE '-' THEN 'Not Defined'
        ELSE upper(sex)
    END AS sex
FROM {{ ref('extract') }}


)
select *
from transform