DROP TABLE if exists jobslog_01;
CREATE TABLE jobslog_01 (
  id SERIAL PRIMARY KEY,
  date DATE,
  time TIME,
  job VARCHAR,
  description VARCHAR,
  outcome VARCHAR,
  comments VARCHAR,
  date_stamp DATE,
  time_stamp TIME
  );