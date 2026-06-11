init_path = "/content/Y3_EPA_NHS-Staff-Survey_NLP-Hybrid-Workflow/pipeline/__init__.py"

with open(init_path, "w") as f:
    f.write("from .utils import run_preprocessing\n")

print("__init__.py overwritten CLEANLY.")
