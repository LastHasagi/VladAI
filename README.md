# API de Modelo Antifraude com FastAPI e Machine Learning

Criei uma API REST usando FastAPI que, com ML, ela se torna capaz de identificar transações financeiras fraudulentas.
A ideia é conseguir com esse projeto fazer uma integração em um sistema de pagamentos real (ainda não defini qual sistema irei usar).

## Treinamento

Todo o treinamento da AI foi feito de maneira supervisionada com dados que são referentes à transções que já são determinadas como fraudulentas, possivelmente fraudulentas, se quiserem usar um Dataset verdadeiro, é possível, o modelo está bem configurado para updates.
Usei também o modelo de Regressão Linear para aprendizado.

## Acurácia 

Definida pelo total de previsões corretas divido pelo total de previsões e a fórmula é:

$$
\text{Acurácia} = \frac{\text{(TP + TN)}}{\text{(TP + TN + FP + FN)}}
$$

## Precisão 

Definida pela divisão dos verdadeiros positivos pelas previsões verdadeiras e a fórmula é:

$$
\text{Precisão} = \frac{\text{(TP)}}{\text{(TP + FP)}}
$$

## Sensibilidade

Definida pela proporção dos verdadeiros positivos por todos os realmente verdadeiros onde sua fórmula é:

$$
\text{Sensibilidade} = \frac{\text{(TP)}}{\text{(TP + FN)}}
$$

## F1-Score

Combinação da Precisão e Sensibilidade em uma única métrica usando a média harmônica:

$$
\text{F1} = \frac{\text{2.(PRECISÂO).(SENSIBILIDADE)}}{\text{(PRECISÃO + SENSIBILIDADE)}}
$$

## Como consultar?

Envie para a API o json do seguinte modelo:

```json
{
    "idade": 0,
    "renda_anual": 0,
    "historico_credito": 0,
    "valor": 0,
    "tipo_transacao": "string", 
    "local_transacao": "string", 
    "categoria_comercio": "string",
    "canal_autenticacao": "string",
    "frequencia_transacoes_24h": 0,
    "distancia_localizacao": 0,
    "tentativas_falhas_ultimas_24h": 0,
    "hora_transacao": "string"
}
```

Lembrando que por enquanto esses parâmetros são meio que obrigatórios serem assim:
> (["Araraquara", "São Carlos", "Ribeirão Preto", "Matão", "São Paulo", "Bahia"])
> (["presencial", "online"])
> (["supermercado", "eletronicos", "restaurante", "luxo", "vestuário"])

Você pode treinar sua IA com infinitos parâmetros e usar esse código como uma base para o desenvolvimento, sinta-se livre para modificar o que quiser. (Se quiser me mencionar, ficarei feliz 😂)

## Tecnologias usadas
| Tecnologia | Motivo |
|------------|--------|
| <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="170"/> | Utilizado para a criação e documentação rápida da nossa API, permitindo desenvolvimento ágil e eficiente. |
| <img src="https://camo.githubusercontent.com/967fcae13b3922eb5e13d0b98ab391095ffd0bec86ea6904cf4ce5d9b8fdc670/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e737667" alt="Python" width="70"/> | Linguagem de programação utilizada devido à sua simplicidade e vasto ecossistema de bibliotecas. |
| <img src="https://pandas.pydata.org/static/img/pandas_white.svg" alt="Pandas" width="170"/> | Ferramenta poderosa para manipulação e análise de dados, essencial para o processamento de grandes volumes de informações. |
| <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="Scikit-learn" width="170"/> | Biblioteca de machine learning que oferece diversas ferramentas para modelagem e avaliação de algoritmos. |
