from transformers import pipeline
import gradio as gr

pipe = pipeline("text-classification", model="cesarcodigo/cesarcodigo-toxicidad")

def analizar_texto(texto):
  resultado = pipe(texto)[0]
  label = resultado['label']
  score = resultado['score']
  if label == 'LABEL_1':
    return f'This comment is toxic (score: {score})'
  else:
    return f'This comment is not toxic (score: {score}'



demo = gr.Interface(
    fn=analizar_texto,
    inputs=gr.Textbox(label='write a comment'),
    outputs=gr.Textbox(label='result')
)

if __name__ == "__main__":
    demo.launch()