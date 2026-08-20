from src.methodology import (
    SourceEvidence,
    MetricRule,
    Methodology,
)


def test_source_evidence():

    source = SourceEvidence(
        source_type="repository",
        title="Aave V3 Repository",
        url="https://github.com/aave",
        authority="official",
        evidence="Contains official protocol implementation.",
    )

    assert source.source_type == "repository"
    assert source.authority == "official"


def test_metric_rule():

    rule = MetricRule(
        metric_type="borrowed",
        included_in_tvl=False,
        description="Borrowed assets are excluded from TVL.",
    )

    assert rule.metric_type == "borrowed"
    assert rule.included_in_tvl is False


def test_methodology_creation():

    methodology = Methodology(
        protocol_name="Aave V3",
        official_repository="https://github.com/aave",
        confidence="high",
    )

    assert methodology.protocol_name == "Aave V3"
    assert methodology.official_repository == "https://github.com/aave"
    assert methodology.confidence == "high"


def test_get_metric_rule():

    chain_rule = MetricRule(
        metric_type="chain",
        included_in_tvl=True,
    )

    borrowed_rule = MetricRule(
        metric_type="borrowed",
        included_in_tvl=False,
    )

    methodology = Methodology(
        protocol_name="Aave V3",
        metric_rules={
            "chain": chain_rule,
            "borrowed": borrowed_rule,
        },
    )

    assert methodology.get_metric_rule("chain") == chain_rule
    assert methodology.get_metric_rule("borrowed") == borrowed_rule
    assert methodology.get_metric_rule("unknown") is None


def test_is_metric_included():

    methodology = Methodology(
        protocol_name="Aave V3",
        metric_rules={
            "chain": MetricRule(
                metric_type="chain",
                included_in_tvl=True,
            ),
            "borrowed": MetricRule(
                metric_type="borrowed",
                included_in_tvl=False,
            ),
        },
    )

    assert methodology.is_metric_included("chain") is True
    assert methodology.is_metric_included("borrowed") is False
    assert methodology.is_metric_included("unknown") is False
