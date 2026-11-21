
import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

from src.conversation import Conversation
from src.llm_client import generate_reply, LLMRequestError
from src.usage import estimate_usage, calculate_provider_cost


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="LLM Chat Lab",
    page_icon="💬",
    layout="centered",
)

st.title("💬 LLM Chat Lab")

st.caption(
    "Task 3 · LLM APIs & Application Development · Demo-ready / deployable"
)

st.info(
    "Demo Mode works without an API key. "
    "To make this a public website, deploy this repository "
    "to Streamlit Community Cloud."
)


# --------------------------------------------------
# SIDEBAR SETTINGS
# --------------------------------------------------

with st.sidebar:

    st.header("Settings")

    demo_mode = st.toggle(
        "Demo Mode (offline)",
        value=os.getenv("DEMO_MODE", "true").lower() == "true",
    )

    model = st.text_input(
        "Model",
        value=os.getenv("LLM_MODEL", "gpt-4o-mini"),
    )

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
    )

    max_tokens = st.slider(
        "Max response tokens",
        min_value=50,
        max_value=2000,
        value=500,
        step=50,
    )

    json_mode = st.checkbox(
        "Request JSON response format"
    )

    custom_instructions = st.text_area(
        "Custom instructions",
        value="You are a helpful, concise assistant.",
        height=120,
    )

    if st.button(
        "Clear conversation",
        use_container_width=True,
    ):

        st.session_state.conversation = Conversation(
            custom_instructions
        )

        st.session_state.usage_rows = []

        st.rerun()


# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------

if "conversation" not in st.session_state:

    st.session_state.conversation = Conversation(
        custom_instructions
    )


if "usage_rows" not in st.session_state:

    st.session_state.usage_rows = []


# Update system instructions without losing conversation history.

st.session_state.conversation.replace_system_prompt(
    custom_instructions
)


# --------------------------------------------------
# DISPLAY EXISTING CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.conversation.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

prompt = st.chat_input("Ask something...")


if prompt:

    conversation = st.session_state.conversation

    conversation.add_user(prompt)


    # Display user message.

    with st.chat_message("user"):

        st.markdown(prompt)


    # Generate assistant response.

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                reply, meta = generate_reply(
                    conversation.api_messages(),
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    json_mode=json_mode,
                    demo_mode=demo_mode,
                )


                # --------------------------------------------------
                # DISPLAY AI RESPONSE
                # --------------------------------------------------

                st.markdown(reply)

                conversation.add_assistant(reply)


                # --------------------------------------------------
                # PRICING CONFIGURATION
                # --------------------------------------------------

                input_rate = float(
                    os.getenv(
                        "INPUT_COST_PER_1K",
                        "0.00015",
                    )
                )

                output_rate = float(
                    os.getenv(
                        "OUTPUT_COST_PER_1K",
                        "0.00060",
                    )
                )


                # --------------------------------------------------
                # LIVE PROVIDER USAGE AND COST
                # --------------------------------------------------

                if meta.get("usage"):

                    usage = meta["usage"]

                    provider_input_tokens = usage[
                        "prompt_tokens"
                    ]

                    provider_output_tokens = usage[
                        "completion_tokens"
                    ]

                    provider_total_tokens = usage[
                        "total_tokens"
                    ]


                    # Calculate cost from actual provider token counts.

                    estimate = calculate_provider_cost(
                        input_tokens=provider_input_tokens,
                        output_tokens=provider_output_tokens,
                        input_rate_per_1k=input_rate,
                        output_rate_per_1k=output_rate,
                    )


                    # Display actual provider usage.

                    st.caption(
                        f"Provider usage: "
                        f"{provider_total_tokens} tokens "
                        f"({provider_input_tokens} prompt · "
                        f"{provider_output_tokens} completion)"
                    )


                    # Display estimated live API cost.

                    st.caption(
                        f"Estimated API cost: "
                        f"${estimate.estimated_cost_usd:.8f}"
                    )


                # --------------------------------------------------
                # ESTIMATED TOKEN USAGE AND COST
                # DEMO MODE / PROVIDER USAGE UNAVAILABLE
                # --------------------------------------------------

                else:

                    estimate = estimate_usage(
                        prompt,
                        reply,
                        input_rate,
                        output_rate,
                    )


                    st.caption(
                        f"Estimated tokens: "
                        f"{estimate.total_tokens} "
                        f"(input: {estimate.input_tokens} · "
                        f"output: {estimate.output_tokens})"
                    )


                    st.caption(
                        f"Approx. cost: "
                        f"${estimate.estimated_cost_usd:.8f}"
                    )


                # --------------------------------------------------
                # MODE INDICATOR
                # --------------------------------------------------

                if meta.get("demo"):

                    st.caption("Demo mode · Simulated response")

                else:

                    st.caption("Live API · Provider usage reported")


                # --------------------------------------------------
                # SAVE USAGE HISTORY
                # --------------------------------------------------

                usage_row = {
                    "input_tokens": estimate.input_tokens,
                    "output_tokens": estimate.output_tokens,
                    "total_tokens": estimate.total_tokens,
                    "estimated_cost_usd": estimate.estimated_cost_usd,
                    "mode": (
                        "Demo"
                        if meta.get("demo")
                        else "Live API"
                    ),
                }

                st.session_state.usage_rows.append(
                    usage_row
                )


            # --------------------------------------------------
            # API ERROR HANDLING
            # --------------------------------------------------

            except LLMRequestError as exc:

                st.error(str(exc))

                # Remove the failed user message
                # from the conversation history.

                conversation.messages.pop()


            # --------------------------------------------------
            # GENERAL ERROR HANDLING
            # --------------------------------------------------

            except Exception:

                st.error(
                    "Unexpected error. Please check settings and try again."
                )

                # Remove failed message from history.

                conversation.messages.pop()


# --------------------------------------------------
# USAGE SUMMARY
# --------------------------------------------------

if st.session_state.usage_rows:

    st.subheader("📊 Usage Summary")

    st.caption(
        "Recent token usage and estimated costs."
    )

    st.json(
        st.session_state.usage_rows[-5:]
    )
