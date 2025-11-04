---
theme: gaia
_class: lead
paginate: true
transition: slide
backgroundColor: #fff
footer: '**Introdução à Assimilação de Dados (MET 563-3)**'
marp: true

style: |
  pre, code {
    font-family: "Fira Code", monospace;
    background: #2e3440;
    color: #eceff4;
    border-radius: 8px;
    padding: 0.75em 1em;
    font-size: 0.9em;
  }

  pre {
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    margin: 1em 0;
  }
---

<!-- _footer: "" -->

![bg left:50%](./figs/1683.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
span.date {
  font-size: 15px;
}

span.program {
  font-size: 18px;
}
</style>

<style>
span.footnote {
    border-top: 0.1em dotted #555;
    font-size: 60%;
    margin-top: auto;
    position:absolute;
    bottom:0;
    width:100%;
    height:60px;    
}
</style>

# **Introdução à Assimilação de Dados (MET 563-3)**

### Motivação - Métodos Baseados em Conjuntos

<p>Dr. Carlos Frederico Bastarz
<br />
Dr. Dirceu Luis Herdies
<br />
<br />
<span class="program">Programa de Pós-Graduação em Meteorologia (PGMET) do INPE</span>
<br />
<br />
<span class="date">05 de Outubro de 2025</span>
</p>

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **Sumário**

<br />

1. Introdução ao método EnKF
2. Histórico e desenvolvimento
3. Características principais
4. _Inflation_ e _Localization_
5. Visão geral sobre os esquemas derivados
6. Atividades realizadas no CPTEC com o método LETKF
7. Filtro de Bayes Recursivo

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **1. Introdução ao método EnKF**

<br />

### O Filtro de Kalman linear (clássico)

<br />

- O Filtro de Kalman calcula analiticamente a atualização do estado e da covariância, assumindo:
  * Linearidade
  * Ruído gaussiano

$$
x_k = F_k(x_{k-1}) + w_{k-1}, \quad y_k = H_k(x_k) + v_k
$$

* Onde:
  * $x_k$ é o estado do sistema no tempo $k$
  * $y_k$ são as observações
  * $F_k$ é a matriz de transição do estado
  * $H_k$ é a matriz de observação
  * $w_k$ e $v_k$ são ruídos de processo e observação gaussianos
  
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **1. Introdução ao método EnKF**

<br />

### O Filtro de Kalman linear (clássico)

<br />

- Vantagens do Filtro de Kalman linear:
  * Além de estimar o estado do sistema (análise), estima analiticamente a covariância (incerteza)
    * 👉 Permite quantificar a confiança na análise
    
      $$
      x_a = x_f + K [y_o - H(x_f)], \quad \mathbf{P}^{a} = (I - KH)\mathbf{P}^{f}
      $$
    
    * A matriz $K$ (ganho de Kalman) ajusta a contribuição do modelo e da observação
    
* Limitações do Filtro de Kalman linear:
  * Não é adequado para sistemas de alta dimensão (e.g., atmosfera, oceado), pois as matrizes de covariâncias ($\mathbf{P}^{f}$ e $\mathbf{P}^{a}$) são explícitas e enormes
  * Requer que o modelo dinâmico seja (quase) linear
  
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **1. Introdução ao método EnKF**

<br />

- O EnKF foi desenvolvido mantendo as principais características do filtro de Kalman linear, mas com as diferenças:
  * Estimativa das covariâncias feita com base nos membros do ensemble e não via matriz explícitas
  * Matriz ganho de Kalman é conceitualmente igual, mas também calculada a partir do ensemble:
  
    $$
    K = P^f H^T(HP^f H^T + R)^-1
    $$
    
  * O espaço do ensemble (i.e., o tamanho do ensemble), é o que define os seus graus de liberdade:
    * A propagação das covariâncias é feita pela propagação do ensemble
    * Permite tratar a não linearidade, pois cada membro do ensemble pode evoluir pelo modelo não linear completo
  
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **2. Histórico e desenvolvimento**

<br />

- O Filtro de Kalman por conjunto é um filtro do tipo Monte-Carlo
  * Assume que os erros são gaussianos
  * Assume que as relações entre os estados são lineares
  * Usa as matrizes de covariâncias para quantificar as incertezas
  
* 💔 O problema é que:
  * Em sistemas reais (e.g., atmosfera, oceano), é impossível armazenar e propagar a matriz de covariâncias completa  
 
* A solução:
  * Ao invés de armazenar as matrizes de covariâncias (teóricas) gigantes, o EnKF estima estas matrizes a partir de um conjunto de amostras (ensemble)
 
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 17px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
.github-code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.95em;
  background-color: #323742;
  color: #f6f8fa;
  padding: 0.2em 0.4em;
  border-radius: 6px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **2. Histórico e desenvolvimento**
  
<div class="columns">
<div>

- O método Monte-Carlo foi introduzido nos anos 1940:
  * Jon von Neumman, durante o desenvolvimento do projeto Manhattan (bomba atômica)
  * Se não é possível calcular algo diretamente, pode-se estimar o resultado por meio de simulações aleatórias
  * Exemplo: estimar o valor de $\pi$ contando quantos pontos caem dentro de um quadrado que contém um círculo inscrito (a razão entre os pontos dentro do círculo e o total é $\approx \frac{\pi}{4}$)

  * 🎲 Exemplo:
  
    ```python
    import numpy as np

    np.random.seed(42)
    
    N = 1000000
    x = np.random.rand(N)
    y = np.random.rand(N)
    dentro_circulo = (x**2 + y**2) <= 1

    estima_pi = 4 * np.sum(dentro_circulo) / N
    print(estima_pi)
    ```  
  
</div>
<!--<div style="margin-left:150px; margin-top:-100px;">-->
<div>
    
<div class="columns">
<div>

<br />
<br />
<br />
<br />

<div align="center">
  <img src="./figs/estpi.png" width="300"/>
</div>

</div>
<div>

<br />
<br />

* 👉 Resultados:

  | Valores de <span class="github-code">N</span> | Valores de $\pi$ |
  |-----------------------------------------------|------------------|
  | 1                                             | 0,0              |
  | 10                                            | 2,8              |
  | 100                                           | 3,2              |
  | 1.000                                         | 3,112            |
  | 10.000                                        | 3,1556           |
  | 100.000                                       | 3,1376           |
  | 1.000.000                                     | 3,141864         |
  | 10.000.000                                    | 3,1415772        |

</div>
</div>

</div>
</div>  

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **2. Histórico e desenvolvimento**

<br />

- O Kalman Filter linear foi introduzido em 1960:
  * _A New Approach to Linear Filtering and Prediction Problems_ (Kalman, 1960)
  * https://x.gd/VlIfX
- O Ensemble Kalman Filter foi introduzido em 1994:
  * _Sequential data assimilation with a nonlinear quasi-geostrophic model using Monte Carlo methods to forecast error statistics_ (Evensen, 1994)
  * https://x.gd/VsQ1V
- Com a evolução dos computadores e o aumento da complexidade do sistema de observação global, novas técnicas derivadas do EnKF surgiram:
  * ETKF - _Ensemble Transform Kalman Filter_
  * LETKF - _Local Ensemble Transform Kalman Filter_
  * Muitos outros...

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **2. Histórico e desenvolvimento**

<br />

- O KF original é aplicado a problemas com dinâmica linear
  * Extensões do KF original foram desenvolvidas para serem aplicadas a problemas com dinâmica não linear (EKF - _Extended Kalman Filter_)
  * O EKF lineariza a solução sucessiva da trajetória do modelo através da aplicação de um modelo tangente linear (tal como o 4DVar)
- O EnKF original é estocástico, no sentido de que as observações são perturbadas para gerar um conjunto de análises
  
  
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **3. Características principais**

<br />

- No EnKF, a covariância dos erros de previsão é substituída pela covariância do conunto:

  $$ 
  \mathbf{P}^{f} = \frac{1}{N-1} \sum_{i=1}^{N}{ <\mathbf{x}_{i} - \bar{\mathbf{x}}>^{\text{T}} <\mathbf{x}_{i} - \bar{\mathbf{x}}>}
  $$
  
  - Se o conjunto for pequeno, as covariâncias são subestimadas
  - Quanto maior o conjunto, melhor será a representação das covariâncias
    * Qual é o tamanho ideal de um conjunto para que se tenha a melhor estimativa das covariâncias do ("erro") do modelo?
  
  
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **4. _Inflation_ e _Localization_**

<br />

- No ciclo de assimilação de dados do EnKF (e variantes), as observações são utilizadas para corrigir o estado do modelo
  * Mas o EnKF perturba o modelo para amostrar a sua incerteza 
  * Ambiguidade: ao mesmo tempo que se perturba do estado, tenta-se corrigí-lo
  * Então, ao longo do tempo, a tendência é a de a incerteza do EnKF seja cada vez mais subestimada, de forma que é necessário inflar a incerteza do conjunto para evitar:
  * A localização é utilizada para compensar o efeito cíclico de correções sobre o espalhamento do conjunto de previsões devido ao seu tamanho

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **5. Visão geral sobre os esquemas derivados**

<br />

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **6. Atividades realizadas no CPTEC com o método LETKF**

<br />

- Por volta de 2009, o grupo de assimilação de dados do CPTEC vinha estudando a aplicação do LETKF como método substituto para a sua análise operacional em domínio global
  * Resolução: TQ0126L028 (aproximadamente 100 km de resolução espacial horizontal e 28 níveis verticais em coordenada sigma)
  * 80 membros
* Desafios: 
  * Desempenho computacional para um conjunto grande de membros (aumento da resolução ficou limitado ao tamanho do conjunto)
  * Assimilação de radiâncias (necessidade de desenvolvimento de diferentes operadores $H$ para diferentes tipos de observações não convencionais)


---

<!-- _transition: drop -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 18px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **6. Atividades realizadas no CPTEC com o método LETKF**

<br />

* LETKF permaneceu como método de pesquisa do CPTEC:
  * **2010** - Tese Rosângela Cintra: "ASSIMILAÇÃO DE DADOS COM REDES NEURAIS ARTIFICIAIS EM MODELO DE CIRCULAÇÃO GERAL DA ATMOSFERA"
  * **2010** - Pós-Doutorado José Aravéquia: "Evaluation of a Strategy for the Assimilation of Satellite Radiance Observations
with the Local Ensemble Transform Kalman Filter"  
  * **2011** - Dissertação Maria Medeiros: "IMPACTO DO USO DE RADIÂNCIA NA ASSIMILAÇÃO DE DADOS USANDO 4D-LETKF NA REGIÃO DA AMÉRICA DO SUL"
  * **2013** - Bolsa PCI Lucas Avanço: "ASSIMILAÇÃO DE DADOS DE RÁDIO OCULTAÇÃO GNSS NO LETKF: DISPONIBILIDADE DE DADOS E IMPLEMENTAÇÃO DE UM OPERADOR"
  * **2018** - Tese Helena Barbieri: "AJUSTE DINÂMICO PARA ANÁLISE HÍBRIDA ENTRE UM SISTEMA VARIACIONAL E FILTRO DE KALMAN POR CONJUNTO"
  * **2018** - Tese Leonardo Lima: "ESTUDO DAS INCERTEZAS NA SIMULAÇÃO POR CONJUNTOS E NO USO DA ASSIMILAÇÃO DE DADOS NO OCEANO ATLÂNTICO SUDOESTE"
  * Entre outros...  
  
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
p {
  text-align: center;
  font-size: 100px;
}
</style>

<br />
<br />
  
**Ninja Vs. Codorna**

🥷  🐦

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />
<!--  -->
<div style="
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
  margin-top:0px;
  font-size: 50px;
  font-weight: bold;
">
Ninja Vs. Codorna

🥷  🐦
</div>

* Uma codorna :bird: pia no meio da mata
* Um ninja 🥷 escuta...
* A codorna pia mais uma vez
* O ninja escuta novamente...
* O ninja quer saber **onde está a codorna**
* A codorna pia novamente...
* E ela faz isso mais 100 vezes
* **Pergunta:** será o ninja capaz de descobrir a posição da codorna no meio da mata? (continua...)

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Palavras-chave

* **Hipótese:** uma pergunta - uma teoria seria uma afirmação?
* **"Dado":** uma informação, uma observação
* **Verossimilhança:** (ou _likelihood_) o grau de veracidade de uma determinada informação
* **Informação à _priori_:** (ou _prior_) aquilo que se conhece a princípio
* **Informação à _posteriori_:** (ou _posterior_) aquilo que se conclui a partir da informação à _priori_
* **Probabilidade conjunta:** probabilidade de dois ou mais eventos ocorrerem simultaneamente

### Conceito-chave

* **Probabilidade condicional:** ocorrência de um evento dada uma informação à _priori_

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

$$
P(H|D) = \frac{P(H)P(D|H)}{P(D)}
$$

- $H$: é a hipótese
- $D$: é o dado observado (uma informação observada)
- $P(H|D)$: é o _posterior_ (ou posteriori, é a probabilidade da hipotese após observar o dado)
- $P(H)$: é o _prior_ (é a probabilidade atribuída à hipótese antes de ver o dado)
- $P(D)$: é a probabilidade do dado (constante de normalização)
- $P(D|H)$: verossimilhança (é a probabilidade da observar o dado, considerando-se a hipótese verdadeira)

<br />

👉 Normaliza-se a probabilidade da hipótese (_prior_) e a verossimilhança pela probabilidade do dado. **Por que?**

$$
P(H|D) \propto P(H)P(D|H)
$$

<br />

<div style="
  background-color: #f8d7da; 
  color: #721c24; 
  padding: 20px; 
  border-radius: 10px; 
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
  margin-top:0px;
  font-size: 18px;
">
O que significa "máxima verossimilhança"?
</div>

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Probabilidade Vs. Verossimilhança

<br />

- **Probabilidade:** é a chance de ocorrência de um determinado evento possível
- **Verossimilhança:** é provável (ou possível) que este evento exista? Este evento é plausível?

<br />

Para que um determinado evento ocorra, é necessário que ele evista e que pertença a um determinado conjunto de eventos possíveis. A máxima verossimilhança destaca, portanto, o quão verossímil é a probabilidade do evento.

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Verossimilhança

<br />

* Considere que você observa o lançamento de 20 dados :dice: sobre uma mesa e deseja saber qual é a verossimilhança desta observação. Todos os dados apresentam os mesmos valores
* Para isto, consideramos duas hipóteses:
  1. Dado viciado
  2. Dado não viciado

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### 🎲 Dado viciado

* Neste cado, os 20 dados apresentam o mesmo valor (e.g., 5). A probabilidade conjunta destes eventos $P(dado_{1}) \times P(dado_{2}) \times ... \times P(dado_{20})$ é $({\frac{1}{1}})^{20}=1$


### 🎲 Dado não viciado

* Neste caso, cada um dos 20 dados possui a mesma probabilidade de apresentar um dos 6 números possíveis. A probabilidade conjunta neste caso é $({\frac{1}{6}})^{20} \approxeq 0$
  
<br />  
  
  <div style="
    background-color: #f8d7da; 
    color: #721c24; 
    padding: 20px; 
    border-radius: 10px; 
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
    margin-top:0px;
    font-size: 18px;
  ">
  Portanto, é muito mais verossímil que o dado seja viciado dada a observação inicial
  </div>
  
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Provabilidade Vs. Verossimilhança

#### Exemplo

- $D$: o ninja 🥷 ouve um canto na mata
- $H$: há uma codorna :bird: na mata
- $L(H|D)$: é a verossimilhança

* $P(D|H) \neq P(H|D)$: o fato de o ninja ouvir um canto na mata, dado que há uma codorna na mata, não significa que dado que há uma codorna na mata, o ninja ouvirá um canto - ela pode estar dormindo 💤
* $P(H|D)$, então $L(H|D)$ é baixa: se há uma codorna na mata, não necessariamente ela está cantando e o que o ninja ouve não é uma codorna, mas sim um pardal &#128038;
* $P(D|H)$, então $L(H|D)$ é alta: se há uma codorna na mata, então há um canto ecoando na mata

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Estimativa de Máxima Verossimilhança

<br />

* Permite estimar, por exemplo, os momentos estatísticos de uma determinada distribuição. Por exemplo:
  * Quais são os valores de média ($\mu$) e desvio-padrão ($\sigma$) que maximizam a probabilidade de um determinado evento (ou hipótese) ou dado observado?
  * Em outras palavras, quais são os valores de $\mu$ e $\sigma$ que tornam os dados observados mais prováveis (considerando que os dados vem de uma distribuição normal $N(\mu,\sigma^{2})$)?
  
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Exemplo de Inferência Bayesiana (ou Filtro Bayesiano)

<br />

- Kalnay (2002)<sup>&#128312;</sup>: dadas duas observações independentes $T_{1}$ e $T_{2}$, as quais são assumidas possuírem distribuição normal e erros com desvios-padrão $\sigma_{1}$ e $\sigma_{2}$, qual é o valor mais provável de $T$? Neste caso, define-se a análise como sendo o valor mais provável de $T$ dadas as observações e as suas estatísticas de erro:

$$
P(T|T_{1},T_{2}) = \frac{P(T)P(T_{1},T_{2}|T)}{P(T_{1},T_{2})}
$$
  
<span class="footnote">
<sup>&#128312;</sup>Kalnay, E. (2002). Atmospheric Modeling, Data Assimilation and Predictability. Cambridge: Cambridge University Press.
</span>  
  
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 20px;
}
</style>

![bg right:50%](./figs/normal2.png)

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**
  
- Distribuição Normal - ou Gaussiana:

$$
p_{\sigma_{1}}(T_{1}|T) = \frac{1}{\sqrt{2\pi}\sigma_{1}}{e}^{-\frac{(T_{1}-T)^{2}}{2\sigma_{1}^{2}}}
$$
  

$$
p_{\sigma_{2}}(T_{2}|T) = \frac{1}{\sqrt{2\pi}\sigma_{2}}{e}^{-\frac{(T_{2}-T)^{2}}{2\sigma_{2}^{2}}}
$$  
  
- O valor mais provável (_likely_) de $T$ dadas as observações independentes $T_{1}$ e $T_{2}$, é aquele que maximiza a **probabilidade conjunta**, ou seja, o produto de $p_{\sigma_{1}}$ e $p_{\sigma_{2}}$:

$$
p_{\sigma_{1}}(T_{1}|T)p_{\sigma_{2}}(T_{2}|T) = \frac{1}{2\pi\sigma_{1}\sigma_{2}}{e}^{-\frac{(T_{1}-T)^{2}}{2\sigma_{1}^{2}}-\frac{(T_{2}-T)^{2}}{2\sigma_{2}^{2}}}
$$
  
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 20px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

<div class="columns">
<div>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Prior, posterior, likelihood, distribuição de probabilidade...

<br />

- Teorema de Bayes: 

$$
P(H|D)=\frac{P(H)P(D|H)}{P(D)}
$$

- Distrbuição Gaussiana: 

$$
p_{\sigma_{1}}(T_{1}|T) = \frac{1}{\sqrt{2\pi}\sigma_{1}}{e}^{-\frac{(T_{1}-T)^{2}}{2\sigma_{1}^{2}}}
$$

</div>
<div>

<div align="center">
  <img src="./figs/vero2.png" width="600"/>
</div>


</div>
</div>

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 20px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

<div id="plotly-div" style="width: 100%; height: 700px;"></div>

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
var H = [];
for(var i=-4; i<=4; i+=0.04){ H.push(i); }

var D = H.slice();  // mesma discretização
var P_H = H.map(h => Math.exp(-0.5*(h/1.5)*(h/1.5)));

// Superfície simples (só exemplo)
var z = [];
for(var i=0;i<H.length;i++){
    var row = [];
    for(var j=0;j<D.length;j++){
        row.push(Math.exp(-0.5*((D[j]-H[i])/1.0)**2)*P_H[i]);
    }
    z.push(row);
}

var data = [{
    z: z,
    x: H,
    y: D,
    type: 'surface',
    colorscale: 'Viridis'
}];

Plotly.newPlot('plotly-div', data);
</script>




---

<!-- _transition: drop -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
p {
  text-align: center;
  font-size: 100px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

### Inferência Bayesiana Recursiva (ou "Filtro de Bayes Recursivo")

* Um ninja ouve o canto intermitente de uma codorna (ela está parada). A cada canto, ele tenta descobrir a posição da codorna. **Como o ninja pode inferir a posição da codorna?**
  * Brincadeira do "quente-frio"
* Um outro problema real poderia ser: ajustar um modelo aos valores observados a cada ciclo de análise (iterativamente)
  * Como isso pode ser feito?
* Qualquer algorítmo de ajuste iterativo pode ser realizado como uma inferência Bayesiana recursiva? 
  
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
p {
  text-align: center;
  font-size: 100px;
}
</style>

<br />
<br />
  
**Ninja Vs. Codorna**

🥷  🐦
  
---

![bg right:50%](./figs/pos_codorna.png)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**
  
<br />  
  
### Exemplo prático: Ninja Vs. Codorna
  
- 🔴 posição real da codorna
- ➕ posição da codorna, segundo o ninja ($N=100$)
  
* A cada canto da codorna, o ninja tenta descobrir a posição real da ave
* O ninja pode modelar a situação e, com um número finitor de tentativas, pode estimar a posição mais provável da codorna
  
---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 20px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
.github-code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.7em;
  background-color: #323742;
  color: #f6f8fa;
  padding: 0.2em 0.4em;
  border-radius: 6px;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**
  
<br />

<div class="columns">
<div>

<br />
<br />
<br />

<video width="500" controls>
  <source src="./figs/bayes_recursivo.mp4" type="video/mp4">
  Seu navegador não suporta vídeo.
</video>

</div>
<div>

Para cada posição inferida pelo ninja, a "função iterativa de Bayes", calcula a verossimilhança da posição:

<span class="github-code">
m[i,j] =  norm * np.exp(np.matmul(-(x[:,n] - me), np.matmul(inv, (x[:,n] - me) / 2.)))
</span>

ou seja, 

$$
p_{\sigma_{1}}(T_{1}|T) = \frac{1}{\sqrt{2\pi}\sigma_{1}}{e}^{-\frac{(T_{1}-T)^{2}}{2\sigma_{1}^{2}}}
$$

<div style="
  background-color: #f8d7da; 
  color: #721c24; 
  padding: 20px; 
  border-radius: 10px; 
  text-align: center;
  max-width: 600px;
  margin: 0 auto;
  margin-top:20px;
  font-size: 18px;
">
A melhor estimativa obtida pelo ninja utilizando-se a inferência Bayesiana recursiva, é chamada de "Estimativa de Máxima Verossimilhança" e representa o valor mais provável a ser obtido (cores mais quentes na superfície) da posição da cordona
</div>

</div>
</div>
 
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# Métodos Baseados em Conjuntos

<br />

## **7. Filtro de Bayes Recursivo**

<br />

🎲 Notebook com <a href="https://colab.research.google.com/github/cfbastarz/MET563-3/blob/main/atividade_07_filtro_bayes_recursivo.ipynb" target="_blank">Atividade Prática 7</a> 
 
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# 1. Ensemble Forecast Exemplo

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
N = 20  # membros do ensemble
x_true = 5.0
x_f = np.random.normal(4.0, 1.0, N)  # forecast ensemble
y_obs = 5.2
R = 0.2**2

plt.figure(figsize=(8,4))
plt.scatter(np.arange(N), x_f, color='blue', label='Forecast Ensemble')
plt.hlines(y_obs, 0, N-1, color='red', linestyles='--', label='Observação')
plt.ylabel('Estado')
plt.xlabel('Membro do Ensemble')
plt.title('Ensemble Forecast')
plt.legend()
plt.show()
```

---


<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# 2. Atualização EnKF Clássico (Estocástico)

```python
K = 0.5  # simplificação para ilustração
x_a_enkf = []

for xi in x_f:
    y_i = y_obs + np.random.normal(0, np.sqrt(R))  # observação perturbada
    xi_a = xi + K*(y_i - xi)
    x_a_enkf.append(xi_a)

plt.figure(figsize=(8,4))
plt.scatter(np.arange(N), x_f, color='blue', label='Forecast')
plt.scatter(np.arange(N), x_a_enkf, color='green', label='Análise EnKF')
plt.hlines(y_obs, 0, N-1, color='red', linestyles='--', label='Observação')
plt.title('Atualização Ensemble - EnKF Estocástico')
plt.xlabel('Membro do Ensemble')
plt.ylabel('Estado')
plt.legend()
plt.show()
```

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# 3. Atualização EnSRF (Determinístico)

```python
x_bar_f = np.mean(x_f)
x_bar_a = x_bar_f + K*(y_obs - x_bar_f)  # atualização da média
X_prime_f = x_f - x_bar_f
T = np.sqrt(1 - K)  # simplificação de transformação
X_prime_a = X_prime_f * T
x_a_ensrf = x_bar_a + X_prime_a

plt.figure(figsize=(8,4))
plt.scatter(np.arange(N), x_f, color='blue', label='Forecast')
plt.scatter(np.arange(N), x_a_ensrf, color='orange', label='Análise EnSRF')
plt.hlines(y_obs, 0, N-1, color='red', linestyles='--', label='Observação')
plt.title('Atualização Ensemble - EnSRF Determinístico')
plt.xlabel('Membro do Ensemble')
plt.ylabel('Estado')
plt.legend()
plt.show()
```
    
---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# 4. Comparação Conceitual

EnKF clássico: perturba observações → spread preservado mas com ruído
EnSRF: determinístico → covariância preservada sem ruído adicional

      EnKF clássico                     EnSRF
  ------------------              ------------------
    x^f members                     x^f members
       |                                |
  perturb observation                 média atualizada
       |                                |
  update each member                 ajustar desvios
       |                                |
  x^a members                        x^a members
(spread com ruído)                  (spread consistente)

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 19px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
</style>

# 5. Conclusão

- KF clássico: linear, baixa dimensão
- EnKF: estocástico, simples, bom para grandes ensembles
- EnSRF: determinístico, covariância precisa, ideal para ensembles pequenos

Visualização do spread ajuda a entender como cada método trata a incerteza

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

![bg right:50%](./figs/1648.jpg)

# :thinking: Dúvidas

<br />
<br />
<br />
<br />
<br />
<br />
<br />

:link: https://cfbastarz.github.io/met563-3/
:octopus: https://github.com/cfbastarz/MET563-3
:email: carlos.bastarz@inpe.br
