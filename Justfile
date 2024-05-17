set export

default:
  @just --list
  
gen:
  python3 diagrams

lint:
  black diagrams/
  pnpm lint
