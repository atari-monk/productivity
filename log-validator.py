import sys
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Generator
import argparse

class LogEntry:
    def __init__(self, date_str: str, start_time: str, end_time: str, duration: str, project: str, notes: List[str]):
        self.date_str = date_str
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.project = project
        self.notes = notes
        self.line_number = 0

    def validate_date_format(self) -> bool:
        try:
            datetime.strptime(self.date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_time_format(self, time_str: str) -> bool:
        if not time_str:
            return True
        try:
            datetime.strptime(time_str, '%H:%M')
            return True
        except ValueError:
            return False

    def validate_duration_format(self) -> bool:
        if not self.duration:
            return True
        pattern = r'^(\d+h)?(\d+m)?$'
        return bool(re.match(pattern, self.duration))

    def validate_project_name(self) -> bool:
        return bool(re.match(r'^[a-z]+(-[a-z]+)*$', self.project))

    def calculate_duration(self) -> Optional[str]:
        if not self.start_time or not self.end_time:
            return None
        
        try:
            start = datetime.strptime(self.start_time, '%H:%M')
            end = datetime.strptime(self.end_time, '%H:%M')
            
            if end < start:
                end = datetime.strptime('23:59', '%H:%M')
                partial_end = datetime.strptime('00:00', '%H:%M')
                duration1 = (datetime.strptime('23:59', '%H:%M') - start).seconds // 60
                duration2 = (end - partial_end).seconds // 60
                total_minutes = duration1 + duration2 + 1
            else:
                total_minutes = (end - start).seconds // 60
            
            hours = total_minutes // 60
            minutes = total_minutes % 60
            
            duration_parts = []
            if hours > 0:
                duration_parts.append(f'{hours}h')
            if minutes > 0:
                duration_parts.append(f'{minutes}m')
            
            return ''.join(duration_parts) if duration_parts else '0h0m'
        except ValueError:
            return None

    def validate_notes(self) -> bool:
        return all(note and note[0].isupper() for note in self.notes if note.strip())

class LogValidator:
    def __init__(self):
        self.entries: List[LogEntry] = []
        self.errors: List[Dict] = []

    def parse_log_file(self, file_path: Path) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        current_entry = None
        line_number = 0
        
        for line in lines:
            line_number += 1
            line = line.strip()
            
            if not line:
                if current_entry:
                    self.entries.append(current_entry)
                    current_entry = None
                continue
            
            if current_entry is None:
                parts = line.split()
                if len(parts) >= 4:
                    date_part = parts[0]
                    time_part = parts[1]
                    duration_part = parts[2]
                    project_part = ' '.join(parts[3:])
                    
                    if '-' in time_part:
                        start_time, end_time = time_part.split('-')
                    else:
                        start_time, end_time = time_part, ''
                    
                    current_entry = LogEntry(date_part, start_time, end_time, duration_part, project_part, [])
                    current_entry.line_number = line_number
            else:
                current_entry.notes.append(line)

        if current_entry:
            self.entries.append(current_entry)

    def validate_entries(self) -> Generator[Dict, None, None]:
        for entry in self.entries:
            if not entry.validate_date_format():
                yield {
                    'line': entry.line_number,
                    'type': 'date_format',
                    'message': f'Invalid date format: {entry.date_str}',
                    'entry': entry
                }
            
            if not entry.validate_time_format(entry.start_time):
                yield {
                    'line': entry.line_number,
                    'type': 'time_format',
                    'message': f'Invalid start time format: {entry.start_time}',
                    'entry': entry
                }
            
            if not entry.validate_time_format(entry.end_time):
                yield {
                    'line': entry.line_number,
                    'type': 'time_format',
                    'message': f'Invalid end time format: {entry.end_time}',
                    'entry': entry
                }
            
            if not entry.validate_duration_format():
                yield {
                    'line': entry.line_number,
                    'type': 'duration_format',
                    'message': f'Invalid duration format: {entry.duration}',
                    'entry': entry
                }
            
            calculated_duration = entry.calculate_duration()
            if calculated_duration and entry.duration != calculated_duration:
                yield {
                    'line': entry.line_number,
                    'type': 'duration_mismatch',
                    'message': f'Duration mismatch: recorded {entry.duration}, calculated {calculated_duration}',
                    'entry': entry
                }
            
            if not entry.validate_project_name():
                yield {
                    'line': entry.line_number,
                    'type': 'project_name',
                    'message': f'Invalid project name format: {entry.project}',
                    'entry': entry
                }
            
            if not entry.validate_notes():
                yield {
                    'line': entry.line_number,
                    'type': 'notes_format',
                    'message': 'Notes should start with capital letter and not be empty',
                    'entry': entry
                }

    def validate_first_error(self) -> Optional[Dict]:
        for error in self.validate_entries():
            return error
        return None

    def validate_all_errors(self) -> List[Dict]:
        return list(self.validate_entries())

def print_error_to_cli(error: Dict) -> None:
    print(f"Line {error['line']}: {error['type']} - {error['message']}")
    print(f"Entry: {error['entry'].date_str} {error['entry'].start_time}-{error['entry'].end_time} {error['entry'].duration} {error['entry'].project}")
    if error['entry'].notes:
        print("Notes:")
        for note in error['entry'].notes:
            print(f"  {note}")
    print("-" * 80)

def save_errors_to_md(errors: List[Dict], output_path: Path) -> None:
    with open(output_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Log Validation Errors\n\n")
        md_file.write(f"Found {len(errors)} validation errors:\n\n")
        
        for error in errors:
            md_file.write(f"## Line {error['line']}: {error['type']}\n")
            md_file.write(f"**Message**: {error['message']}\n\n")
            md_file.write(f"**Entry**: {error['entry'].date_str} {error['entry'].start_time}-{error['entry'].end_time} {error['entry'].duration} {error['entry'].project}\n\n")
            
            if error['entry'].notes:
                md_file.write("**Notes**:\n")
                for note in error['entry'].notes:
                    md_file.write(f"- {note}\n")
                md_file.write("\n")
            
            md_file.write("---\n\n")

def main():
    parser = argparse.ArgumentParser(description='Validate productivity log file')
    parser.add_argument('log_file', help='Path to the log file to validate')
    parser.add_argument('--output', '-o', help='Path to output MD file for all errors')
    parser.add_argument('--first', '-f', action='store_true', help='Stop at first error and print to CLI')
    
    args = parser.parse_args()
    
    log_file_path = Path(args.log_file)
    
    if not log_file_path.exists():
        print(f"Error: File {log_file_path} does not exist")
        sys.exit(1)
    
    validator = LogValidator()
    validator.parse_log_file(log_file_path)
    
    if args.first:
        error = validator.validate_first_error()
        if error:
            print_error_to_cli(error)
            sys.exit(1)
        else:
            print("No validation errors found!")
            sys.exit(0)
    elif args.output:
        errors = validator.validate_all_errors()
        if errors:
            output_path = Path(args.output)
            save_errors_to_md(errors, output_path)
            print(f"Found {len(errors)} errors. Saved to {output_path}")
            sys.exit(1)
        else:
            print("No validation errors found!")
            sys.exit(0)
    else:
        errors = validator.validate_all_errors()
        if errors:
            print(f"Found {len(errors)} validation errors:")
            print("-" * 80)
            for error in errors:
                print_error_to_cli(error)
            sys.exit(1)
        else:
            print("All log entries are valid!")
            sys.exit(0)

if __name__ == "__main__":
    main()