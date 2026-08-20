"""
Methodology-aware analytical utilities.

This module applies a resolved protocol methodology to
already-normalized protocol metrics.

It does not:
- discover sources,
- resolve methodologies,
- normalize raw data,
- calculate protocol TVL independently.

Those responsibilities belong to other modules.
"""


def apply_methodology(normalized_data, methodology):
    """
    Apply methodology rules to normalized protocol metrics.

    Args:
        normalized_data (list[dict]):
            Normalized protocol metrics.

        methodology (dict):
            Resolved methodology definition.

            Expected structure:

            {
                "name": str,
                "include_metric_types": list[str]
            }

    Returns:
        list[dict]:
            Analytical records containing the original metric
            information plus the methodology decision.
    """

    include_metric_types = methodology.get(
        "include_metric_types",
        [],
    )

    results = []

    for record in normalized_data:

        metric_type = record["metric_type"]

        included = metric_type in include_metric_types

        result = record.copy()

        result["methodology_included"] = included

        results.append(result)

    return results


def calculate_methodology_tvl(
    normalized_data,
    methodology,
):
    """
    Calculate TVL according to a resolved methodology.

    Args:
        normalized_data (list[dict]):
            Normalized protocol metrics.

        methodology (dict):
            Resolved methodology definition.

    Returns:
        float:
            TVL calculated according to the methodology.
    """

    analyzed_data = apply_methodology(
        normalized_data,
        methodology,
    )

    total_tvl = 0.0

    for record in analyzed_data:

        if not record["methodology_included"]:
            continue

        total_tvl += record["value"]

    return total_tvl
