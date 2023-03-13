/*Filter by NAS IP*/
select ISE_NODE,USERNAME from Radius_authentications where NAS_IP_ADDRESS = '10.52.13.216';


/*Authentications by ISE Node*/
select  ise_node, sum(passed_count) as passed, sum(failed_count) as failed, sum(passed_count) + sum(failed_count) as total,round(to_char(((sum(failed_count) / (sum(passed_count) + sum(failed_count))) * 100)), 2) as failed_percentage, round(to_char(sum(total_response_time)/(sum(passed_count) + sum(failed_count))), 2) as total_response_time, max(max_response_time) as max_response_time from radius_authentication_summary group by ise_node;

/*Authentications by Allowed Protocol*/
select  access_service as allowed_protocol, sum(passed_count) as passed, sum(failed_count) as failed, sum(passed_count) + sum(failed_count) as total, round(to_char(((sum(failed_count) / (sum(passed_count) + sum(failed_count))) * 100)), 2) as failed_percentage, round(to_char(sum(total_response_time)/(sum(passed_count) + sum(failed_count))), 2) as total_response_time, max(max_response_time) as max_response_time from radius_authentication_summary group by access_service;

/*Authentications by Network Device Name*/
select  device_name as network_device_name, sum(passed_count) as passed, sum(failed_count) as failed, sum(passed_count) + sum(failed_count) as total, round(to_char(((sum(failed_count) / (sum(passed_count) + sum(failed_count))) * 100)), 2) as failed_percentage, round(to_char(sum(total_response_time)/(sum(passed_count) + sum(failed_count))), 2) as total_response_time, max(max_response_time) as max_response_time from radius_authentication_summary group by device_name;

/*Join two tables*/
select * from radius_authentications inner join radius_authentication_summary on radius_authentications.ISE_NODE = radius_authentication_summary.ISE_NODE;