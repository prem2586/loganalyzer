def read_logs(file_obj, max_lines=100):
    """
    Reads the last `max_lines` lines from a log file.
    Handles both uploaded file-like objects and regular file handles.

    Args:
        file_obj: A file-like object (from open() or Streamlit uploader)
        max_lines: Number of lines to keep from the end

    Returns:
        A single string containing the last N lines
    """
    try:
        # For uploaded files (Streamlit): need to decode from bytes
        lines = file_obj.read().decode("utf-8").splitlines()
    except AttributeError:
        # For local open() files: already in string format
        lines = file_obj.readlines()

    return "\n".join(lines[-max_lines:])
