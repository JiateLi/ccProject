-- drop database if exists EchoDB;
create database if not exists EchoDB;

use EchoDB;

drop table if exists TweetQ4;
create table if not exists TweetQ4 (
    d DATE NOT NULL,
    loc VARCHAR(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    rank INTEGER(32) NOT NULL,
    tag VARCHAR(140) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
    tids TEXT NOT NULL,
    PRIMARY KEY (d, loc, rank)
);
