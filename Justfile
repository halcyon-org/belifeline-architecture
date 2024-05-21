set export

default:
  @just --list

setup:
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  
gen:
  python3 diagrams

lint: lint-python lint-markdown

lint-python: 
  black diagrams/

lint-markdown:
  pnpm lint
