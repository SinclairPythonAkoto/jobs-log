DROP TABLE if exists jobslog_01;
CREATE TABLE jobslog_01 (
  id SERIAL PRIMARY KEY,
  date VARCHAR,
  time VARCHAR,
  job VARCHAR,
  description VARCHAR,
  outcome VARCHAR,
  comments VARCHAR,
  date_stamp VARCHAR,
  time_stamp VARCHAR
  );