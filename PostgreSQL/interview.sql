-- Problem 1
DROP TABLE IF EXISTS piblic.cars;
CREATE TABLE public.cars
(
    id SMALLSERIAL,
    model_name CHARACTER VARYING(100),
	color CHARACTER VARYING(100),
	brand CHARACTER VARYING(100)
);

INSERT INTO 
	public.cars (model_name, color, brand)
VALUES
    ('Leaf','Black', 'Nissan'),
	('Leaf','Black', 'Nissan'),
	('Model S','Black', 'Tesla'),
	('Model X','White', 'Tesla'),
	('RAV4','Black', 'Toyota'),
	('RAV4','Red', 'Toyota'),
	('RAV4','Black', 'Toyota'),
	('Camry','White', 'Toyota');
	
SELECT * FROM public.cars;

-- Select Duplicate Rows
-- Solution 1
SELECT * 
FROM public.cars
WHERE id NOT IN (
	SELECT max(id)
	FROM public.cars
	GROUP BY model_name, brand, color
);

----------------------------------------
-- Problem 2
drop table if exists job_positions;
create table job_positions
(
	id			int,
	title 		varchar(100),
	groups 		varchar(10),
	levels		varchar(10),
	payscale	int,
	totalpost	int
);
insert into job_positions values (1, 'General manager', 'A', 'l-15', 10000, 1);
insert into job_positions values (2, 'Manager', 'B', 'l-14', 9000, 5);
insert into job_positions values (3, 'Asst. Manager', 'C', 'l-13', 8000, 10);

drop table if exists job_employees;
create table job_employees
(
	id				int,
	name 			varchar(100),
	position_id 	int
);
insert into job_employees values (1, 'John Smith', 1);
insert into job_employees values (2, 'Jane Doe', 2);
insert into job_employees values (3, 'Michael Brown', 2);
insert into job_employees values (4, 'Emily Johnson', 2);
insert into job_employees values (5, 'William Lee', 3);
insert into job_employees values (6, 'Jessica Clark', 3);
insert into job_employees values (7, 'Christopher Harris', 3);
insert into job_employees values (8, 'Olivia Wilson', 3);
insert into job_employees values (9, 'Daniel Martinez', 3);
insert into job_employees values (10, 'Sophia Miller', 3);

select * from job_positions;
select * from job_employees;

-- Solution
SELECT jp.title, jp.groups AS group, jp.levels AS level, jp.payscale, COALESCE(e.name, 'N/A') AS employee_name
FROM job_positions AS jp
CROSS JOIN generate_series(1, jp.totalpost)
LEFT JOIN (SELECT name, position_id, row_number() over(partition by position_id) as rn
FROM job_employees) AS e
ON e.position_id = jp.id AND e.rn=generate_series;

-- Problem 3
DROP TABLE IF EXISTS icc_world_cup;
CREATE TABLE icc_world_cup
(
	Team_1 CHARACTER VARYING(20),
	Team_2 CHARACTER VARYING(20),
	Winner CHARACTER VARYING(20)
);
INSERT INTO icc_world_cup values('India','SL','India');
INSERT INTO icc_world_cup values('SL','Aus','Aus');
INSERT INTO icc_world_cup values('SA','Eng','Eng');
INSERT INTO icc_world_cup values('Eng','NZ','NZ');
INSERT INTO icc_world_cup values('Aus','India','India');

SELECT
	a.team AS team_name,
	COUNT(a.team) AS no_of_matchs_played,
	SUM(a.win_flag) AS won,
	COUNT(a.team) - SUM(a.win_flag) AS loss
FROM (
	SELECT 
		team_1 AS team, 
		CASE 
			WHEN team_1 = winner 
			THEN 1 
			ELSE 0 
		END AS win_flag
	FROM icc_world_cup
	UNION ALL
	SELECT 
		team_2 AS team, 
		CASE 
			WHEN team_2 = winner 
			THEN 1 
			ELSE 0 
		END AS win_flag
	FROM icc_world_cup
) AS a 
GROUP BY a.team
ORDER BY won DESC;

-- Problem 4
DROP TABLE IF EXISTS customer_orders;
CREATE TABLE customer_orders (
	order_id integer,
	customer_id integer,
	order_date date,
	order_amount integer
);

INSERT INTO customer_orders 
VALUES
	(1,100,cast('2022-01-01' as date),2000),
	(2,200,cast('2022-01-01' as date),2500),
	(3,300,cast('2022-01-01' as date),2100),
	(4,100,cast('2022-01-02' as date),2000),
	(5,400,cast('2022-01-02' as date),2200),
	(6,500,cast('2022-01-02' as date),2700),
	(7,100,cast('2022-01-03' as date),3000),
	(8,400,cast('2022-01-03' as date),1000),
	(9,600,cast('2022-01-03' as date),3000);

SELECT 
	order_date,
	SUM(order_amount) AS total_sale
FROM customer_orders
GROUP BY order_date
ORDER BY total_sale DESC;

SELECT 
	*
FROM customer_orders;

WITH 
first_visit AS (
SELECT 
	customer_id,
	MIN(order_date) AS first_visit_date
FROM customer_orders
GROUP BY customer_id),
visit_flag AS (
SELECT 
	co.customer_id,
	co.order_amount,
	co.order_date, 
	CASE 
		WHEN co.order_date = fv.first_visit_date 
		THEN 1 
		ELSE 0 
	END AS first_visit_flag,
	CASE 
		WHEN co.order_date != fv.first_visit_date 
		THEN 1 
		ELSE 0 
	END AS repeat_visit_flag
FROM customer_orders AS co
INNER JOIN first_visit as fv
ON co.customer_id = fv.customer_id
ORDER BY co.order_date)

SELECT
	vf.order_date,
	SUM(vf.first_visit_flag) AS total_first_visit,
	SUM(vf.first_visit_flag * vf.order_amount) AS total_amount_first_visitor,
	SUM(vf.repeat_visit_flag) AS total_repeat_visit,
	SUM(vf.repeat_visit_flag * vf.order_amount) AS total_amount_repeat_visitor
FROM visit_flag AS vf
GROUP BY vf.order_date
ORDER BY vf.order_date ASC;

-- Problem 5



