import streamlit as st
import requests

# Título da página
st.title('Datacrafters Generative Agent with Langchain 🐦')

# Campo de entrada para o usuário digitar o texto
input_text = st.text_input("Digite sua entrada:", "")

# Botão para enviar a entrada
if st.button('Gerar'):
    if input_text:
        # URL da API (ajuste conforme necessário)
        url = 'http://localhost:8000/generate/agent'
        
        # Dados a serem enviados como JSON
        data = {'input_text': input_text}
        
        # Fazendo a requisição POST para a API
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            # Obtendo a resposta da API
            result = response.json()['model_response']
            st.success(f'Resposta: {result}')
        else:
            st.error('Erro ao processar a requisição')
    else:
        st.error('Por favor, digite alguma coisa para gerar.')
        