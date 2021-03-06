# ISA

- [Getting Started](#getting-started)
- [Running Commands](#running-commands)
- [User Stories](#user-stories)

## Getting Started
### Quickstart (download/build/run containers)

Run this command from the top-level directory:

```bash
bin/start
```

### To start up Spark, run:

```bash
bin/spark -v
```

Leave off the -v flag for quiet output.

### Drop into MySQL repl

```bash
bin/edit-db
```

### Nuclear option

Database is broken? Want to blow it up? Run this:

```bash
bin/wipe-all
```

### Run Jmeter performance tests

```bash
bin/jmeter-test
```

## Running Commands

You may want to run a command within a docker-compose service (e.g. `web`).
For example, to open a Django shell on the `web` service:

```bash
docker-compose exec web python manage.py shell_plus
```

Other useful management commands include `clear_cache`, `reset_db`, and `syncdata`.
More commands and details [here](https://django-extensions.readthedocs.io/en/latest/command_extensions.html).

Along the same lines, a simple `bash` shell can be entered via:

```bash
docker-compose exec web bash
```

## User stories

1. As a user, I want to view a list of users and bids that have already been placed in each lottery so I can determine if I want to place a bid.
2. As a user, I want to sort the lottery list by end-date so that I can find out which lotteries are ending soonest.
3. As a user, I want to view the details of a specific card so that I can decide if I want to bid for it.
4. As a user, I want to view the details of a lottery so that I can determine if I want to place a bid in it.
5. As a user, I want to see a list of open lotteries so that I can view the details of each.
6. As a user, I want to be able to create a new account.
7. As a user, I want to easily be able to log into my account from the home page.
8. As a user, I want to create new lotteries.
9. As a user, I want the site to remember my credentials while I'm on the website.
10. As a user, I want my login information to be securely stored.
11. As a user, I want to be able to search for lotteries and cards so that I can locate specific entries.
12. As a user, I want new lotteries and cards that I add to show up in the search database so that I know others can find them.
13. As a user, I want to be able to filter my searches so that I can find specific entries more easily.
14. As a user, I want the search bar to be accessible at the top of all screens so that I can easily search from anywhere on the site.
15. As a user, I want to be able to see recommended lotteries based on what lotteries are often accessed together by users.
