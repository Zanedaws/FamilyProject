PRAGMA foreign_keys = ON;
CREATE TABLE users (userName TEXT, pswd TEXT, userHash TEXT PRIMARY KEY);
CREATE TABLE inputs (userHash TEXT, inputHash TEXT, note TEXT, amount INT, inputTime TEXT DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(userHash) REFERENCES users(userHash));
CREATE TABLE totals (name TEXT, ammount INT)