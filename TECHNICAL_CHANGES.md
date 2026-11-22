# Technical Changes

## Overview

The report generator was refactored to improve pagination, table readability,
load-report structure, design-check visualization, material summaries, and
global formatting consistency.

## Key Code and LaTeX/PyLaTeX Changes

### Table pagination and repeated headers

- Dynamic report tables use LaTeX `longtable` markup.
- Repeated header blocks are added with `\endfirsthead` and `\endhead`.
- Existing explicit longtable headers are preserved.
- `\needspace`, `\raggedbottom`, widow/orphan penalties, and controlled
  table spacing reduce page-bottom collisions.
- Header height, footer separation, row stretch, cell padding, and rule
  thickness are applied consistently through the report preamble.

### Chapter 3 load tables

- Vehicle live loads and footway live loads are now separate tables.
- Vehicle rows are generated from the existing GUI selection keys.
- Standard and custom vehicles can report total load, impact factor, braking
  state/value, and eccentricity.
- Internal Newton-based IRC vehicle values are converted to kN before display.
- Footway pressure is reported with its unit and IRC reference.

### Utilization and quantity charts

- Matplotlib generates a utilization-ratio chart for:
  - Steel plate girders
  - Concrete deck slab
  - Cross bracing
  - End diaphragms
- A red dashed `UR = 1.0` reference line distinguishes passing and failing
  checks.
- Material charts summarize structural steel, concrete, and reinforcement
  quantities.
- Charts are written to temporary image assets and embedded in LaTeX figures.
- Missing values are shown as `N/A` rather than being treated as passing.

## Files Altered

- [`src/osdagbridge/core/reports/report_generator.py`](src/osdagbridge/core/reports/report_generator.py)
  - Central report assembly, LaTeX preamble, longtable processing, chart
    generation, and chart embedding.
- [`src/osdagbridge/core/reports/chap3.py`](src/osdagbridge/core/reports/chap3.py)
  - Separate vehicle/footway tables and corrected vehicle-load unit handling.
- [`src/osdagbridge/core/reports/chap5.py`](src/osdagbridge/core/reports/chap5.py)
  - Utilization chart placement in Section 5.5.
- [`src/osdagbridge/core/reports/chap7.py`](src/osdagbridge/core/reports/chap7.py)
  - Material quantity chart placement.
- [`src/osdagbridge/core/boq/boq_generator.py`](src/osdagbridge/core/boq/boq_generator.py)
  - End-diaphragm quantity calculation for the material take-off.
- [`src/osdagbridge/core/reports/styles.py`](src/osdagbridge/core/reports/styles.py)
  - Centralized page, typography, color, table, and plot configuration.

## Centralized Formatting Configuration

[`styles.py`](src/osdagbridge/core/reports/styles.py) is the single source of
truth for report presentation settings. It defines immutable dataclasses for:

- `ReportPageStyle`: paper size, margins, header dimensions, and footer skip.
- `ReportTypographyStyle`: body, chapter, section, table, and figure sizes.
- `ReportColorStyle`: primary, secondary, table, border, pass, and fail colors.
- `ReportTableStyle`: cell padding, row stretch, row height, rule width, and
  page-bottom thresholds.
- `ReportPlotStyle`: chart dimensions, DPI, threshold, colors, and label sizes.

The exported style instances are consumed by the report generator and chapter
modules instead of duplicating formatting constants.

## Architectural and Styling Rationale

- Raw LaTeX chapter generators are retained because the existing report
  architecture produces LaTeX strings rather than native PyLaTeX trees.
- `longtable` is used only where tables may span pages; small fixed tables
  remain unchanged.
- Formatting values are centralized to make global visual changes safe and
  predictable.
- Temporary chart assets prevent generated images from accumulating beside
  final reports.
- Separate quantity chart axes avoid comparing incompatible units such as
  concrete volume in m³ with steel weight in MT.
- Existing design-result and BOQ data sources are reused to keep report values
  consistent with the engineering calculations.

## Visual Enhancements and Open Polish

Implemented visual improvements include:

- Consistent A4 page geometry and header/footer spacing.
- More readable table padding and row height.
- Consistent heading hierarchy and typography.
- Green report branding with coordinated table and chart colors.
- Clear pass/fail utilization visualization.
- Improved chart labels, legends, threshold lines, and missing-data markers.
- Separate, clearly titled Chapter 3 live-load tables.
- End-diaphragm quantities included in the material summary.

The generated PDF has been validated with the supported Python 3.12,
OpenSees, and LaTeX environment. Unit and integration tests pass. A minor
remaining presentation item is the logical footer page count: the PDF may
contain one more physical page than the number shown in the footer because of
the title/contents page numbering arrangement.
