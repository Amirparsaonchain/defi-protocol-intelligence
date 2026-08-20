Protocol:
Aave V3

Category:
Lending

TVL Definition:
Tokens locked in protocol contracts to be used as collateral
to borrow or to earn yield.

Excluded:
Borrowed coins.

Conceptual Formula:
TVL = Σ(eligible_token_balance × token_price)

Chain-Level Formula:
TVL(chain) =
Σ(eligible_token_balance(chain) × token_price)

Primary Risk:
Do not add borrowed values to TVL.

Validation:
Compare reconstructed TVL against DeFiLlama reference TVL.