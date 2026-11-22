from dataclasses import dataclass


@dataclass(frozen=True)
class ReportPageStyle:
    paper: str = "a4paper"
    left_in: float = 0.75
    right_in: float = 0.75
    top_in: float = 0.78
    bottom_in: float = 0.82
    head_height: float = 14.0
    head_sep: float = 10.0
    foot_skip: float = 18.0


@dataclass(frozen=True)
class ReportTypographyStyle:
    body_pt: int = 12
    chapter_pt: int = 17
    section_pt: int = 14
    subsection_pt: int = 12
    table_pt: int = 10
    figure_pt: int = 9


@dataclass(frozen=True)
class ReportColorStyle:
    primary: str = "#91B014"
    secondary: str = "#4C78A8"
    table_header: str = "#E7EDE0"
    border: str = "#7A7A7A"
    passing: str = "#2E7D32"
    failing: str = "#D62728"


@dataclass(frozen=True)
class ReportTableStyle:
    column_padding_pt: float = 5.0
    row_stretch: float = 1.08
    extra_row_height_pt: float = 0.4
    rule_width_pt: float = 0.5
    pre_skip_pt: float = 0.0
    post_skip_pt: float = 4.0
    min_remaining_baselines: int = 6


@dataclass(frozen=True)
class ReportPlotStyle:
    dpi: int = 200
    figure_width_in: float = 7.2
    utilization_height_in: float = 3.8
    quantity_height_in: float = 3.8
    threshold: float = 1.0
    threshold_color: str = "#D62728"
    steel_color: str = "#91B014"
    concrete_color: str = "#4C78A8"
    rebar_color: str = "#F58518"
    pass_color: str = "#2E7D32"
    fail_color: str = "#D62728"
    missing_color: str = "#A0A0A0"
    title_pt: int = 11
    label_pt: int = 10
    tick_pt: int = 9
    legend_pt: int = 9


PAGE_STYLE = ReportPageStyle()
TYPOGRAPHY_STYLE = ReportTypographyStyle()
COLOR_STYLE = ReportColorStyle()
TABLE_STYLE = ReportTableStyle()
PLOT_STYLE = ReportPlotStyle()
OSDAG_GREEN = COLOR_STYLE.primary
