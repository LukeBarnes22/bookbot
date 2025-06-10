from stats import getBookText
from stats import print_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_info = getBookText(sys.argv[1])
    print_report(book_info)

main()
