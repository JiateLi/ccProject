create database if not exists EchoDB;
use EchoDB;
create table if not exists TweetQ2 (
    uid BIGINT(64) UNSIGNED NOT NULL,
    ts TIME NOT NULL,
    rst VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
    PRIMARY KEY (uid, ts)
);
