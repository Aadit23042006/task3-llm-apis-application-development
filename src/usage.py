
from dataclasses import dataclass
from typing import Optional


@dataclass
class UsageEstimate:
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_cost_usd: float


def estimate_tokens(text: str) -> int:
    """
    Estimate tokens using a lightweight character-based heuristic.

    This is NOT an exact tokenizer. Actual provider token counts
    may differ depending on the model and text.
    """
    if not text:
        return 0

    return max(1, (len(text) + 3) // 4)


def estimate_usage(
    prompt: str,
    response: str,
    input_rate_per_1k: float = 0.00015,
    output_rate_per_1k: float = 0.00060,
) -> UsageEstimate:
    """
    Estimate token usage and API cost from text.

    Used primarily when provider usage data is unavailable,
    such as in Demo Mode.

    Args:
        prompt: Input text sent to the model.
        response: Generated response text.
        input_rate_per_1k: Estimated cost per 1,000 input tokens.
        output_rate_per_1k: Estimated cost per 1,000 output tokens.

    Returns:
        UsageEstimate containing estimated token counts and cost.
    """

    if input_rate_per_1k < 0 or output_rate_per_1k < 0:
        raise ValueError("Token pricing rates cannot be negative.")

    input_tokens = estimate_tokens(prompt)
    output_tokens = estimate_tokens(response)

    total_tokens = input_tokens + output_tokens

    input_cost = (
        input_tokens / 1000
    ) * input_rate_per_1k

    output_cost = (
        output_tokens / 1000
    ) * output_rate_per_1k

    total_cost = input_cost + output_cost

    return UsageEstimate(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        estimated_cost_usd=round(total_cost, 8),
    )


def calculate_provider_cost(
    input_tokens: int,
    output_tokens: int,
    input_rate_per_1k: float = 0.00015,
    output_rate_per_1k: float = 0.00060,
) -> UsageEstimate:
    """
    Calculate estimated API cost using provider-reported token counts.

    Unlike estimate_usage(), this function does not estimate
    token counts from text. It uses the actual token counts
    returned by the API provider.

    Note:
        The calculated cost is still an estimate. Pricing rates
        must match the provider, model, and applicable billing tier.
    """

    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Token counts cannot be negative.")

    if input_rate_per_1k < 0 or output_rate_per_1k < 0:
        raise ValueError("Token pricing rates cannot be negative.")

    total_tokens = input_tokens + output_tokens

    input_cost = (
        input_tokens / 1000
    ) * input_rate_per_1k

    output_cost = (
        output_tokens / 1000
    ) * output_rate_per_1k

    total_cost = input_cost + output_cost

    return UsageEstimate(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        estimated_cost_usd=round(total_cost, 8),
    )


def format_cost(cost_usd: float) -> str:
    """
    Format estimated API cost for display.
    """
    if cost_usd < 0:
        raise ValueError("Cost cannot be negative.")

    return f"${cost_usd:.8f}"
