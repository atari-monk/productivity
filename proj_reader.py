import argparse
import re
from pathlib import Path
from typing import Iterator, List, Optional, Pattern

class ProjectLogEntry:
    def __init__(self, date: str, duration: str, project: str, description: str):
        self.date = date
        self.duration = duration
        self.project = project
        self.description = description

    def __str__(self) -> str:
        return f"{self.date} {self.duration} {self.project}\n{self.description}"

class ProjectLogParser:
    ENTRY_PATTERN = re.compile(
        r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}-\d{2}:\d{2}) (\d+[hm]|\d+h\d+m) (.+?)\n([\s\S]*?)(?=\n\d{4}-\d{2}-\d{2} |\Z)",
        re.MULTILINE
    )

    def __init__(self, content: str):
        self.content = content

    def parse_entries(self) -> Iterator[ProjectLogEntry]:
        for match in self.ENTRY_PATTERN.finditer(self.content):
            date, time_range, duration, project, description = match.groups()
            full_duration = f"{time_range} {duration}"
            cleaned_description = description.strip()
            yield ProjectLogEntry(date, full_duration, project, cleaned_description)

class ProjectLogFilter:
    def __init__(self, entries: List[ProjectLogEntry]):
        self.entries = entries

    def filter_by_project(self, project_pattern: Pattern) -> List[ProjectLogEntry]:
        return [entry for entry in self.entries if project_pattern.search(entry.project)]

class ProjectLogReader:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def read_content(self) -> str:
        return self.file_path.read_text(encoding="utf-8")

def create_project_pattern(project_name: str) -> Pattern:
    return re.compile(re.escape(project_name), re.IGNORECASE)

def format_entries(entries: List[ProjectLogEntry]) -> str:
    return "\n\n".join(str(entry) for entry in entries)

def main():
    parser = argparse.ArgumentParser(description="Filter project log entries by project name")
    parser.add_argument("project", help="Project name to filter", default="C:/Atari-Monk-Art/productivity/proj-log-2025.txt")
    parser.add_argument("--file", default="C:/Atari-Monk-Art/productivity/proj-log-2025.txt", 
                       help="Path to project log file")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found at {file_path}")
        return

    reader = ProjectLogReader(file_path)
    content = reader.read_content()

    parser_instance = ProjectLogParser(content)
    entries = list(parser_instance.parse_entries())

    project_pattern = create_project_pattern(args.project)
    filter_instance = ProjectLogFilter(entries)
    filtered_entries = filter_instance.filter_by_project(project_pattern)

    if filtered_entries:
        print(format_entries(filtered_entries))
    else:
        print(f"No entries found for project: {args.project}")

if __name__ == "__main__":
    main()