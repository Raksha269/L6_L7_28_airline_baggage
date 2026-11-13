### Observations

1. Hypothesis was used to generate random input values, including empty strings, malformed strings, and `None` values.
2. Initially, all three fuzz tests failed due to insufficient input validation.
3. The `parse_booking()` function raised `ValueError` and `AttributeError` for invalid booking codes.
4. The `total_weight()` function raised `ValueError` and `AttributeError` when processing invalid baggage weights.
5. The `tag_label()` function raised `IndexError` and `AttributeError` for invalid passenger names.
6. Input validation and exception handling were added to prevent these failures.
7. After correcting the code, all three Hypothesis tests passed.
8. The corrected application successfully processed valid booking information, baggage weights, and passenger names.

### Conclusion

The experiment demonstrated how fuzz testing can identify input-validation vulnerabilities in Python applications. Hypothesis successfully discovered multiple failure cases that could cause the original application to crash. After implementing input validation and defensive error handling, all three fuzz tests passed, confirming improved robustness against the tested inputs.
