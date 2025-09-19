---
theme: gaia
_class: lead
paginate: true
transition: slide
backgroundColor: #fff
footer: '**Introdução à Assimilação de Dados (MET 563-3)**'
marp: true
---

<!-- _footer: "" -->

![bg left:50%](./figs/2141.jpg)

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

# **Introdução à Assimilação de Dados (MET 563-3)**

### Apresentação da Disciplina

<p>Dr. Carlos Frederico Bastarz
<br />
Dr. Dirceu Luis Herdies
<br />
<br />
<span class="program">Programa de Pós-Graduação em Meteorologia (PGMET) do INPE</span>
<br />
<br />
<span class="date">22 de Setembro de 2025</span>
</p>

---

![bg right:30%](./figs/sumario.png)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :memo: Sumário

<br />
<br />
<br />
<br />

1. Finalidade
2. Instrutores
3. Pré-requisitos
4. Assuntos Abordados
5. Bibliografia Recomendada 
6. Forma de avaliação
7. Grupo de Assimilação de Dados
8. Dúvidas

---

![bg left:30%](./figs/objectives.jpeg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :dart: Finalidade

<br />

## **Objetivos**

- Fornecer aos alunos uma visão geral sobre o que é a assimilação de dados, quais são os seus métodos principais e quais as técnicas utilizadas para a sua aplicação
- Experimentar os esquemas principais de assimilação de dados por meio de **toy models** em ambiente controlado

<br />

## **Escopo**

- Assimilação de Dados Atmosféricos
- As mesmas técnicas podem ser pensadas para aplicações em outros fluídos, levendo-se em consderação as peculiaridades e as especificidades de outros modelos

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :busts_in_silhouette: Instrutores

<br />

<img align="right" width="150" height="150" src="./figs/carlos.png">

## **Dr. Carlos Frederico Bastarz**

- Graduação em Licenciatura em Matemática (UNESP, 2005)
- Mestrado e Doutorado em Meteorologia (INPE, 2010 e 2017)
* _Assimilação de Dados Variacional e por Conjunto_

<br />

<img align="right" width="150" height="150" src="./figs/dlherdies.png">

## **Dr. Dirceu Luis Herdies**

- Graduação em Física (UFSM, 1983)
- Mestrado em Meteorologia (INPE, 1991)
- Doutorado em Meteorologia (USP, 2002)
* _Assimilação de Dados regional_
  
--- 

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :gear: Pré-requisitos

<br />

## **Parte teórica<sup>&#128312;</sup>**

- Meteorologia Dinâmica I (MET 225-3)
- Métodos Matemáticos em Meteorologia (MET 560-3)
- Modelagem Numérica da Atmosfera (MET 576-4)

<br />

## **Parte prática<sup>&#128312;</sup>**

- Bash
- Fortran
- Python
- Containers

<span class="footnote">
<sup>&#128312;</sup>Desejável
</span>

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados<sup>&#128312;</sup>

<br />
<br />

1. Motivação
2. O Sistema Global de Observações Meteorológicas
3. Métodos Clássicos (Esquemas de Interpolação Estatística)
4. Método Variacional
5. Métodos Baseados em Conjuntos (EnKF et al.)
6. Métodos Híbridos (Ensemble-Variacional)
7. Frameworks de Assimilação de Dados
8. Assimilação de Dados Regional
9. Impacto e Experimentos de Sistemas Observacionais
10. Assimilação de Dados de Superfície
11. Reanálises

<span class="footnote">
<sup>&#128312;</sup>São 11 assuntos, incluindo as aulas práticas (sujeito a alterações e ajustes)
</span>

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

![bg right:30%](./figs/richardsond.jpg)

# :books: Assuntos Abordados

<br />
<br />

## **1. Motivação**

- Por que a assimilação de dados fornece uma estimativa ótima?
- Histórico da Assimilação de Dados
  - Revisão do histórico da assimilação de dados e das motivações para o seu desenvolvimento, passando pelos métodos tradicionais/clássicos até o estabelecimento dos métodos operacionais para modelos massivamente paralelos

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

![bg left:30%](./figs/globalobssys3.png)

# :books: Assuntos Abordados

<br />
<br />

## **2. O Sistema Global de Observações Meteorológicas**

- O que é o Sistema Global de Observações Meteorlógicas
- Os diferentes tipos de observações (_in situ_, por sensoriamento remoto e plataformas oceânicas) 
- O fluxo de dados operacional no CPTEC para a Assimilação de Dados
- Controle de Qualidade das Observações

---

![bg right:30%](./figs/classicalmethods.jpeg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados

<br />
<br />

## **3. Métodos Clássicos (Esquemas de Interpolação Estatística)**

- Revisão dos métodos clássicos de assimilação de dados baseados em interpolação estatística
  - Análise de Cressman
  - Interpolação Ótima

---

<!-- _footer: "" -->

![bg right:30%](./figs/gauss.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 20px;
}
</style>

# :books: Assuntos Abordados

## **4. Método Variacional**

- Revisão de Álgebra Linear (Operações com Matrizes)
- Introdução do método 3DVar
  - Histórico e desenvolvimento 
  - Características principais 
  - PSAS<sup>&#128312;</sup>
  - FGAT<sup>&#128313;</sup>
- Componentes 
  - Método de minimização da função custo do 3DVar
  - Matriz de Covariâncias dos Erros de Previsão
  - Modelo de Transferência Radiativa
  - Controle de Qualidade
- Visão geral sobre o método 4DVar
- Atividades realizadas no CPTEC com o método 3DVar

<span class="footnote">
<sup>&#128312;</sup>PSAS: <i>Physical-space Statistical Analysis System</i>
<br />
<sup>&#128313;</sup>FGAT: <i>First Guess at Appropriate Time</i>
</span>

---

<!-- _footer: "" -->

![bg left:30%](./figs/borboleta.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados

<br />
<br />

## **5. Métodos Baseados em Conjuntos (EnKF et al.)**

- Introdução ao método EnKF<sup>&#128312;</sup>
- Histórico e desenvolvimento
- Características principais 
- Inflation e Localization
- Visão geral sobre os esquemas derivados
- Atividades realizadas no CPTEC com o método LETKF<sup>&#128313;</sup>

<span class="footnote">
<sup>&#128312;</sup>EnKF: <i>Ensemble Kalman Filter</i><br />
<sup>&#128313;</sup>LETKF: <i>Local Ensemble Transform Kalman Filter</i>
</span>
 
---

![bg right:30%](./figs/hybrid.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados

<br />
<br />

## **6. Métodos Híbridos (Ensemble-Variacional)**

- Introdução ao método híbrido ensemble-variacional 3DEnVar
- Histórico e desenvolvimento
- Características principais
- Atividades realizadas no CPTEC com o método ensemble-variacional 3DEnVar

---

![bg left:30%](./figs/frames.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados

<br />
<br />

## **7. Frameworks de Assimilação de Dados**

- Apresentação dos principais frameworks abertos para a assimilação de dados operacional: GSI e JEDI
- Paradigmas de desenvolvimento do JEDI 
- Atividades realizadas no CPTEC com o GSI e JEDI

---

![bg right:30%](./figs/2116.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados

<br />
<br />

## **8. Assimilação de Dados Regional**

- Apresentação sobre as particularidades de um sistema de assimilação de dados regional
- Assimilação de Dados de Radar
- Desenvolvimentos realizados no CPTEC

---

![bg left:30%](./figs/impact.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :books: Assuntos Abordados

<br />
<br />

## **9. Impacto e Experimentos de Sistemas Observacionais**

- Visão geral sobre a metodologia e a ferramenta para o estudo de impacto das observações empregada no sistema de assimilação de dados do CPTEC
- Impacto da Assimilação das Observações
- Observing System Experiment (OSE) e Observing System Simulation Experiment (OSSE)

---

# :books: Assuntos Abordados

![bg right:30%](./figs/superficie.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

<br />
<br />

## **10. Assimilação de Dados de Superfície**

- Apresentação sobre a assimilação de dados de superfície, seus impactos e desafios
- Desenvolvimentos realizados no CPTEC

---

# :books: Assuntos Abordados

![bg left:30%](./figs/1568.jpg)

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

<br />
<br />

## **11. Reanálises**

- O que é reanálise
- Reanálise como ferramenta de validação de modelos numéricos
- Desenvolvimentos realizados no CPTEC com reanálise regional

---

![bg left:35%](./figs/livro_kalnay.jpg)

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :books: Bibliografia Recomendada

<br />
<br />

## **Livros**

Kalnay, E. (2002). Atmospheric Modeling, Data Assimilation and Predictability. Cambridge: Cambridge University Press.

- https://www.cambridge.org/highereducation/books/atmospheric-modeling-data-assimilation-and-predictability/C5FD207439132836E85027754CE9BC1A#overview

---

![bg left:35%](./figs/livro_daley.jpg)

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :books: Bibliografia Recomendada

<br />
<br />

## **Livros**

Daley, R. (1991). Atmospheric Data Analysis. Cambridge Atmospheric and Space Science Series, Cambridge University Press.

- https://www.cambridge.org/pm/universitypress/subjects/earth-and-environmental-science/atmospheric-science-and-meteorology/atmospheric-data-analysis

---

![bg left:35%](./figs/livro_lynch.jpg)

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :books: Bibliografia Recomendada

<br />
<br />

## **Livros**

Lynch, P. (2006). The Emergence of Numerical Weather Prediction: Richardson's Dream, Cambridge University Press.

- https://maths.ucd.ie/~plynch/Dream/Dream.html

---

![bg left:35%](./figs/livro_varahan.png)

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :books: Bibliografia Recomendada

<br />
<br />

## **Livros**

Lewis,  J. M., Lakshmivarahan S., Dhall S. (2006). Dynamic Data Assimilation: A Least Squares Approach. Cambridge University Press.

- https://www.cambridge.org/core/books/dynamic-data-assimilation/91BD4736A2CD99B575002A89518DB63C

---

![bg left:35%](./figs/livro_lahoz.jpeg)

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :books: Bibliografia Recomendada

<br />
<br />

## **Livros**

Lahoz, W., Khattatov, B., and Ménard, R. (2010). Data Assimilation: Making Sense of Observations. Springer-Verlag, Heidelberg.

- https://link.springer.com/book/10.1007/978-3-540-74703-1

---

![bg left:35%](./figs/livro_jazwinski.jpg)

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :books: Bibliografia Recomendada

<br />
<br />

## **Livros**

A. Jazwinski (1970). Stochastic Processes and Filtering Theory. Mathematics in Science and Engineering, Vol. 64, Academic Press.

- https://store.doverpublications.com/products/9780486462745?srsltid=AfmBOopDWzwg5wKhLva9kk5dmEhQW0tH-aYP-jKL9_468Aj7UP8gNzEj

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {  
  font-size: 21px;
}
</style>

# :scream: Forma de avaliação

## **Trabalhos práticos com relatórios<sup>&#128312;</sup>**

- Experimentos com **toy models** e os sistemas de assimilação de dados com a produção de relatórios
  - Uso de containers Apptainer e Docker e notebooks do Jupyter
  
<br />

## **Apresentação de artigos para discussão em sala de aula<sup>&#128312;</sup>**

- Cada aluno fará uma apresentação (explicação de um artigo em assimilação de dados)
  - Alunos podem escolher um artigo em assimilação de dados relacionado com a sua dissertação/tese

<br />

## **Interação durante as aulas**

- Dúvidas, perguntas e respostas

<span class="footnote">
<sup>&#128312;</sup>Individual
</span>

--- 

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
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

# :busts_in_silhouette: Grupo de Assimilação de Dados

<br />
<br />
<br />

## **Atividades de Pesquisa e Desenvolvimento**

- Desenvolvimento em assimilação de dados e técnicas de previsão por conjuntos para os modelos do CPTEC:
  - _Brazilian Atmospheric Model_ (BAM/GSI<sup>&#128312;</sup>)
  - _Model for Ocean-LaNd-Atmosphere PredictionN_ (MONAN/JEDI<sup>&#128313;</sup>)
- Pesquisas relacionadas com a assimilação de dados GNSS _Radio Occultation_, Radar e Radiâncias Hiperespectrais
- Desenvolvimento de software para o suporte às atividades de pesquisa
- Mais informações em :octopus: https://github.com/GAD-DIMNT-CPTEC

<span class="footnote">
<sup>&#128312;</sup>GSI: <i>Gridpoint Statistical Interpolation</i>
<br />
<sup>&#128313;</sup>JEDI: <i>Joint Effort for Data Assimilation Integration</i>
</span>

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :busts_in_silhouette: Grupo de Assimilação de Dados

<br />
<!--## Equipe-->

<img align="right" width="150" height="150" src="./figs/jgerd.png">

## **Dr. João Gerd Zell de Mattos<sup>&#128312;</sup>**

- Graduação em Meteorologia (UFPel, 2003)
- Mestrado e Doutorado em Meteorologia (INPE, 2006 e 2016)
* _Assimilação de Dados de Superfície_

<br />

<img align="right" width="150" height="150" src="./figs/sapucci.png">

## **Dr. Luiz Fernando Sapucci**

- Graduação em Licenciatura em Matemática (UNESP, 1998)
- Mestrado e Doutorado em Ciências Cartográficas (UNESP, 2001 e 2005)
* _Assimilação de dados GNSS-RO_

<span class="footnote">
<sup>&#128312;</sup>Coordenador do GAD
</span>

--- 

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :busts_in_silhouette: Grupo de Assimilação de Dados

<br />

<img align="right" width="150" height="150" src="./figs/profile.png">

## **Dr. Éder Paulo Vendrasco<sup>&#128312;</sup>**

- Graduação em Meteorologia (USP, 2003)
- Mestrado em Meteorologia (USP, 2006)
- Doutorado em Meteorologia (INPE, 2015)
* _Assimilação de Dados de Radar_

<br />

<img align="right" width="150" height="150" src="./figs/sergio.png">

## **Dr. Sérgio Henrique Ferreira Soares**

- Graduação em Física (UNITAU, 1984)
- Mestrado e Doutorado em Meteorologia (INPE, 2003 e 2013)
* _Observações Meteorológicas e Controle de Qualidade_

<span class="footnote">
<sup>&#128312;</sup>Coordenador da PGMET
</span>

--- 

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

# :busts_in_silhouette: Grupo de Assimilação de Dados

<br />

<img align="right" width="150" height="150" src="./figs/helena.png">

## **Dra. Helena Barbieri de Azevedo**

- Graduação em Meteorologia (UFPel, 2010)
- Mestrado e Doutorado em Meteorologia (INPE, 2014 e 2018)
* _Assimilação de Dados de Radiâncias_

<br />

<img align="right" width="150" height="150" src="./figs/liviany.png">

## **Dra. Liviany Pereira Viana**

- Graduação em Meteorologia (UEA, 2012)
- Mestrado e Doutorado em Meteorologia (INPE, 2015 e 2021)
* _Impacto das Observações na Assimilação de Dados_

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

![bg right:50%](./figs/2140.jpg)

# :thinking: Dúvidas

<br />
<br />
<br />
<br />
<br />
<br />
<br />

:link: https://cfbastarz.github.io
:email: carlos.bastarz@inpe.br
:octopus: https://github.com/cfbastarz
