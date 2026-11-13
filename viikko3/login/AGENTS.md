# Project guide

This directory contains a small Flask login and registration application with
Robot Framework browser tests. Keep changes for this project within this
directory unless the user explicitly asks otherwise.

## Structure

- `src/app.py` defines Flask routes and renders templates from `src/templates/`.
- `src/services/` contains user validation and authentication logic.
- `src/repositories/` contains the in-memory user repository.
- `src/entities/` contains domain objects.
- `src/tests/` contains Robot Framework browser tests. Shared browser settings
  and keywords are in `resource.robot`.
- `pyproject.toml` declares Python and project dependencies; `uv.lock` pins them.

## Running

- Install/synchronize dependencies with `uv sync`.
- Start the application from this directory with `uv run python3 src/index.py`.
  It listens on port 5001.
- With the application running, execute the browser tests with
  `uv run robot --variable HEADLESS:true src/tests`.

The browser tests use the application reset endpoint and expect the server to
be available at `localhost:5001`.

## Changes and tests

- Put business rules in the service layer rather than in Flask route handlers.
- Keep browser test cases in the relevant `.robot` suite and reuse shared
  keywords from `src/tests/resource.robot`.
- Run the relevant Robot Framework suite against a running application when
  changing routes, templates, or user-facing behavior.
