set export

default:
  @just --list
  
gen:
  python3 diagrams

lint: lint-python lint-markdown

lint-python: 
  black diagrams/

lint-markdown:
  pnpm lint
