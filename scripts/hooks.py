import logging, re
import mkdocs.plugins

log = logging.getLogger('mkdocs')

@mkdocs.plugins.event_priority(-50)
def on_page_markdown(markdown, page, **kwargs):
    path = page.file.src_uri
    for m in re.finditer(r'\bhttp://[^) ]+', markdown):
        log.warning(f"Documentation file '{path}' contains a non-HTTPS link: {m[0]}")