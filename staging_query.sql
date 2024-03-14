with t4 as (
  
with t3 as (
  
with t2 as (
  
with t1 as (
  
SELECT DATETIME(opr_dt, TIME(opr_hr-1, 

case when OPR_INTERVAL=1 then 0
      when OPR_INTERVAL=2 then 15
      when OPR_INTERVAL=3 then 30
      when OPR_INTERVAL=4 then 45
      else 0
  end

, 0)) AS combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW, max(timestamp_utc) as mt FROM `quickstart-1598631876908.caiso_price.t3`

group by combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW

union all


SELECT DATETIME(opr_dt, TIME(opr_hr-1, 15,0)) AS combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW, timestamp_utc FROM `quickstart-1598631876908.caiso_price.t3`
where market_run_id='DAM'

union all


SELECT DATETIME(opr_dt, TIME(opr_hr-1, 30,0)) AS combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW, timestamp_utc FROM `quickstart-1598631876908.caiso_price.t3`
where market_run_id='DAM'

union all


SELECT DATETIME(opr_dt, TIME(opr_hr-1, 45,0)) AS combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW, timestamp_utc FROM `quickstart-1598631876908.caiso_price.t3`
where market_run_id='DAM'

)


select  distinct combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW, max(mt) as mt from t1
group by combined_datetime, node_id, market_run_id, XML_DATA_ITEM, MW

)

select t2.combined_datetime, node_id, 

case when market_run_id='HASP' then MW end as HASP,
case when market_run_id='DAM' then MW end as DAM,

 xml_data_item, from t2 

 )

 select a.combined_datetime, a.node_id, case when a.HASP is null then b.HASP else a.HASP end as HASP, case when a.DAM is null then b.DAM else a.DAM end as DAM, a.xml_data_item  from t3 a left join t3 b on a.combined_datetime=b.combined_datetime and a.xml_data_item=b.xml_data_item

)

select distinct *, HASP-DAM as Spread from t4

where HASP is not null and DAM is not null and xml_data_item in ('LMP_ENE_PRC', '')






