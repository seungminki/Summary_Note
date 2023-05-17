create table temp3 ( --table 생성
	col0 VARCHAR
	, col1 INT
	, col2 TIMESTAMP
);

alter table temp2 ADD column  col3 CHAR(10); -- column 추가

alter table temp2 drop column col3; -- column 삭제

alter table temp2 rename column col0 to text; -- column 이름 변경

alter table temp2 rename TO temp1; -- table 이름 변경

alter table temp1 alter column col1 type FLOAT; -- column type 변경

drop table TEMP1; --table 삭제

create table today_study ( -- table 생성
	col0 CHAR(8)
	, summry VARCHAR
	, note VARCHAR
);

alter table today_study add column idx INT; -- column 추가

insert into today_study ( -- value 추가
	col0
	, summry
	, note
	, idx
) values (
	'20221208'
	, '오리엔테이션'
	, '   '
	, 1
);
	
insert into today_study -- value 여러개 추가
	(col0, summry, note, idx) 
values 
	('20221208', '관련직무', '   ', 2)
	, ('20221208', '환경구성', '   ', 3)
	, ('20221208', '데이터의 위치', '     ', 3)
	, ('20221208', '데이터의 종류', '     ', 3)
;

create table today_study_bak AS ( --  백업 table 생성
select * from today_study where 0=1)
;

insert into today_study_bak -- 백업 table value 넣기
select *
from today_study
;

update today_study -- where 절을 찾아서 값을 변경
set idx = 4
where  summry = '데이터의 위치'
;

update today_study -- where 절을 찾아서 값을 변경
set idx = 5
where  summry = '데이터의 종류'
;

update today_study -- null값은 [NULL]이라고 뜸
set note = null 
where  note  = '   '
;

delete from today_study -- where에 해당되는 row들이 다 날라감
where note = '     '
;

delete from today_study -- table 형태는 남아있고 값만 삭제됨
;

truncate table TODAY_STUDY_BAK; --backup tabled에 똑같이 복사됨
