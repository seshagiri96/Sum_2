drop table if exists sess_table ;
create table sess_table (
  id integer primary key autoincrement,
  status text not null,
  sess_id text not null
);