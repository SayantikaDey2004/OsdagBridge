# PDF Report Generator Refactoring

## Files modified

- `src/osdagbridge/core/reports/styles.py`
- `src/osdagbridge/core/reports/report_generator.py`
- `src/osdagbridge/core/reports/chap3.py`
- `src/osdagbridge/core/reports/chap5.py`
- `src/osdagbridge/core/reports/chap7.py`
- `src/osdagbridge/core/boq/boq_generator.py`

## Files created

- `src/osdagbridge/core/reports/styles.py`
- `docs/report_generator_refactoring.md`

## Implemented changes

### LaTeX pagination and layout

- A `longtable` post-processing utility adds `\endfirsthead` and `\endhead`
  when headers are not already declared explicitly.
- Page geometry, header height, footer skip, table padding, row stretch,
  rule width, vertical row height, and minimum remaining page space are
  centralized in `styles.py`.
- `needspace`, `raggedbottom`, widow/orphan penalties, and footer/header
  spacing are used to reduce table and footer overlap.

### Chapter 3 loads

- Vehicle live loads are displayed in a dedicated table driven by the existing
  loading-tab keys.
- Selected standard vehicles and custom vehicles are read dynamically.
- Total vehicle load, impact factor, braking load, selection state, and
  eccentricity are shown in separate columns.
- Footway live pressure is displayed in a separate table.

### Section 5.5 utilization chart

- A Matplotlib bar chart is generated for steel plate girders, concrete deck
  slab, cross bracing, and end diaphragms.
- The chart uses the existing utilization keys and `design_results`,
  `deck_report_values`, cross-bracing efficiency, and end-diaphragm design
  results.
- Missing values are displayed as `N/A` rather than as passing values.
- A red dashed `UR = 1.0` threshold is included.

### Chapter 7 material chart

- A structural-steel tonnage chart uses the existing material take-off fields.
- A separate concrete/reinforcement visualization uses separate units.
- Chapter 7 also calculates an end-diaphragm tonnage contribution from existing
  end-diaphragm section properties and geometry.

### Centralized styling

`styles.py` now contains page, typography, color, table, and plot style data
classes. Report preamble geometry, table spacing, TOC heading typography,
chart dimensions, and chart colors consume these values.

## Validation performed

- Python syntax compilation passed for all modified report and BOQ modules.
- `git diff --check` passed.
- Chapter 3 vehicle/footway smoke test passed.
- `longtable` repeated-header smoke test passed.
- Matplotlib utilization and material chart smoke tests passed.
- `tests/unit/test_io.py`: `1 passed`.

## Manual verification still required

- Generate a complete PDF using the desktop GUI and inspect multi-page tables.
- Inspect the formerly problematic footer-area pages.
- Change GUI vehicle selections and confirm Chapter 3 updates.
- Confirm Section 5.5 and Chapter 7 charts against the calculated design data.
- Verify end-diaphragm quantity values for both cross-bracing and beam types.

The original PDF baseline was not available in the workspace, so
`Report_Before.pdf` could not be reproduced. No PDF was fabricated.
