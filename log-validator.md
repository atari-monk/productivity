# Log Validation Script Rules Report

## Overview
The `log-validator.py` script enforces the following validation rules on productivity log files:

## 1. Date Format Validation
- **Rule**: Dates must follow the `YYYY-MM-DD` format
- **Validation Method**: `validate_date_format()`
- **Error Type**: `date_format`
- **Example**: `2023-12-25` (valid) vs `2023/12/25` (invalid)

## 2. Time Format Validation
- **Rule**: Start and end times must follow the `HH:MM` 24-hour format
- **Validation Method**: `validate_time_format()`
- **Error Type**: `time_format`
- **Example**: `09:30` (valid) vs `9:30` (invalid)

## 3. Duration Format Validation
- **Rule**: Duration must follow specific patterns: `Xh`, `Ym`, or `XhYm`
- **Validation Method**: `validate_duration_format()`
- **Error Type**: `duration_format`
- **Valid Examples**: `1h`, `30m`, `1h30m`, `2h45m`
- **Invalid Examples**: `1.5h`, `90`, `1h30`

## 4. Duration Calculation Consistency
- **Rule**: Recorded duration must match calculated duration from start/end times
- **Validation Method**: `calculate_duration()` comparison
- **Error Type**: `duration_mismatch`
- **Note**: Handles cross-midnight scenarios (end time < start time)

## 5. Project Name Format Validation
- **Rule**: Project names must contain only alphanumeric characters, spaces, hyphens, apostrophes, and parentheses
- **Validation Method**: `validate_project_name()`
- **Error Type**: `project_name`
- **Valid Examples**: `game-hub`, `Programista operator frezarki CNC`, `Project (Phase 1)`
- **Invalid Examples**: `Project@Home`, `Task#123`

## 6. Notes Content Validation
- **Rule**: Notes lines should not be empty if they exist
- **Validation Method**: `validate_notes()`
- **Error Type**: `notes_format`
- **Note**: Removed strict capitalization requirement, only checks for non-empty content

## 7. Log Entry Structure Validation
- **Rule**: Proper entry structure with date, time range, duration, and project name
- **Validation Method**: Parsing logic in `parse_log_file()`
- **Note**: Handles continuation lines as notes for the previous entry

## 8. Cross-Midnight Time Handling
- **Rule**: Properly calculates duration when end time is earlier than start time (crossing midnight)
- **Validation Method**: `calculate_duration()` with timedelta adjustment

## 9. Error Reporting Options
- **First Error Only**: Stop at first validation error with `--first` flag
- **Complete Report**: Generate full error list with Markdown formatting using `--output`
- **CLI Output**: Default command-line error display with detailed context

## 10. File Handling
- **Rule**: Validates file existence before processing
- **Validation Method**: Path existence check in `main()`
- **Error Handling**: Proper exit codes (0 for success, 1 for errors)

The script provides comprehensive validation for productivity log entries while maintaining flexibility for various project naming conventions and handling edge cases like overnight work sessions.