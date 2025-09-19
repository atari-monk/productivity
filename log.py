import sys
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, List

class LogEntry:
    def __init__(self, project: str, start_time: datetime, end_time: Optional[datetime] = None, note: str = ""):
        self.project = project
        self.start_time = start_time
        self.end_time = end_time
        self.note = note

    @property
    def duration(self) -> Optional[str]:
        if not self.end_time:
            return None
        total_minutes = int((self.end_time - self.start_time).total_seconds() / 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        if hours and minutes:
            return f"{hours}h{minutes}m"
        elif hours:
            return f"{hours}h"
        else:
            return f"{minutes}m"

    def format_entry(self) -> str:
        date_str = self.start_time.strftime("%Y-%m-%d")
        time_range = f"{self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')}" if self.end_time else self.start_time.strftime("%H:%M")
        duration_str = self.duration if self.duration else ""
        return f"{date_str} {time_range} {duration_str} {self.project}\n{self.note}".strip()

class LogFileHandler:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read_entries(self) -> List[LogEntry]:
        if not self.file_path.exists():
            return []
        
        entries = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        blocks = [block.strip() for block in content.split('\n\n') if block.strip()]
        
        for block in blocks:
            lines = block.split('\n')
            header = lines[0]
            note = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
            
            parts = header.split()
            if len(parts) < 3:
                continue
            
            try:
                date_str = parts[0]
                time_part = parts[1]
                project = ' '.join(parts[2:])
                
                if '-' in time_part:
                    start_str, end_str = time_part.split('-')
                    start_time = datetime.strptime(f"{date_str} {start_str}", "%Y-%m-%d %H:%M")
                    end_time = datetime.strptime(f"{date_str} {end_str}", "%Y-%m-%d %H:%M")
                    entries.append(LogEntry(project, start_time, end_time, note))
                else:
                    start_time = datetime.strptime(f"{date_str} {time_part}", "%Y-%m-%d %H:%M")
                    entries.append(LogEntry(project, start_time, note=note))
            except ValueError:
                continue
        
        return entries

    def get_active_entry(self) -> Optional[LogEntry]:
        entries = self.read_entries()
        for entry in reversed(entries):
            if not entry.end_time:
                return entry
        return None

    def write_entry(self, entry: LogEntry):
        with open(self.file_path, 'a', encoding='utf-8') as file:
            file.write(f"{entry.format_entry()}\n\n")

    def append_note_to_active_entry(self, new_note: str):
        content = self.file_path.read_text(encoding='utf-8')
        blocks = [block.strip() for block in content.split('\n\n') if block.strip()]
        
        for i, block in enumerate(reversed(blocks)):
            lines = block.split('\n')
            header = lines[0]
            
            if '-' not in header.split()[1]:
                active_block_index = len(blocks) - 1 - i
                if len(lines) > 1:
                    existing_notes = '\n'.join(lines[1:])
                    blocks[active_block_index] = f"{header}\n{existing_notes}\n{new_note}"
                else:
                    blocks[active_block_index] = f"{header}\n{new_note}"
                
                self.file_path.write_text('\n\n'.join(blocks) + '\n\n', encoding='utf-8')
                return
        
        raise ValueError("No active entry found to update")

    def get_last_entries(self, count: int) -> List[LogEntry]:
        entries = self.read_entries()
        return entries[-count:] if count > 0 else entries

class LogManager:
    def __init__(self, file_handler: LogFileHandler):
        self.file_handler = file_handler

    def start_entry(self, project: str, note: str = ""):
        active_entry = self.file_handler.get_active_entry()
        if active_entry:
            print(f"There is already an active entry for project: {active_entry.project}")
            return
        
        new_entry = LogEntry(project, datetime.now(), note=note)
        self.file_handler.write_entry(new_entry)
        print(f"Started logging for project: {project}")

    def add_note(self, note: str):
        active_entry = self.file_handler.get_active_entry()
        if not active_entry:
            print("No active entry to add note to.")
            return
        
        self.file_handler.append_note_to_active_entry(note)
        print("Note added to current entry.")

    def end_entry(self, note: str = ""):
        active_entry = self.file_handler.get_active_entry()
        if not active_entry:
            print("No active entry to end.")
            return
        
        if note:
            self.file_handler.append_note_to_active_entry(note)
        
        active_entry.end_time = datetime.now()
        active_entry.note = self.get_active_entry_notes()
        
        content = self.file_handler.file_path.read_text(encoding='utf-8')
        blocks = [block.strip() for block in content.split('\n\n') if block.strip()]
        
        for i, block in enumerate(blocks):
            lines = block.split('\n')
            header = lines[0]
            
            if '-' not in header.split()[1]:
                blocks[i] = active_entry.format_entry()
                break
        
        self.file_handler.file_path.write_text('\n\n'.join(blocks) + '\n\n', encoding='utf-8')
        print(f"Entry ended. Duration: {active_entry.duration}")

    def get_active_entry_notes(self) -> str:
        content = self.file_handler.file_path.read_text(encoding='utf-8')
        blocks = [block.strip() for block in content.split('\n\n') if block.strip()]
        
        for block in reversed(blocks):
            lines = block.split('\n')
            header = lines[0]
            
            if '-' not in header.split()[1]:
                return '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
        
        return ""

    def print_active(self):
        active_entry = self.file_handler.get_active_entry()
        if active_entry:
            print("Active entry:")
            print(active_entry.format_entry())
        else:
            print("No active entry.")

    def print_last_entries(self, count: int = 5):
        entries = self.file_handler.get_last_entries(count)
        if not entries:
            print("No entries found.")
            return
        
        print(f"Last {len(entries)} entries:")
        for i, entry in enumerate(reversed(entries), 1):
            print(f"\n{i}. {entry.format_entry()}")

def main():
    log_path = Path("C:/Atari-Monk-Art/productivity/proj-log-2025.txt")
    file_handler = LogFileHandler(log_path)
    log_manager = LogManager(file_handler)

    args = sys.argv[1:]

    if not args:
        print("Usage: <command> [args]")
        print("Commands:")
        print("  <project_name> [note] - Start logging for project")
        print("  note <note> - Add note to current entry")
        print("  end [note] - End current entry with optional note")
        print("  print [count] - Print active entry or last N entries")
        return

    command = args[0].lower()

    if command == "note":
        if len(args) < 2:
            print("Please provide a note.")
            return
        note = ' '.join(args[1:])
        log_manager.add_note(note)
    elif command == "end":
        note = ' '.join(args[1:]) if len(args) > 1 else ""
        log_manager.end_entry(note)
    elif command == "print":
        if len(args) > 1 and args[1].isdigit():
            count = int(args[1])
            log_manager.print_last_entries(count)
        else:
            log_manager.print_active()
    else:
        project = args[0]
        note = ' '.join(args[1:]) if len(args) > 1 else ""
        log_manager.start_entry(project, note)

if __name__ == "__main__":
    main()