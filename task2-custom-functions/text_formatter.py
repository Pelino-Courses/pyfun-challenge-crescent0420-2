def format_text(text, width=70, align='left'):
    """
    Format a string to a specified width and alignment ('left', 'right', 'center').

    Parameters:
        text (str): The input string.
        width (int): Line width (positive integer). Default is 70.
        align (str): Text alignment. One of 'left', 'right', or 'center'. Default is 'left'.

    Returns:
        str: Formatted, aligned, and wrapped text.

    Raises:
        TypeError: If input types are incorrect.
        ValueError: If values are invalid.

    Example:
        format_text("Hello", width=10, align='center')  # Returns '  Hello   '
    """
    import textwrap

    # Input validation
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if width <= 0:
        raise ValueError("width must be a positive integer")
    if align not in ('left', 'right', 'center'):
        raise ValueError("align must be one of 'left', 'right', or 'center'")

    # Wrap text
    wrapped_lines = textwrap.wrap(text, width=width)

    # Align text
    aligned_lines = []
    for line in wrapped_lines:
        if align == 'left':
            aligned_lines.append(line.ljust(width))
        elif align == 'right':
            aligned_lines.append(line.rjust(width))
        elif align == 'center':
            aligned_lines.append(line.center(width))

    return '\n'.join(aligned_lines)


# Example usage with error handling
if __name__ == "_main_":
    try:
        sample_text = "This is a test of the emergency text formatting system."
        print(format_text(sample_text, width=30, align='center'))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")