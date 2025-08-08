def read_logs(file_obj, max_lines=100):
    """
    Reads the last `max_lines` lines from a file-like object.
    Supports both binary streams (from Streamlit uploaders)
    and regular text files (from open()).
    """
    try:
        # If binary (Streamlit upload)
        content = file_obj.read()
        if isinstance(content, bytes):
            content = content.decode("utf-8")
        lines = content.splitlines()
    except Exception as e:
        # If already a text file
        lines = file_obj.readlines()

    return "\n".join(lines[-max_lines:])

