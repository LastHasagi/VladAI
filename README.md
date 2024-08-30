# API de Modelo Antifraude com FastAPI e Machine Learning

Criei uma API REST usando FastAPI que, com ML, ela se torna capaz de identificar transações financeiras fraudulentas.
A ideia é conseguir com esse projeto fazer uma integração em um sistema de pagamentos real (ainda não defini qual sistema irei usar).

## Treinamento

Todo o treinamento da AI foi feito de maneira supervisionada com dados que são referentes à transções que já são determinadas como fraudulentas, possivelmente fraudulentas...

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

## Informações para definir fraudes
1. Transações de valor muito alto para um cliente que possui uma renda anual baixa.

2. Transação ocorrendo em um local muito distante da localização atual do cliente.

3. Transação muito grande em nome de um cliente com score de crédito baixo.

#### Exemplo de transação fraudulenta

Senhor Cléber está fazendo uma compra de R$57.803,41, o sistema verifica que a renda anual é de R$10.365,76 e Sr. Cléber tem um Score de 328. 
Em nosso sistemas, essa transação deverá ficar marcada como fraudulenta. Teremos em nosso dataset uma coluna marcada como *Fraudulenta* (que terá valor 1) e outra *Legítima* (que terá valor 0).

## Treinamento do modelo

Com o dataset rotulado, o modelo de machine learning aprende a identificar padrões associados às transações fraudulentas. No treinamento, o modelo analisa as transações e tenta encontrar correlações entre as características (como valor da transação, local, histórico de crédito) e o rótulo de fraude.

## Como o modelo aprende?

 Algoritmo de *Regressão Logística*: Esse algoritmo tenta encontrar uma função matemática que separe as transações fraudulentas das legítimas. Ele calcula a probabilidade de uma transação ser fraudulenta com base nos dados de entrada.
> Exemplo: Se uma transação é de alto valor e o cliente tem um histórico de crédito baixo, o modelo pode "aprender" que essas características aumentam a probabilidade de fraude.

## Predição de novas transações
Quando uma nova transação é enviada para o modelo, ele usa a função que aprendeu durante o treinamento para calcular a probabilidade dessa transação ser fraudulenta.

>>*Probabilidade*: O modelo retorna um valor entre 0 e 1. Se o valor for próximo de 1, significa que a transação tem alta probabilidade de ser *fraudulenta*. Se for próximo de 0, a transação provavelmente é legítima. Baseado na probabilidade, podemos definir um limiar (por exemplo 0.5), se a probabilidade estiver acima do limiar a transação é considerada fraudulenta e será "negada".

## Dados no Dataset

> Observação: Todos os dados usados para treinamento da AI foram gerados com a biblioteca '
### Dados do cartão e do cliente
<ol>
    <li>
        <b>cartao_id</b>
        <ul>
            <li>
            <b>Descrição:</b> Identificação única do cartão de crédito.
            </li>
        </ul>
    </li>
    <li>
        <b>cliente_id</b>
        <ul>
            <li>
            <b>Descrição:</b> Identificação única do cliente titular do cartão.
            </li>
        </ul>
    </li>
    <li>
        <b>idade</b>
        <ul>
            <li>
            <b>Descrição:</b> Idade do cliente titular do cartão.
            </li>
            <li>
            <b>Relevância:</b> Certas faixas etárias podem ter comportamentos de compra específicos, o que pode ser relevante para identificar fraudes (por exemplo, compras de alto valor feitas por clientes muito jovens).
            </li>
        </ul>
    </li>
    <li>
        <b>renda_anual</b>
        <ul>
            <li>
            <b>Descrição:</b> Renda anual declarada do cliente.
            </li>
            <li>
            <b>Relevância:</b> A renda influencia diretamente o poder de compra. Transações de valor muito alto, incompatíveis com a renda do cliente, podem ser indicativas de fraude.
            </li>
        </ul>
    </li>
    <li>
        <b>historico_credito</b>
        <ul>
            <li>
            <b>Descrição:</b> Pontuação de crédito do cliente, variando entre 0 e 1.
            </li>
            <li>
            <b>Relevância:</b> Clientes com um histórico de crédito ruim (pontuação baixa) podem estar mais propensos a comportamentos atípicos, e transações de alto valor podem ser suspeitas.
            </li>
        </ul>
    </li>
</ol>

### Dados da transação

<ol>
    <li>
        <b>transacao_id</b>
        <ul>
            <li><b>Descrição:</b> Identificação única da transação.</li>
        </ul>
    </li>
    <li>
        <b>valor</b>
        <ul>
            <li><b>Descrição:</b> Valor monetário da transação.</li>
            <li>
            <b>Relevância:</b> Transações de valor muito alto, especialmente se forem inesperadas ou repetidas em curto intervalo, podem ser sinal de fraude.
            </li>
        </ul>
    </li>
    <li>
        <b>data_hora</b>
        <ul>
            <li><b>Descrição:</b> Data e hora em que a transação foi realizada.</li>
        </ul>
    </li>
    <li>
        <b>tipo_transacao</b>
        <ul>
            <li><b>Descrição:</b> Tipo de transação realizada (presencial, online, etc.).</li>
            <li>
            <b>Relevância:</b> O tipo de transação pode influenciar o risco de fraude. Transações online, por exemplo, geralmente têm maior risco.
            </li>
        </ul>
    </li>
    <li>
        <b>local_transacao</b>
        <ul>
            <li><b>Descrição:</b> Localização geográfica onde a transação foi realizada (cidade, estado).</li>
            <li>
            <b>Relevância:</b> Transações feitas em locais distantes do habitual do cliente podem indicar fraude, especialmente se realizadas em curto intervalo de tempo.
            </li>
        </ul>
    </li>
    <li>
        <b>categoria_comercio</b>
        <ul>
            <li><b>Descrição:</b> Categoria do estabelecimento onde a compra foi feita (ex.: restaurante, supermercado, loja de luxo).</li>
            <li>
            <b>Relevância:</b> Compras em categorias incomuns para o cliente (ex.: uma compra de luxo inesperada) podem ser suspeitas.
            </li>
        </ul>
    </li>
    <li>
        <b>canal_autenticacao</b>
        <ul>
            <li><b>Descrição:</b> Método de autenticação utilizado na transação (chip, tarja magnética, contactless, online).</li>
            <li>
            <b>Relevância:</b> Certos métodos de autenticação podem ser mais vulneráveis a fraude (ex.: transações online sem autenticação adicional).
            </li>
        </ul>
    </li>
</ol>

### Dados do comportamento

<ol>
    <li>
        <b>frequencia_transacoes_24h</b>
        <ul>
            <li><b>Descrição:</b> Número de transações feitas pelo cliente nas últimas 24 horas.</li>
            <li>
            <b>Relevância:</b> Um aumento súbito no número de transações em curto período pode ser um indicativo de fraude.
            </li>
        </ul>
    </li>
    <li>
        <b>distancia_localizacao</b>
        <ul>
            <li><b>Descrição:</b> Distância entre a localização atual da transação e a localização habitual das transações do cliente.</li>
            <li>
            <b>Relevância:</b> Transações feitas em locais distantes da localização habitual do cliente podem ser sinal de cartão clonado ou perdido.
            </li>
        </ul>
    </li>
    <li>
        <b>tentativas_falhas_ultimas_24h</b>
        <ul>
            <li><b>Descrição:</b> Número de tentativas de transações falhas nas últimas 24 horas.</li>
            <li>
            <b>Relevância:</b> Várias tentativas falhas seguidas de uma transação bem-sucedida podem indicar uma tentativa de fraude, como tentativa de adivinhar a senha.
            </li>
        </ul>
    </li>
    <li>
        <b>hora_transacao</b>
        <ul>
            <li><b>Descrição:</b> Hora do dia em que a transação foi feita.</li>
            <li>
            <b>Relevância:</b> Transações feitas em horários atípicos, como madrugada, podem ser suspeitas, especialmente se o cliente normalmente não faz compras nesse horário.
            </li>
        </ul>
    </li>
</ol>

### Rótulo de fraude (label)

<ol>
    <li>
        <b>fraudulenta</b>
        <ul>
            <li><b>Descrição:</b>   Indica se a transação foi considerada fraudulenta <b>1</b> ou não <b>0</b>.</li>
            <li>
            <b>Relevância:</b> Este é o rótulo que o modelo de machine learning vai aprender a prever. Transações com <b>fraudulenta = 1</b> são aquelas que, de acordo com as características analisadas, foram marcadas como possivelmente <b>fraudulentas</b>.
            </li>
        </ul>
    </li>
</ol>

## Tecnologias usadas
| Tecnologia | motivo |
|----| ---- |
| FastAPI | --- |
| Python | --- |
