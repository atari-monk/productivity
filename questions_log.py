import argparse
import datetime
import os
import sys
from pathlib import Path

class QuestionLogger:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def _read_entries(self):
        if not self.file_path.exists():
            return []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read().split('\n\n')

    def _write_entries(self, entries):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(entries))

    def add_timestamp_entry(self, note=None):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        entry = timestamp
        if note:
            entry += f"\n{note}"
        entries = self._read_entries()
        entries.append(entry)
        self._write_entries(entries)

    def append_to_last_entry(self, note):
        entries = self._read_entries()
        if not entries:
            self.add_timestamp_entry(note)
            return
        last_entry = entries[-1]
        if '\n' in last_entry:
            entries[-1] += f"\n{note}"
        else:
            entries[-1] += f"\n{note}"
        self._write_entries(entries)

    def add_empty_line(self):
        entries = self._read_entries()
        entries.append('')
        self._write_entries(entries)

    def print_entries(self, last_n=None):
        entries = self._read_entries()
        if last_n:
            entries = entries[-last_n:]
        for entry in entries:
            print(entry)
            print()

    def search_entries(self, tag):
        entries = self._read_entries()
        for entry in entries:
            if tag.lower() in entry.lower():
                print(entry)
                print()

def main():
    parser = argparse.ArgumentParser(description='Question and Answer logging system', usage='''questions_log.py <command> [options]

Commands:
  start         Add a timestamp entry with optional note
  add           Append to the last entry or add empty line
  print         Display all or last N entries
  search        Search entries containing specific text

Use 'questions_log.py <command> --help' for more information about a command.
''')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    start_parser = subparsers.add_parser('start', help='Add timestamp entry')
    start_parser.add_argument('--note', help='Optional note text')

    add_parser = subparsers.add_parser('add', help='Append to last entry')
    add_group = add_parser.add_mutually_exclusive_group(required=True)
    add_group.add_argument('--note', help='Note text to append')
    add_group.add_argument('--empty', action='store_true', help='Add empty line')

    print_parser = subparsers.add_parser('print', help='Display entries')
    print_parser.add_argument('--last', type=int, help='Show last N entries')

    search_parser = subparsers.add_parser('search', help='Search entries')
    search_parser.add_argument('--tag', required=True, help='Tag text to search')

    args = parser.parse_args()

    logger = QuestionLogger('C:/Atari-Monk-Art/productivity/questions-log-2025.txt')

    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == 'start':
        logger.add_timestamp_entry(args.note)
    elif args.command == 'add':
        if args.empty:
            logger.add_empty_line()
        else:
            logger.append_to_last_entry(args.note)
    elif args.command == 'print':
        logger.print_entries(args.last)
    elif args.command == 'search':
        logger.search_entries(args.tag)

if __name__ == '__main__':
    main()