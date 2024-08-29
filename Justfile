set export

default:
  @just --list

setup: setup-py setup-pnpm

setup-py:
  python3 -m venv env
  env/bin/pip3 install -r requirements.txt

setup-pnpm:
  pnpm install --frozen-lockfile
  
gen:
  env/bin/python3 diagrams

lint: lint-py lint-md

lint-py: setup-py
  env/bin/black diagrams/
  env/bin/isort diagrams/

lint-md: setup-pnpm
  pnpm lint:fix
