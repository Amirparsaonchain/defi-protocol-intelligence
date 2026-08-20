"""
Methodology prompt utilities.

This module builds the instruction used by the future AI
methodology interpreter.

It does not call an AI provider.
It does not calculate TVL.
It does not perform protocol analysis.

Its responsibility is to define the interpretation contract
between methodology evidence and the AI interpreter.
"""


def build_methodology_prompt(evidence):
    """
    Build an AI methodology interpretation prompt.

    Args:
        evidence (dict):
            Structured methodology evidence.

    Returns:
        str:
            Prompt containing the evidence and interpretation rules.

    Raises:
        ValueError:
            If required evidence fields are missing.
    """

    required_fields = [
        "protocol",
        "source",
        "content",
    ]

    for field in required_fields:
        if field not in evidence:
            raise ValueError(
                f"Missing evidence field: {field}"
            )

    protocol = evidence["protocol"]
    source = evidence["source"]
    content = evidence["content"]

    return f"""
You are a DeFi protocol methodology analyst.

Your task is to determine the protocol's methodology
from the provided official source evidence.

Protocol:
{protocol}

Source type:
{source["type"]}

Source URL:
{source["url"]}

Official source evidence:
---
{content}
---

Rules:

1. Use the provided source evidence as the primary basis
   for your conclusions.

2. Do not invent methodology rules that are not supported
   by the evidence.

3. Distinguish explicitly stated facts from reasonable
   interpretation.

4. Identify which metrics are included in the protocol's
   methodology.

5. Identify which metrics are excluded.

6. Describe the aggregation logic when it is supported
   by the evidence.

7. Preserve the source information so that every methodology
   conclusion remains traceable to its origin.

8. If the evidence is insufficient to determine a rule,
   explicitly state that the rule is unknown rather than
   guessing.

Return a structured methodology specification containing:

- protocol
- source
- claims
- included_metrics
- excluded_metrics
- aggregation_logic
- confidence

The resulting specification must be suitable for validation
by a deterministic software layer.
""".strip()
