# Monitoring

## Description

This Python apps does snapshot of system information every given time interval and  writes to the log file.

## Installation

pip install `devoups_lab/monitoring-1.0-py3-none-any.whl`

## HowTo

### import

`import monitoring.monitoring` \
`import monitoring.monitoring as monitoring` \

### Settings
Function `set_interval(int)` - set interval to do a snapshot (min) \
Function `set_file_name(str)` - set file name \
Function `set_file_type(str)` - set file type \

### Running

Function `run()`

## Example

### program

`import monitoring.monitoring `

`monitoring.monitoring.set_interval(1) ` \
`monitoring.monitoring.set_file_type('json') ` \
`monitoring.monitoring.run() ` \

### json output file

{ \
    "Snapshot 1": { \
        "timestamp": "Sat Jun 22 10:31:01 2019", \
        "cpu": { \
            "percent": 0.0, \
            "load_average_for_1_minute": 0.35, \
            "load_average_for_5_minutes": 0.46, \
            "load_average_for_10_minutes": 0.6 \
        }, \
        "physical memory": { \
            "/": { \
                "total": "46677.73 Mb", \
                "used": "26835.39 Mb", \
                "free": "17442.19 Mb" \
            }, \
            "/home": { \
                "total": "308748.13 Mb", \
                "used": "97644.28 Mb", \
                "free": "195352.26 Mb" \
            } \
        }, \
        "virtual_memory": { \
            "total": "7861.55 Mb", \
            "used": "2660.49 Mb", \
            "free": "3470.96 Mb" \
        }, \
...

### plain output file

Snapshot 1: \
timestamp Sat Jun 22 10:19:29 2019; \
cpu: {'percent': 7.7, 'load_average_for_1_minute': 0.39, 'load_average_for_5_minutes': 1.14, 'load_average_for_10_minutes': 0.74}; \
...
