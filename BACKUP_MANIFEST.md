# Backup manifest

This snapshot contains the Mini-SWE-Agent experiment harness and its Sudoku/Papers QA examples. Credential fields in the LiteLLM and vLLM configuration files were replaced with `${LITELLM_API_KEY}`; the original files were left unchanged.

Excluded local state:

- `.env` and any environment-specific credentials.
- `logs/` terminal logs and `runs/` trajectories.
- `.venv/`, `.pytest_cache/`, Python bytecode caches.

Copy any experiment logs or trajectories needed for later analysis to separate storage before the cluster account is removed.
