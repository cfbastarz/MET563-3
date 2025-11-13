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

![bg left:50%](./figs/2212.jpg)

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

span.footnote2 {
    border-top: 0.1em dotted #555;
    font-size: 60%;
    margin-top: auto;
    position:absolute;
    bottom:0;
    width:100%;
    height:90px;    
}
</style>

<br />

# **Introdução à Assimilação de Dados (MET 563-3)**

### Frameworks de Assimilação de Dados

<br />
<p>Dr. Carlos Frederico Bastarz
<br />
<br />
<br />
<span class="program">Programa de Pós-Graduação em Meteorologia (PGMET) do INPE</span>
<br />
<br />
<span class="date">14 de Novembro de 2025</span>
</p>

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

# Frameworks de Assimilação de Dados

<br />

## **Sumário**

<br />

1. Informações sobre containers
   1.1 Docker
   1.2 Singularity
2. GSI
   2.1 Exercícios em sala
3. JEDI
   3.1 Paradigmas de desenvolvimento do JEDI
   3.2 Instruções para exercícios em casa
4. Outros frameworks de assimilação de dados
5. Atividades realizadas no CPTEC com o GSI e JEDI

---

![bg left:30%](./figs/containers.jpg)

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
</style>

# Frameworks de Assimilação de Dados

<br />

## **1. Informações sobre containers**

<br />

- Um container é um artefato que contém toda a estrutura de software necessária para a execução de outros software em outros computadores
  * É um tipo de virtualização multiplataforma (no Mac OS a virtualização pode ser feita em duas camadas)
  * Foco em portabilidade e reprodutibilidade (mesmo em outras plataformas com processadores diferentes)
  * Elimina a necessidade de configuração do ambiente para a execução do software (mas é necessário instalar o genrenciador do container)
  * Permite o acesso aos dados do host com permissões de acesso que variam de acordo com o tipo de container

- Duas insfraestruturas de containeres mais comnuns são o Docker e o Singularity
  * Apptainer/Singularity foi pensado para ambientes de HPC<sup>&#128312;</sup>
  * Docker tem um propósito mais geral
  * Ambos podem ser utilizados para a maioria das tarefas (e.g., executar um software pela linha de comando ou com interface gráfica; executar um modelo)

<span class="footnote">
<sup>&#128312;</sup>HPC: <i>High Performance Computing</i>
</span>

---

<!-- _footer: "" -->

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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **1. Informações sobre containers**

<br />

### 1.1 Docker

<br />

- Foco é a execução de programas pequenos, aplicações em nuvem em ambienytes corporativos, servidores e redes
* Containeres do Docker são executados como processos do usuário root e requer permissões elevadas e não permitido em ambientes multiusuário (não é permitido o compartilhamento do container por questões de segurança)
* A imagem do container é isolada, i.e., não há ações diretas entre os arquivos de dentro do container e da máquina host
* Requer configurações adicionais para funcionar com MPI<sup>&#128312;</sup> e CUDA<sup>&#128313;</sup>
 
<div>
  <img src="./figs/docker.png" class="floating" alt="Docker logo">
</div>

<span class="footnote">
<sup>&#128312;</sup>MPI: <i>Message Passing Interface</i>
<br />
<sup>&#128313;</sup>CUDA: <i>Compute Unified Device Architecture</i>
</span>

---

<!-- _footer: "" -->

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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **1. Informações sobre containers**

<br />

### 1.2 Apptainer/Singularity<sup>&#128312;</sup>

- Foco está na área científica e ambientes de HPC atendendo a requisitos de execução de programas grandes (e.g., um modelo numérico)
* Containeres do Apptainer/Singularity, por serem compatíveis com ambientes HPC
  * Não requerem permissões de root
  * São compatíveis com MPI para simulações paralelizadas
  * Possui suporte a CUDA
* A imagem do container é isolada da máquina host, mas pode ser compartilhada e movida livremente 
* Permite o uso de imagens do Docker

<div>
  <img src="./figs/apptainer.png" class="floating" alt="Apptainer logo">
</div>

<span class="footnote">
<sup>&#128312;</sup>O Singularity era gerenciado por uma empresa privada (Sylabs), a qual passou a sua tutela para a Linux Foundation - a partir disso, o software foi renomeado para Apptainer
</span>

---

<!-- _footer: "" -->

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

# Frameworks de Assimilação de Dados

<br />

## **2. GSI<sup>&#128312;</sup>**

- O GSI é um framework de assimilação de dados desenvolvido pelo NCEP
  * Fornece a implementação de software para todas as componentes relacionadas à assimilação de dados
    * Métodos variacional (3D/4DVar, híbrido-variacional e 3D/4DEnVar)
    * Métodos baseados em conjuntos (EnKF, EnSRF, LETKF)
    * Métodos de minimização da função custo variacional
    * Operador $H$ (Modelo de Transferência Radiativa)
    * Suporte para modelos globais (espectrais) e regionais (em ponto de grade)
* Foco em sistemas operacionais
* Mantido pelo DTC<sup>&#128313;</sup>/NCAR
  * Centraliza as contribuições, faz o gerenciamento do código, distribui releases e realiza tutoriais para a comunidade de usuários
- Recebe contribuições da NASA, NCEP e universidades  

<span class="footnote">
<sup>&#128312;</sup>GSI: <i>Gridpoint Statistical Interpolation</i>
<br />
<sup>&#128313;</sup>DTC: <i>Developmental Testbed Center</i>
</span>

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

# Frameworks de Assimilação de Dados

<br />

## **2.1 Exercícios em sala**

<br />

- Utilização do container Docker do GSI (fornecido pelo DTC) para a realização dos sistemas 3DVar, 4DVar e híbrido-variacional 3DVar
* Teste com a assimilação de uma única variável
* Verificação da minimização da função custo por meio da verificação dos outer e inner loops
* Verificação da assimilação de dados por meio da redução do erro da análise durante a minimização da função custo

---

<!-- _footer: "" -->

<!-- Scoped style -->
<style scoped>
section {
  font-size: 18px;
}
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **2.1 Exercícios em sala**

<br />

### Instalação do Docker

- Referência Ubuntu Linux (v22.04 +) - [Instalação](https://docs.docker.com/engine/install/ubuntu/) | [Pós-instalação](https://docs.docker.com/engine/install/linux-postinstall)

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
- Em seguida

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

<div>
  <img src="./figs/docker.png" class="floating" alt="Docker logo">
</div>

---

<!-- _footer: "" -->

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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **2.1 Exercícios em sala**

<br />

### Instalação do Docker

- Verificação da instalação

```bash
sudo systemctl status docker
```

- Se o serviço do Docker não estiver em execução

```bash
sudo systemctl start docker
```

- Em seguida

```bash
sudo docker run hello-world
```

<div>
  <img src="./figs/docker.png" class="floating" alt="Docker logo">
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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **2.1 Exercícios em sala**

<br />

### Pós-instalação

- Permitir a execução como usuário normal

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

- Em seguida

```bash
newgrp docker
```

- Finalmente

```bash
docker run hello-world
```

<div>
  <img src="./figs/docker.png" class="floating" alt="Docker logo">
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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **2.1 Exercícios em sala**

<br />

### Instalação do Apptainer/Singularity

<br />

- Forma simples para o Ubuntu Linux e derivados

```bash
wget -c https://github.com/apptainer/apptainer/releases/download/v1.4.2/apptainer_1.4.2_amd64.deb
wget -c https://github.com/apptainer/apptainer/releases/download/v1.4.2/apptainer-suid_1.4.2_amd64.deb
sudo dpkg -i apptainer_1.4.2_amd64.deb
sudo dpkg -i apptainer-suid_1.4.2_amd64.deb
sudo apt install -f
```

- Há pacotes pré-compilados disponíveis para outras distribuições Linux

<div>
  <img src="./figs/apptainer.png" class="floating" alt="Docker logo">
</div>

---

<!-- _footer: "" -->

![bg right:40%](./figs/jedi.png)

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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 80px;
  width: 200px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **3. JEDI<sup>&#128312;</sup>**

- É um esforço conjunto liderado pelo JCSDA<sup>&#128313;</sup> para o desenvolvimento de um novo sistema de assimilação de dados unificado 🔗 [link](https://www.jcsda.org/jcsda-project-jedi)
* Novo framework de assimilação de dados
  * Mais moderno: escrito do zero, com abordagem de separação de conceitos
  * Implementa os métodos de assimilação de dados mais utilizados (variacionais e por conjuntos)
  * Implementa interfaces para diversos modelos (globais, regionais, atmosféricos e oceânicos)
* Foco é a operação e a colaboração de desenvolvimento com a comunidade de usuários
  * Anualmente são oferecidas as _JEDI Academies_ 

<span class="footnote">
<sup>&#128312;</sup>JEDI: <i>Joint Effort for Data Assimilation Integration</i>
<br />
<sup>&#128313;</sup>JCSDA: <i>Joint Center for Satellite Data Assimilation</i>
</span>

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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 200px;
  right: 100px;
  width: 500px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

## **3. JEDI**

<br />

### _JEDI Academy_

<br />
<br />

- <img src="./figs/pepejedi-emoji.png" width="24" style="vertical-align:middle;"/> 7a Jedi Academy 
  - 4 a 8 de outurbo de 2021
  - Formato virtual
  - Página da JEDI Academy: 🔗 [link](https://www.jcsda.org/jedi-academies)
  - Conteúdo do curso: 🔗 [link](http://academy.jcsda.org/2021-10/index.html)

<div>
  <img src="./figs/jediacademy.png" class="floating" alt="Docker logo">
</div>

---

<!-- _footer: "" -->

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
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  top: 320px;
  right: 250px;
  width: 800px;
  opacity: 0.9;
  pointer-events: none; /* evita interferir com seleção de texto */
}

/* Exemplo flex: texto + imagem lado a lado */
.row {
  display: flex;
  align-items: center;
  gap: 120px;
}
.row .left-img {
  width: 200px;
  flex-shrink: 0;
}
</style>

# Frameworks de Assimilação de Dados

<br />

## **3. JEDI**

<br />

### Paradigmas de desenvolvimento do JEDI - Separação de Conceitos

<div>
  <img src="./figs/jedisoc.png" class="floating" alt="Docker logo">
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

# Frameworks de Assimilação de Dados

<br />



<br />

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

# Frameworks de Assimilação de Dados

<br />

## **5. Atividades realizadas no CPTEC com o GSI e JEDI**

---

<!-- _footer: "" -->

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

# Método Variacional - Parte I

<br />

## **3. Introdução ao Método 3DVar**

<br />

* O 3DVar é uma das primeiras aplicações do cálculo variacional em meteorologia
  * **Objetivo:** combinar previsão do modelo e observações para obter a melhor estimativa do estado atmosférico
  
* **Função Custo:**
  $$
  J(\mathbf{x}) =
  \frac{1}{2}(\mathbf{x} - \mathbf{x}_b)^{\text{T}}\mathbf{B}^{-1}(\mathbf{x} - \mathbf{x}_b)

  + \frac{1}{2}[\mathbf{y}_o - H(\mathbf{x})]^{\text{T}}\mathbf{R}^{-1}[\mathbf{y}_o - H(\mathbf{x})]
  $$
* **Gradiente:**
  $$
  \nabla J(\mathbf{x}) = (\mathbf{B}^{-1}+\mathbf{H}^\text{T}\mathbf{R}^{-1}\mathbf{H})(\mathbf{x}-\mathbf{x}_b) - (\mathbf{H}^\text{T}\mathbf{R}^{-1}) [\mathbf{y}_{o}-H(\mathbf{x}_b)] = 0
  $$
* **Solução Analítica Exata:**<sup>&#128312;</sup>
  $$
  \mathbf{x}_a = \mathbf{x}_b + \mathbf{W}[\mathbf{y}_o - H(\mathbf{x}_b)], \quad \mathbf{W} = \mathbf{BH}^{\text{T}}(\mathbf{HBH}^{\text{T}}+\mathbf{R})^{-1}
  $$
  
<span class="footnote">
👉 O 3DVar foi implementado operacionalmente no ECMWF em 1996 e foi substituído pelo 4DVar em 1997; 👉 No CPTEC, o 3DVar começou a ser aplicado em 1997
<br />
<sup>&#128312;</sup>Utilizando a identidade de Sherman-Morrison-Woodburry
</span>

---

<!-- Scoped style -->
<style scoped>
section {
  font-size: 21px;
}
</style>

![bg right:50%](./figs/5620.jpg)

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

<br />
<br />
<br />
<br />
<br />

<p style="font-size:13px;">
👉 This work is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
<p>

