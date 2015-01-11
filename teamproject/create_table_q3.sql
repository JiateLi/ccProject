-- drop database if exists EchoDB;
create database if not exists EchoDB;

use EchoDB;

create table if not exists TweetQ3 (
    uid BIGINT(64) UNSIGNED NOT NULL,
    tuids TEXT NOT NULL,
    PRIMARY KEY (uid)
);
