Goal: Turn messy, redacted, inconsistent comments into clean text

import re
RE_REDACTION = re.compile(r"
\REDACTED.*?|]
", flags=red.IGNORECASE)

def remove_redactions(text: str) -> str:
return RE_REDACTION.sub("", text)
