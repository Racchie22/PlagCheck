"""Streamlit interface for the PlagCheck text comparison flow."""

import streamlit as st

from modules.matching import find_matching_sentences
from modules.similarity import calculate_similarity

st.set_page_config(page_title="PlagCheck", page_icon="🔎", layout="wide")

st.title("PlagCheck")
st.caption("Text similarity checker")

st.write(
    "Compare two text samples and inspect how much wording they have in common. "
    "The result is a similarity indicator, not a final plagiarism judgement."
)

with st.form("comparison_form"):
    left, right = st.columns(2)
    with left:
        text_a = st.text_area(
            "Text sample 1",
            height=260,
            placeholder="Paste the first text here...",
        )
    with right:
        text_b = st.text_area(
            "Text sample 2",
            height=260,
            placeholder="Paste the second text here...",
        )

    submitted = st.form_submit_button("Compare texts", type="primary", use_container_width=True)

if submitted:
    if not text_a.strip() or not text_b.strip():
        st.error("Please enter text in both boxes before comparing.")
    else:
        try:
            score = calculate_similarity(text_a, text_b)
            st.subheader("Comparison result")
            st.metric("Text similarity", f"{score:.2f}%")
            st.progress(int(round(score)))
            st.write(
                "This percentage represents textual similarity based on TF-IDF and "
                "cosine similarity. It does not prove that plagiarism has occurred. "
                "Common phrases, quotations, references and document context should "
                "be considered when interpreting the result."
            )

            st.subheader("Matching sentences")
            matches = find_matching_sentences(text_a, text_b)
            if matches:
                st.caption(
                    "Showing sentence pairs with at least 50% similarity. "
                    "Each sentence from Text 1 is paired with its closest match in Text 2."
                )
                for index, match in enumerate(matches, start=1):
                    with st.container(border=True):
                        st.markdown(
                            f"**Match {index} — {match['similarity']:.2f}% similar**"
                        )
                        st.markdown("**Text 1**")
                        st.write(match["sentence_a"])
                        st.markdown("**Text 2 — closest sentence**")
                        st.write(match["sentence_b"])
            else:
                st.info("No sentence pairs met the 50% similarity threshold.")
        except (TypeError, ValueError) as error:
            st.error(str(error))

st.divider()
st.caption("Sprint 1: text comparison and similarity score | Sprint 2: sentence-level matching.")
