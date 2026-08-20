from dataclasses import dataclass, field


@dataclass(frozen=True)
class SourceEvidence:
    """
    Represent an authoritative source used to support a methodology.

    Args:
        source_type (str):
            Type of source, such as "repository" or "documentation".

        title (str):
            Human-readable source title.

        url (str):
            URL of the source.

        authority (str):
            Authority classification of the source.

        evidence (str):
            Short description of what the source supports.
    """

    source_type: str
    title: str
    url: str
    authority: str
    evidence: str


@dataclass(frozen=True)
class MetricRule:
    """
    Define how a metric should be treated during TVL calculation.

    Args:
        metric_type (str):
            Metric category, such as "chain" or "borrowed".

        included_in_tvl (bool):
            Whether the metric contributes to TVL.

        description (str):
            Explanation of the rule.
    """

    metric_type: str
    included_in_tvl: bool
    description: str = ""


@dataclass
class Methodology:
    """
    Represent the structured methodology of a DeFi protocol.

    This object is designed to separate methodology discovery
    from deterministic data processing.

    Args:
        protocol_name (str):
            Name of the protocol.

        official_repository (str | None):
            Official repository URL when available.

        sources (list[SourceEvidence]):
            Evidence supporting the methodology.

        metric_rules (dict[str, MetricRule]):
            Rules describing how protocol metrics are treated.

        special_cases (list[str]):
            Protocol-specific exceptions or special handling rules.

        confidence (str):
            Confidence level of the methodology specification.
    """

    protocol_name: str
    official_repository: str | None = None
    sources: list[SourceEvidence] = field(default_factory=list)
    metric_rules: dict[str, MetricRule] = field(default_factory=dict)
    special_cases: list[str] = field(default_factory=list)
    confidence: str = "unknown"

    def get_metric_rule(self, metric_type):
        """
        Return the rule associated with a metric type.

        Args:
            metric_type (str):
                Metric category to look up.

        Returns:
            MetricRule | None:
                Matching rule, or None when no rule exists.
        """

        return self.metric_rules.get(metric_type)

    def is_metric_included(self, metric_type):
        """
        Determine whether a metric type contributes to TVL.

        Args:
            metric_type (str):
                Metric category to evaluate.

        Returns:
            bool:
                True when the methodology includes the metric.
        """

        rule = self.get_metric_rule(metric_type)

        if rule is None:
            return False

        return rule.included_in_tvl
