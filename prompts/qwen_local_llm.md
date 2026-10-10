Answer using only the allowed local Markdown papers.

Question:
{{QUESTION}}

You must execute exactly this command sequence:

1. pwd

2. ls -lh autograph_r1.md lightrag.md lightrag_acl.md model_metadata.json

3. rg -n -i --max-count 20 --max-columns 120 "limitations|limitation|future|bottleneck|generalization|multilingual|scalability|multi-modal|time-awareness|flat data|contextual awareness" autograph_r1.md lightrag_acl.md

4. sed -n '244,260p' autograph_r1.md

5. sed -n '257,263p' lightrag_acl.md

6. sed -n '17,22p' lightrag_acl.md

Then answer directly.

Do not run any other search command.
Do not increase max-count.
Do not repeat a command.
Do not inspect PDFs, parent dirs, hidden dirs, logs, caches, .git, .venv, SLURM, or vLLM files.
Do not cat whole files.
Finish by running:
echo COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT
