
"""Streamlit interface for the PlagCheck application."""

import streamlit as st
from pathlib import Path

from modules.document_reader import extract_text
from modules.document_store import (
    save_document,
    get_stored_documents,
    compare_with_collection,
)
from modules.matching import find_matching_sentences
from modules.similarity import calculate_similarity
from modules.history import save_comparison, get_history
from modules.report_generator import generate_pdf_report
from modules.dashboard import summarize_history


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PlagCheck",
    page_icon="🔎",
    layout="wide",
)

st.title("PlagCheck")
st.caption("Smart Plagiarism Detection System")

st.write(
    "Check textual similarity between text samples or uploaded documents. "
    "Similarity is an indicator of textual overlap, not proof of plagiarism."
)


# --------------------------------------------------
# APPLICATION TABS
# --------------------------------------------------

text_tab, document_tab, dashboard_tab, history_tab = st.tabs([
    "Text Comparison",
    "Document Comparison",
    "Dashboard",
    "Comparison History",
])


# --------------------------------------------------
# TEXT COMPARISON
# --------------------------------------------------

with text_tab:

    st.header("Compare Text Samples")

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

        submitted = st.form_submit_button(
            "Compare texts",
            type="primary",
            use_container_width=True,
        )

    if submitted:

        if not text_a.strip() or not text_b.strip():

            st.error("Please enter text in both boxes before comparing.")

        else:

            try:
                # Calculate overall similarity
                score = calculate_similarity(text_a, text_b)

                # Find matching sentences
                matches = find_matching_sentences(text_a, text_b)

                # Save comparison in SQLite history
                comparison_id = save_comparison(
                    comparison_type="Text",
                    source_name="Text Sample 1",
                    target_name="Text Sample 2",
                    similarity=score,
                    matches=matches,
                )

                st.success(
                    f"Comparison saved successfully! ID: {comparison_id}"
                )

                # Display comparison result
                st.subheader("Comparison result")

                st.metric(
                    "Text similarity",
                    f"{score:.2f}%",
                )

                st.progress(int(round(score)))

                st.write(
                    "This percentage represents textual similarity based "
                    "on TF-IDF and cosine similarity. It does not prove "
                    "that plagiarism has occurred."
                )

                # Display matching sentences
                st.subheader("Matching sentences")

                if matches:

                    st.caption(
                        "Showing sentence pairs with at least 50% similarity."
                    )

                    for index, match in enumerate(matches, start=1):

                        with st.container(border=True):

                            st.markdown(
                                f"**Match {index} — "
                                f"{match['similarity']:.2f}% similar**"
                            )

                            st.write("Text 1:")
                            st.write(match["sentence_a"])

                            st.write("Text 2:")
                            st.write(match["sentence_b"])

                else:

                    st.info(
                        "No sentence pairs met the 50% similarity threshold."
                    )

                # Generate downloadable PDF report
                report_bytes = generate_pdf_report(
                    comparison_type="Text",
                    source_name="Text Sample 1",
                    target_name="Text Sample 2",
                    similarity=score,
                    matches=matches,
                )

                st.download_button(
                    label="Download PDF Report",
                    data=report_bytes,
                    file_name="plagcheck_text_report.pdf",
                    mime="application/pdf",
                    key=f"text_report_{comparison_id}",
                    type="primary",
                )

            except (TypeError, ValueError) as error:

                st.error(str(error))


# --------------------------------------------------
# DOCUMENT COMPARISON
# --------------------------------------------------

with document_tab:

    st.header("Document Comparison")

    st.write(
        "Upload a document and compare it against documents "
        "previously added to the local collection."
    )

    # --------------------------------------------------
    # ADD DOCUMENTS TO COLLECTION
    # --------------------------------------------------

    st.subheader("1. Add documents to the collection")

    collection_uploads = st.file_uploader(
        "Select documents to store",
        type=["txt", "pdf", "docx"],
        accept_multiple_files=True,
        key="collection_uploads",
    )

    if st.button("Add to collection", key="add_documents"):

        if not collection_uploads:

            st.warning("Please select at least one document.")

        else:

            saved_count = 0

            for uploaded_file in collection_uploads:

                try:
                    saved_path = save_document(
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                    )

                    st.success(f"Added: {saved_path.name}")

                    saved_count += 1

                except (TypeError, ValueError) as error:

                    st.error(f"{uploaded_file.name}: {error}")

            if saved_count:

                st.info(
                    f"{saved_count} document(s) added to the collection."
                )

    st.divider()

    # --------------------------------------------------
    # COMPARE UPLOADED DOCUMENT
    # --------------------------------------------------

    st.subheader("2. Compare a document")

    comparison_file = st.file_uploader(
        "Upload the document you want to check",
        type=["txt", "pdf", "docx"],
        key="comparison_upload",
    )

    if st.button(
        "Compare against collection",
        type="primary",
        key="compare_documents",
    ):

        if comparison_file is None:

            st.warning("Please upload a document to compare.")

        else:

            try:
                # Extract uploaded document text
                uploaded_text = extract_text(
                    comparison_file.name,
                    comparison_file.getvalue(),
                )

                stored_documents = get_stored_documents()

                if not stored_documents:

                    st.warning(
                        "The document collection is empty. "
                        "Add some documents first."
                    )

                else:

                    # Compare against stored collection
                    results = compare_with_collection(uploaded_text)

                    if not results:

                        st.warning(
                            "No readable stored documents were available "
                            "for comparison."
                        )

                    else:

                        st.subheader("Comparison results")

                        st.metric(
                            "Documents compared",
                            len(results),
                        )

                        best_match = results[0]

                        st.success(
                            f"Closest match: {best_match['document_name']}"
                        )

                        st.metric(
                            "Highest similarity",
                            f"{best_match['similarity']:.2f}%",
                        )

                        # Calculate sentence matches and save
                        # every document comparison in history.
                        document_matches = {}

                        for result in results:

                            document_path = (
                                Path("data")
                                / "documents"
                                / result["document_name"]
                            )

                            stored_text = extract_text(
                                result["document_name"],
                                document_path.read_bytes(),
                            )

                            try:

                                matches = find_matching_sentences(
                                    uploaded_text,
                                    stored_text,
                                )

                            except (TypeError, ValueError):

                                matches = []

                            document_matches[
                                result["document_name"]
                            ] = matches

                            # Save individual comparison in history
                            save_comparison(
                                comparison_type="Document",
                                source_name=comparison_file.name,
                                target_name=result["document_name"],
                                similarity=result["similarity"],
                                matches=matches,
                            )

                        st.success(
                            f"Saved {len(results)} comparison(s) "
                            "to history."
                        )

                        # Display results and provide individual PDF reports
                        st.subheader("All document comparisons")

                        for index, result in enumerate(results, start=1):

                            document_name = result["document_name"]
                            matches = document_matches[document_name]

                            with st.container(border=True):

                                st.markdown(
                                    f"**{index}. {document_name}**"
                                )

                                st.metric(
                                    "Similarity",
                                    f"{result['similarity']:.2f}%",
                                )

                                # Generate PDF report
                                report_bytes = generate_pdf_report(
                                    comparison_type="Document",
                                    source_name=comparison_file.name,
                                    target_name=document_name,
                                    similarity=result["similarity"],
                                    matches=matches,
                                )

                                st.download_button(
                                    label="Download PDF Report",
                                    data=report_bytes,
                                    file_name=f"plagcheck_report_{index}.pdf",
                                    mime="application/pdf",
                                    key=f"document_report_{index}",
                                )

                        st.caption(
                            "Similarity scores are based on TF-IDF and "
                            "cosine similarity. They indicate textual "
                            "overlap, not proof of plagiarism."
                        )

                        # Display matches for closest document
                        st.subheader(
                            "Matching sentences with closest document"
                        )

                        matches = document_matches[
                            best_match["document_name"]
                        ]

                        if matches:

                            for index, match in enumerate(
                                matches,
                                start=1,
                            ):

                                with st.container(border=True):

                                    st.markdown(
                                        f"**Match {index} — "
                                        f"{match['similarity']:.2f}%**"
                                    )

                                    st.write(match["sentence_a"])
                                    st.write(match["sentence_b"])

                        else:

                            st.info(
                                "No sentence pairs met the "
                                "50% similarity threshold."
                            )

            except (TypeError, ValueError, OSError) as error:

                st.error(f"Document comparison failed: {error}")


# --------------------------------------------------
# DASHBOARD (US08)
# --------------------------------------------------

with dashboard_tab:

    st.header("Dashboard")

    st.write(
        "Overview of your PlagCheck comparison activity."
    )

    try:

        # Retrieve saved comparisons
        history = get_history()

        # Calculate dashboard statistics
        stats = summarize_history(history)

        if stats["total"] == 0:

            st.info(
                "No comparison data available yet. "
                "Perform a comparison to see dashboard statistics."
            )

        else:

            # ------------------------------------------
            # MAIN STATISTICS
            # ------------------------------------------

            st.subheader("Overall Statistics")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Total Comparisons",
                stats["total"],
            )

            col2.metric(
                "Average Similarity",
                f"{stats['average_similarity']:.2f}%",
            )

            col3.metric(
                "Highest Similarity",
                f"{stats['highest_similarity']:.2f}%",
            )

            col4.metric(
                "Lowest Similarity",
                f"{stats['lowest_similarity']:.2f}%",
            )

            st.divider()

            # ------------------------------------------
            # COMPARISON TYPE BREAKDOWN
            # ------------------------------------------

            st.subheader("Comparison Breakdown")

            type_col1, type_col2 = st.columns(2)

            with type_col1:

                st.metric(
                    "Text Comparisons",
                    stats["text_count"],
                )

            with type_col2:

                st.metric(
                    "Document Comparisons",
                    stats["document_count"],
                )

            chart_data = {
                "Comparison Type": ["Text", "Document"],
                "Count": [
                    stats["text_count"],
                    stats["document_count"],
                ],
            }

            st.bar_chart(
                chart_data,
                x="Comparison Type",
                y="Count",
            )

            st.divider()

            # ------------------------------------------
            # RECENT SIMILARITY SCORES
            # ------------------------------------------

            st.subheader("Recent Similarity Scores")

            recent_scores = stats["recent"]

            chart_data = {
                "Comparison": list(
                    range(1, len(recent_scores) + 1)
                ),
                "Similarity (%)": [
                    record["similarity"]
                    for record in reversed(recent_scores)
                ],
            }

            st.line_chart(
                chart_data,
                x="Comparison",
                y="Similarity (%)",
            )

            st.caption(
                "Shows the five most recent comparisons "
                "in chronological order."
            )

            st.divider()

            # ------------------------------------------
            # RECENT ACTIVITY
            # ------------------------------------------

            st.subheader("Recent Activity")

            recent_activity = []

            for record in stats["recent"]:

                recent_activity.append({
                    "Date": record["created_at"],
                    "Type": record["comparison_type"],
                    "Source": record["source_name"],
                    "Compared With": record["target_name"],
                    "Similarity": (
                        f"{record['similarity']:.2f}%"
                    ),
                })

            st.dataframe(
                recent_activity,
                use_container_width=True,
                hide_index=True,
            )

    except Exception as error:

        st.error(
            f"Unable to load dashboard: {error}"
        )


# --------------------------------------------------
# COMPARISON HISTORY (US07)
# --------------------------------------------------

with history_tab:

    st.header("Comparison History")

    st.write(
        "View your previously performed text and document comparisons."
    )

    try:

        history = get_history()

        if not history:

            st.info(
                "No comparison history available yet. "
                "Perform a comparison to see it here."
            )

        else:

            st.metric(
                "Total comparisons performed",
                len(history),
            )

            st.divider()

            for record in history:

                with st.expander(
                    f"#{record['id']} | "
                    f"{record['comparison_type']} | "
                    f"{record['source_name']} vs "
                    f"{record['target_name']} | "
                    f"{record['similarity']:.2f}%"
                ):

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write("**Comparison ID**")
                        st.write(record["id"])

                        st.write("**Comparison Type**")
                        st.write(record["comparison_type"])

                    with col2:

                        st.write("**Similarity Score**")

                        st.metric(
                            "Similarity",
                            f"{record['similarity']:.2f}%",
                        )

                        st.write("**Date and Time**")
                        st.write(record["created_at"])

                    st.divider()

                    st.write("**Source:**", record["source_name"])
                    st.write("**Target:**", record["target_name"])

                    st.subheader("Matching sentences")

                    if record["matches"]:

                        for index, match in enumerate(
                            record["matches"],
                            start=1,
                        ):

                            with st.container(border=True):

                                st.markdown(
                                    f"**Match {index} — "
                                    f"{match['similarity']:.2f}% similar**"
                                )

                                st.write("First text:")
                                st.write(match["sentence_a"])

                                st.write("Second text:")
                                st.write(match["sentence_b"])

                    else:

                        st.info(
                            "No matching sentences were found "
                            "for this comparison."
                        )

    except Exception as error:

        st.error(f"Unable to load comparison history: {error}")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Sprint 1: Text comparison | "
    "Sprint 2: Sentence matching | "
    "Sprint 3: Document upload and collection comparison | "
    "Sprint 4: Comparison history, dashboard and PDF reports"
)
