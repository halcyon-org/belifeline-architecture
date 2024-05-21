set export

default:
  @just --list

setup: setup-py setup-pnpm

setup-py:
  python3 -m venv env
  @if command -v source > /dev/null; then \
      source env/bin/activate; \
  else \
      ./env/bin/activate; \
  fi

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
