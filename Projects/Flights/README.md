# Flights Dataset

## Main Table: `flights`

**File:** `flights.csv`

- 20,000 rows
- 5 columns
- One row represents one flight.

**Columns:**
- Date and time
- Delay (in minutes)
- Distance (unit not specified in the file)
- Origin (airport code)
- Destination (airport code)

## Second Table: `airports`

**File:** `airports.csv`

- 3,376 airports
- Contains:
  - Airport code (`iata`)
  - Airport name
  - City
  - State
  - Country
  - Geographic position

## Merge

Merge the two tables using the airport code (`iata`).

## Questions to Start With

1. **Flight delays**
   - Which airports, hours, or weekdays have the worst delays?
   - What does the mean hide?

2. **Flight distance**
   - Does a longer flight mean a longer delay?

3. **Time period**
   - Which period does the data cover?
   - What does that mean for your conclusions?