import requests
import streamlit as st

def buscar_letra(banda, musica):
  endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
  response = requests.get(endpoint)
  letra = response.json()["lyrics"] if response.status_code == 200 else ""
  return letra

st.image("https://images.unsplash.com/photo-1511379938547-c1f69419868d?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width=500)
st.title("Letras de Música")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
  letra = buscar_letra(banda, musica)
  if letra:
    st.success("Encontramos a letra da sua música!")
    st.text(letra)
  else:
    st.error("Infelizmente não foi possível encontrar a letra dessa música")
