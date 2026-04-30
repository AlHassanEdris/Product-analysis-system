# Fusion Model

def fuse(text_score, image_score):
    final_score = 0.6 * text_score + 0.4 * image_score
    return final_score
