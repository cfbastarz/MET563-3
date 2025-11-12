---
marp: true
theme: default
---

<style>
/* Garante que elementos absolutos sejam posicionados em relação ao slide */
section {
  position: relative;
}

/* Imagem flutuante no canto inferior direito */
.floating {
  position: absolute;
  bottom: 30px;
  right: 40px;
  width: 120px;
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

# Slide com imagem flutuante

Texto do slide aqui.

<!-- Usa HTML puro — mais confiável que Markdown+atributos -->
<img src="./figs/docker.png" class="floating" alt="Docker logo">

---

# Slide com texto e imagem lado a lado

<div class="row">
  <div>
    - Ponto 1<br>
    - Ponto 2<br>
    - Ponto 3
  </div>

  <div>
    <img src="./figs/docker.png" class="left-img" alt="Docker logo">
  </div>
</div>
