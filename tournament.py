#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
# Checked for PEP8 conformity with http://pep8online.com/
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM players")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT count(name) from players")
    count = cursor.fetchone()[0]
    db.close()
    return int(count)


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, wins, total_matches FROM standings")
    matches = cursor.fetchall()
    db.close()
    return matches


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO matches (winner, loser) VALUES (%s, %s)", (winner, loser)
    )
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []  # Collection of pairs
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM standings ORDER BY wins DESC")
    pair_listing = cursor.fetchall()
    if len(pair_listing) % 2 == 0:
        # if there are an even number of pairings, iterate over pair_listing,
        # create the matches
        for i in range(0, len(pair_listing), 2):
            pair = (pair_listing[i][0], pair_listing[i][1],
                    pair_listing[i + 1][0], pair_listing[i + 1][1])
            pairings.append(pair)
        # Close before returning.
        db.close()
        return pairings
    else:
        # Otherwise, print a statement and close.
        print "There are an uneven number of players in the tournament"
        db.close()
