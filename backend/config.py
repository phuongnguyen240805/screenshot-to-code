import os


def _bounded_int_env(name: str, default: int, minimum: int, maximum: int) -> int:
    """Read a bounded integer environment variable with a safe default."""
    raw = os.environ.get(name)
    if raw is None or not raw.strip():
        return default

    try:
        value = int(raw)
    except ValueError:
        return default

    return max(minimum, min(maximum, value))


# Keep upstream defaults when env vars are absent. For the LadiPage internal
# microservice deployment set NUM_VARIANTS=1 to avoid generating four landing
# page variants when the caller only consumes one result.
NUM_VARIANTS = _bounded_int_env("NUM_VARIANTS", 4, 1, 4)
NUM_VARIANTS_VIDEO = _bounded_int_env("NUM_VARIANTS_VIDEO", 2, 1, 2)

# LLM-related
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", None)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", None)
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL", None)

# Image generation (optional)
REPLICATE_API_KEY = os.environ.get("REPLICATE_API_KEY", None)

# Debugging-related
IS_DEBUG_ENABLED = bool(os.environ.get("IS_DEBUG_ENABLED", False))
DEBUG_DIR = os.environ.get("DEBUG_DIR", "")

# When enabled, every LLM request is written to run_logs/prompt_reports as a
# JSON report viewable at /evals/prompt-reports.
PROMPT_REPORTS_ENABLED = os.environ.get(
    "PROMPT_REPORTS_ENABLED", ""
).strip().lower() in {"1", "true", "yes", "on"}
LOCAL_ASSET_DIR = os.environ.get(
    "LOCAL_ASSET_DIR", os.path.join(os.path.dirname(__file__), "local_assets")
)
# Base URL the backend serves /local-assets from. The live (websocket) path
# infers this per-request; the evals path has no request, so it uses this.
LOCAL_ASSET_BASE_URL = os.environ.get("LOCAL_ASSET_BASE_URL", "http://127.0.0.1:7001")

# Set to True when running in production (on the hosted version)
# Used as a feature flag to enable or disable certain features
IS_PROD = os.environ.get("IS_PROD", False)
