# Project (Labs 2–6)

## Project Description

This project develops a BlockProcessor system that handles incoming blocks and votes, constructing a valid chain according to predefined rules.

Across Labs 2–6, the system gradually progresses from basic CSV input handling to a complete event-driven architecture powered by SQLite.

The project showcases:

- Interaction with SQLite databases
- Organized Python design using classes
- Event-driven data processing (event_stream)
- Data validation with Pydantic
- Testing using Pytest

## Features

- Load data from CSV files or accept it via user input
- Store and handle data within an SQLite database
- Process events through the event_stream mechanism
- Create and maintain a valid block chain
- Validate data using Pydantic and perform testing with Pytest

## Core Entities

- Block — main data unit
- Vote — voting records
- Person — users
- Source — data sources

flowchart TD

A[Start] --> B[Load CSV files]
B --> C[Updater inserts data into SQLite]

C --> D[Database SQLite]

D --> E[BlockProcessor]
E --> F[Load Blocks]
E --> G[Load Votes]
E --> H[Load Persons]
E --> I[Load Sources]

F --> J[Validate and Process Data]
G --> J
H --> J
I --> J

J --> K[Build Valid Chain]
K --> L[Generate Results]
L --> M[Output]

M --> N[End]



## Notes
- The database is saved locally in lab3.db 
- The system can be easily expanded (for example, by adding an API or a user interface)

## Author
Tolochanov Maksym
