# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.9.4] - 2026-03-19
### Changed
- Moved package metadata (`__version__`, `__author__`, `__maintainer__`, `__email__`, `__date__`, `__update__`) from `DynaTMT.py` to `__init__.py`.
- Updated Jupyter notebooks to import `DynaTMT` package directly for version reporting (`DynaTMT.__version__` instead of `mePROD.__version__`).

## [2.9.3] - 2026-03-18
### Updated
- Repository renamed from `DynaTMT-py-SB` / `DynaTMT-py` to `DynaTMT`. All references in code, documentation, and URLs updated accordingly.
- Default branch renamed from `master` to `main`.
- `baseline_correction()` function (both `PD_input` and `plain_text_input` classes):
  - PSM/Peptide file detection is now case-insensitive (`.lower()` comparison) to handle column name variations across ProteomeDiscoverer versions.
  - Added support for **Proteome Discoverer 3.2** column names alongside existing PD 2.4 columns (backward compatible):
    - PSMs: additionally checks for `Identifying Node Type`, `Identifying Node`, or `Search ID` columns (PD 3.2), in addition to `PSMs Peptide ID` (PD 2.4).
    - Peptides: additionally checks for `Number of PSMs` column (PD 3.2), in addition to `Peptide Group ID` (PD 2.4).

## [2.9.2] - 2024-06-03
### Updated
- `baseline_correction()` function:
  - Fixed an issue where the `Random=False` part was yielding an error.

## [2.9.1] - 2024-03-08
### Updated
- `filter_PSMs()` and `filter_peptides()` functions:
  - Changed the order of filtering; removal of any TMT channels with at least one NA value is now performed at the end.

## [2.9.0] - 2024-03-06
### Updated
- `filter_PSMs()` and `filter_peptides()` functions with several enhancements:
  - Updates in `filter_PSMs`:
    - Removed filtering for TMT channels with at least one NA value.
    - Other filtering criteria remain unchanged.
  - Updates in `filter_peptides`:
    - Removed filtering for TMT channels with at least one NA value.

## [2.8.5] - 2024-02-06
### Added
- `PSMs_to_Peptide()` function:
  - Separates the functionality from `baseline_correction` for merging PSMs into peptides using specified columns.
  - Auto-detects 'Theo. MH+ [Da]' column using regular expressions even if the name does not fully match.

## [2.8.4] - 2024-01-18
### Updated
- The script now supports PSMs and Peptide file processing for both MS2 and MS3 measurements across both `PD_input` and `plain_text_input` classes.
- `filter_peptides()` function now specifically works for peptide files.
- Added `filter_PSMs()` function for PSM files, removing isolation interference > 50%.
- Updated `extract_heavy()` and `extract_light()` functions to support a broader range of labels.
- Major updates to `baseline_correction()` function:
  - New usage parameters and functionality adjustments.
  - Improved baseline correction process and integration with PSM and Peptides file identification.

## [2.7.0] - 2023-12-05
### Updated
- `filter_peptides()` function:
  - Enhanced to remove sum of intensities equal to 0.
  - Now converts NaN values to 0 for cleaner data handling.