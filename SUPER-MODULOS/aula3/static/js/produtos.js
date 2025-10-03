document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("produtos-cards");

  fetch("/api/produtos")
    .then((response) => response.json())
    .then((data) => {
      if (data.length === 0) {
        container.innerHTML = `<p class='text-center'>Nenhum produto inserido.</p>`;
        return;
      }

      data.slice(-3).forEach((produto) => {
        const card = document.createElement("div");
        card.className = "col";
        card.innerHTML = `
                <div class="card h-100>
                ${
                  produto.imagem
                    ? `<img src="/static/${produto.imagem}" class="card-img-top">`
                    : `<img src="https://placehold.co/600x400?text=Not+Image" class="card-img-top">`
                }
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">${produto.name}</h5>
                        <p class="card-text mb-4">Preço:${produto.price.toFixed(
                          2
                        )}</p>
                    </div>
                </div>
                `;
        container.appendChild(card);
      });
    });
});
