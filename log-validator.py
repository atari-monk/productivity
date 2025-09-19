import sys
import re
from datetime import datetime, timedelta
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
        
        # Allow various duration formats: 1h, 30m, 1h30m, 1h30m, etc.
        pattern = r'^(\d+h)?(\d+m)?$'
        return bool(re.match(pattern, self.duration))

    def validate_project_name(self) -> bool:
        # Allow alphanumeric, spaces, hyphens, apostrophes, and parentheses
        # This accommodates project names like 'game-hub' and job entries like 'Programista operator frezarki CNC'
        pattern = r'^[a-zA-Z0-9\s\-\'\(\)]+$'
        return bool(re.match(pattern, self.project))

    def calculate_duration(self) -> Optional[str]:
        if not self.start_time or not self.end_time:
            return None
        
        try:
            start_dt = datetime.strptime(self.start_time, '%H:%M')
            end_dt = datetime.strptime(self.end_time, '%H:%M')
            
            # Handle cross-midnight scenario
            if end_dt < start_dt:
                # Add one day to end time for calculation
                end_dt = end_dt + timedelta(days=1)
            
            total_seconds = (end_dt - start_dt).total_seconds()
            total_minutes = int(total_seconds // 60)
            
            hours = total_minutes // 60
            minutes = total_minutes % 60
            
            duration_parts = []
            if hours > 0:
                duration_parts.append(f'{hours}h')
            if minutes > 0:
                duration_parts.append(f'{minutes}m')
            
            return ''.join(duration_parts) if duration_parts else '0m'
        except ValueError:
            return None

    def validate_notes(self) -> bool:
        # Remove strict capitalization requirement for notes
        # Only check that notes are not empty if they exist
        if not self.notes:
            return True
        return all(note.strip() for note in self.notes)

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
            
            # Check if this line starts a new entry (starts with date pattern)
            if re.match(r'^\d{4}-\d{2}-\d{2}', line):
                if current_entry:
                    self.entries.append(current_entry)
                
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
                    # Incomplete entry line, treat as note for previous entry or ignore
                    if current_entry:
                        current_entry.notes.append(line)
            elif current_entry:
                # This is a continuation note for the current entry
                current_entry.notes.append(line)
            else:
                # Orphan line without a parent entry - could be handled or ignored
                # For now, we'll create a minimal entry to capture the error
                current_entry = LogEntry('', '', '', '', line, [])
                current_entry.line_number = line_number
                self.entries.append(current_entry)
                current_entry = None

        if current_entry:
            self.entries.append(current_entry)

    def validate_entries(self) -> Generator[Dict, None, None]:
        for entry in self.entries:
            # Skip validation for orphan lines that aren't proper entries
            if not entry.date_str or not entry.validate_date_format():
                if entry.date_str:  # Only report if it looks like it was supposed to be a date
                    yield {
                        'line': entry.line_number,
                        'type': 'date_format',
                        'message': f'Invalid date format: {entry.date_str}',
                        'entry': entry
                    }
                continue
            
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
            
            # Only check duration mismatch if we have valid start and end times
            if (entry.validate_time_format(entry.start_time) and 
                entry.validate_time_format(entry.end_time)):
                calculated_duration = entry.calculate_duration()
                if (calculated_duration and entry.duration and 
                    entry.duration != calculated_duration):
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
                    'message': 'Notes should not be empty',
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
    entry = error['entry']
    if entry.date_str:
        print(f"Entry: {entry.date_str} {entry.start_time}-{entry.end_time} {entry.duration} {entry.project}")
    else:
        print(f"Entry: {entry.project}")
    if entry.notes:
        print("Notes:")
        for note in entry.notes:
            print(f"  {note}")
    print("-" * 80)

def save_errors_to_md(errors: List[Dict], output_path: Path) -> None:
    with open(output_path, 'w', encoding='utf-8') as md_file:
        md_file.write("# Log Validation Errors\n\n")
        md_file.write(f"Found {len(errors)} validation errors:\n\n")
        
        for error in errors:
            md_file.write(f"## Line {error['line']}: {error['type']}\n")
            md_file.write(f"**Message**: {error['message']}\n\n")
            
            entry = error['entry']
            if entry.date_str:
                md_file.write(f"**Entry**: {entry.date_str} {entry.start_time}-{entry.end_time} {entry.duration} {entry.project}\n\n")
            else:
                md_file.write(f"**Entry**: {entry.project}\n\n")
            
            if entry.notes:
                md_file.write("**Notes**:\n")
                for note in entry.notes:
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