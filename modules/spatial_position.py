def get_position(x_center, frame_width):
    """Object kis direction me hai"""
    if x_center < frame_width * 0.33:
        return "left"
    elif x_center > frame_width * 0.66:
        return "right"
    else:
        return "center"

def get_distance_message(box_height, frame_height):
    """Kitna dur hai"""
    ratio = box_height / frame_height
    if ratio > 0.5:
        return "very close"
    elif ratio > 0.25:
        return "near"
    else:
        return "far"