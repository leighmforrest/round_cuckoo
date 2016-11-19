-- Table definitions for the tournament project.
--
-- Do a clean install
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;


-- Create the players table.
CREATE TABLE players (
    id serial primary key,
    name text
);


-- Create the matches table.
CREATE TABLE matches (
    match_id serial primary key,
    winner integer REFERENCES players(id) NOT NULL,
    loser integer REFERENCES players(id) NOT NULL
    );


-- Create a view that returns players id, player's name, wins, and total matches
-- The view is called standings.
-- | id  | name  | wins | total_matches |
--
CREATE VIEW standings as
    SELECT players.id as id, players.name as name,
    (SELECT count(matches.winner)
        FROM matches
        WHERE players.id = matches.winner)
        as wins,
    (SELECT count(matches.match_id)
        FROM matches
        WHERE players.id = matches.winner
        OR players.id = matches.loser
    ) as total_matches
    FROM players
    ORDER BY wins DESC, total_matches DESC;
;
