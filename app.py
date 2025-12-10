import gradio as gr
import time
from PIL import Image, ImageDraw, ImageFont


# Draw array as vertical lines
def draw_lines(arr, max_val, min_val, width=600, height=300):
    img = Image.new("RGB", (width, height), "black")
    draw = ImageDraw.Draw(img)

    if not arr:
        return img

    n = len(arr)

    try: #Checks if the font is usable - AI
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default() # Always has a font

    for i, v in enumerate(arr):
        x1 = int(i * width / n)  #Width makes the bars fit based on how many bars there are - AI
        x2 = int((i + 1) * width / n)
        h = int(((v - min_val + 1)/ (max_val - min_val + 1)) * 280) #Scales heigth based on relation to min and max values
        if h <= 0:
            h = 1
        draw.rectangle([(x1, height - h), (x2, height)], fill="white")

        text = str(v)  # Displays the vales for each bar above it - AI
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        text_x = x1 + (x2 - x1) // 2 - text_w // 2
        text_y = height - h - text_h - 4  # 4px above the bar

        draw.text((text_x, text_y), text, fill="white", font=font)

    return img

# Splits arrays in half and calls function to merge

def split_visual(arr):
    # Yield current state for visualization
    yield arr

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    leftside = arr[:half]
    rightside = arr[half:]


    left_sorted = None
    right_sorted = None

    # left recursion frames - AI
    for frame in split_visual(leftside):
        left_sorted = frame
        yield merge(left_sorted, rightside) if right_sorted else frame

    # right recursion frames - AI
    for frame in split_visual(rightside):
        right_sorted = frame
        yield merge(left_sorted, right_sorted) if left_sorted else frame

    # Final merge
    merged = merge(left_sorted, right_sorted)
    yield merged # Display

    return merged

# merge logic

def merge(left, right):
    l = 0
    r = 0
    new_list = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            new_list.append(left[l])
            l += 1
        else:
            new_list.append(right[r])
            r += 1

    # append leftovers
    new_list.extend(left[l:])
    new_list.extend(right[r:])

    return new_list

# GRADIO SIMULATION

def simulate(user_input, speed):
    try: # checks if user_input is valid
        arr = [int(x.strip()) for x in user_input.split(" ") if x.strip() != ""]
    except:    
        raise ValueError

    # produce frames
    max_val = max(arr)
    min_val = min(arr)
    for frame in split_visual(arr):
        img = draw_lines(frame, max_val, min_val)
        time.sleep(speed)
        yield img



# GRADIO UI

with gr.Blocks() as demo:
    gr.Markdown("## 🔷 Merge Sort Animation")


    user_input = gr.Textbox(
        label="Enter intergers with a space between them",
        placeholder="e.g. 3 1 5 2",
        lines=1
    )
    speed = gr.Slider(0.01, 1.5, value=0.05, step=0.01, label="Animation Speed")

    out = gr.Image(label="Visualization")
    start = gr.Button("Start")
    
    start.click(simulate, [user_input, speed], out)

demo.launch()
