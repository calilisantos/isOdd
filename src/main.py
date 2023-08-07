from .orchestrator import Orchestrator
import sys

def main():
  entry_value = sys.argv[1]
  limit_value = sys.argv[2]
  orchestrator = Orchestrator(entry_value, limit_value)
  print(orchestrator.show_result())

if __name__ == '__main__':
  main()
