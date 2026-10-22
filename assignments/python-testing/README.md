# 📘 Assignment: Testing Python Programs with pytest

## 🎯 Objective

Learn how to use pytest to verify Python functions and find defects. Build a focused test suite for a calculator module, then use failing tests to improve the module's behavior for normal and edge-case inputs.

## 📝 Tasks

### 🛠️ Write Unit Tests

#### Description

Complete the test file for the functions in `calculator.py`. Use pytest assertions to check expected results for normal inputs, and organize each behavior into a separate test function.

#### Requirements

Completed test suite should:

- Test `add`, `calculate_average`, `apply_discount`, and `split_bill` with representative inputs.
- Include at least six test functions with clear, descriptive names.
- Use pytest assertions to compare each function's result with an expected value.
- Run successfully with the command `pytest` before adding edge-case tests.

### 🛠️ Test Edge Cases and Fix Defects

#### Description

Add tests for invalid or boundary inputs, run the complete suite, and update `calculator.py` so that the implementation meets the behavior described by the tests.

#### Requirements

Completed program and test suite should:

- Verify that calculating an average for an empty list raises `ValueError`.
- Verify that splitting a bill for zero or a negative number of people raises `ValueError`.
- Verify that discounts are calculated as percentages, such as a 15% discount on 100 resulting in 85.
- Make all tests pass when `pytest` is run from the assignment directory.
- Keep the existing function names and parameters unchanged.