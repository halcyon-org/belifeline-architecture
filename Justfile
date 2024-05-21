set export

default:
  @just --list

setup: setup-py setup-pnpm

setup-py:
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt

setup-pnpm:
  pnpm install --frozen-lockfile
  
gen:
  python3 diagrams

lint: lint-py lint-md

lint-py: 
  black diagrams/

lint-md:
  pnpm lint
