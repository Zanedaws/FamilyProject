PRAGMA foreign_keys = ON;
CREATE TABLE users (userName TEXT, pswd TEXT, userHash TEXT PRIMARY KEY);
CREATE TABLE inputs (userHash TEXT, inputHash TEXT PRIMARY KEY, note TEXT, amount DOUBLE, inputTime TEXT DEFAULT CURRENT_TIMESTAMP, timeValue INT, FOREIGN KEY(userHash) REFERENCES users(userHash));
CREATE TABLE totals (name TEXT, ammount INT)