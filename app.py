import gradio as gr

def multiply_by_two(x):
    return x * 2

app = gr.Interface(
    fn=multiply_by_two,
    inputs=gr.Number(label="Enter Number"),
    outputs=gr.Number(label="Result"),
    title="Multiply By 2"
)

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)
