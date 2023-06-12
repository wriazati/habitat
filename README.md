# Habitat data downloader 

(use the RST file. It looks better than this :)

Lets go through the basic steps to download todays bid data!

1.  MONGODB_VERSION=6.0-ubi8 docker run \--name mongodb -d -p
    27017:27017 -v data:/data/db
    mongodb/mongodb-community-server:\$MONGODB_VERSION

    > -   This command will download the latest MongoDB image and run
    >     via Docker
    > -   Prerequsite: must have docker desktop installed

2.  poetry install

    > -   Install project dependencies using a virtualenv

3.  poetry run python main.py \--download

    > -   Enables todays eso data.
    > -   Stores the data in the DB instance

4.  poetry run python main.py \--print \--query \'{\"Status\":
    \"Rejected\"}\'

    > -   Prints db data with query string [{\"Status\":
    >     \"Rejected\"}]{.title-ref}.
    > -   Optionally use without the \--query argument to see all data

5.  poetry run python main.py \--clear

    > -   Clears or resets any previous data set in the default
    >     collection.

6.  poetry run pytest

    > -   Runs the test suite
