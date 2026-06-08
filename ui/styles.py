from __future__ import annotations

# Gradio CSS overrides create a neon costume-booth identity.
CUSTOM_CSS = """
body, .gradio-container {
    background-color: #120712 !important;
    color: #fff7ed !important;
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}

#fb-header {
    text-align: center;
    margin: 0 auto 0.65rem auto;
    padding: 0.35rem 0 0.65rem 0;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
#fb-header h1 {
    color: #fb7185 !important;
    font-size: 2.7rem !important;
    font-weight: 760 !important;
    letter-spacing: 0 !important;
    margin-bottom: 0.35rem !important;
}
#fb-header p {
    color: #f0abfc !important;
    font-size: 1.08rem !important;
    margin: 0 !important;
}
#fb-kicker {
    width: fit-content;
    max-width: 92%;
    margin: 0 auto 1.5rem auto;
    padding: 0.72rem 1.6rem !important;
    background-color: rgba(34, 211, 238, 0.08) !important;
    border: 1px solid rgba(251, 113, 133, 0.5) !important;
    border-radius: 8px !important;
    text-align: center;
    color: #fdf4ff !important;
}

.fb-main-grid, .fb-control-row, .fb-example-grid {
    gap: 1rem !important;
    align-items: stretch !important;
}
.fb-main-grid > .form, .fb-main-grid > .row, .fb-main-grid > div,
.fb-example-grid > .form, .fb-example-grid > .row, .fb-example-grid > div {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 1rem !important;
}
.fb-input-panel, .fb-output-panel, .fb-examples-section {
    background-color: #241124 !important;
    border: 1px solid rgba(251, 113, 133, 0.25) !important;
    border-radius: 8px !important;
    box-shadow: 0 5px 16px rgba(0, 0, 0, 0.32) !important;
    padding: 1.15rem !important;
}
.fb-examples-section {
    margin-top: 1rem !important;
}
.fb-input-panel, .fb-output-panel {
    flex: 1 1 340px !important;
}
.fb-input-panel h3, .fb-output-panel h3, .fb-examples-section h3 {
    color: #67e8f9 !important;
    margin: 0 0 0.75rem 0 !important;
}
#fb-idea-input textarea, .fb-prompt-output textarea, .fb-log-box textarea {
    background-color: #140a14 !important;
    color: #fff7ed !important;
    border: 1px solid rgba(240, 171, 252, 0.34) !important;
    border-radius: 8px !important;
    line-height: 1.5 !important;
    overflow-wrap: anywhere !important;
}
.fb-image-input, .fb-output-image, .fb-audio-input {
    border-radius: 8px !important;
    overflow: hidden !important;
}
.fb-output-image {
    min-height: 420px !important;
}
.fb-run-btn {
    background: #22d3ee !important;
    color: #120712 !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 760 !important;
    min-height: 52px !important;
}
.fb-run-btn:hover {
    opacity: 0.9 !important;
}
.fb-example-card {
    flex: 1 1 245px !important;
    background-color: #140a14 !important;
    border: 1px solid rgba(251, 113, 133, 0.26) !important;
    border-radius: 8px !important;
    padding: 0.85rem !important;
}
.fb-example-copy {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
.fb-example-head {
    display: flex;
    justify-content: space-between;
    gap: 0.8rem;
    color: #fce7f3;
    font-weight: 740;
}
.fb-example-head strong {
    color: #67e8f9;
    white-space: nowrap;
}
.fb-example-copy p {
    color: #f5d0fe;
    margin: 0;
    line-height: 1.45;
}
.fb-example-btn {
    border-radius: 8px !important;
}
#fb-links {
    text-align: center;
    margin-top: 1rem;
    color: #a5f3fc !important;
}
"""
