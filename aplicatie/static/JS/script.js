console.log("script pornit"); 
function obtineProduse(pagina = 1) {
    console.log("apeleaza functia obtineProduse cu pagina =", pagina);

    const form = document.getElementById('filterForm');
    const dateFormular = new FormData(form);
    dateFormular.append('pagina', pagina);

    if (categorie_url_param !== null) {
        dateFormular.set('categorie', categorie_url_param);
    }

    const params = new URLSearchParams(window.location.search);
    if (params.has('sort')) {
        dateFormular.append('sort', params.get('sort'));
    }

    if (pagina !== 1) {
        alert("Atentie: In urma repaginarii este posibil sa fi sarit peste unele produse sau sa le vezi din nou pe cele deja vizualizate.");
    }

    if (!dateFormular.get('categorie')) dateFormular.delete('categorie');
    if (!dateFormular.get('marime')) dateFormular.delete('marime');
    if (!dateFormular.get('pret_minim')) dateFormular.delete('pret_minim');
    if (!dateFormular.get('pret_maxim')) dateFormular.delete('pret_maxim');
    if (!dateFormular.get('items_per_page')) dateFormular.delete('items_per_page');


    console.log("trimit fetch...");

    fetch(URL_FILTRARE, {
        method: "POST",
        body: dateFormular,
        headers: {
            'X-CSRFToken': CSRF_TOKEN,
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        console.log("raspuns brut primit:", response);
        return response.json();
    })
    .then(data => {
        console.log("JSON primit:", data); 

        let listaProduse = document.getElementById('produseItems');
        listaProduse.innerHTML = ''; 

        if (data.status === 'success') {
            data.produse.forEach(produs => {
                const divProdus = document.createElement('div');
                divProdus.classList.add('produs-card');
                divProdus.innerHTML = `
                    ${produs.imagine ? `<img src="${produs.imagine}" alt="${produs.nume}">` : ''}
                    <div class="produs-detalii">
                        <h3 class="nume">
                            <a href="/SissiStudio/produse/${produs.id}/">${produs.nume}</a>
                        </h3>
                        <p class="pret">Pret: ${produs.pret} RON</p>
                        <p class="categorie">
                            <a href="/SissiStudio/categorii/${produs.categorie_url}/">
                                ${produs.categorie_icon ? `<img src="${produs.categorie_icon}" alt="${produs.categorie}" class="categorie-icon">` : ''}
                                ${produs.categorie}
                            </a>
                        </p>
                    </div>
                `;

                listaProduse.appendChild(divProdus);
            });

            // paginare
            const paginDiv = document.querySelector('.paginare');
            if (paginDiv && data.pagination) {
                const p = data.pagination;
                let html = '';
                if (p.has_previous) html += `<a href="#" data-page="${p.previous_page_number}">Inapoi</a>`;
                html += `<span>Pagina ${p.pagina_actuala} din ${p.total_pagini}</span>`;
                if (p.has_next) html += `<a href="#" data-page="${p.next_page_number}">Inainte</a>`;
                paginDiv.innerHTML = html;

                // evenimente pentru click pe paginare
                paginDiv.querySelectorAll('a[data-page]').forEach(a => {
                    a.addEventListener('click', e => {
                        e.preventDefault();
                        obtineProduse(parseInt(a.getAttribute('data-page')));
                    });
                });
            }

        } else {
            listaProduse.innerHTML = `<p style="color:red;">Eroare: ${data.message}</p>`;
        }
    })
    .catch(error => console.error("Eroare la obținerea produselor:", error));
}


document.addEventListener("DOMContentLoaded", () => {

    console.log("script pornit");

    const form = document.getElementById('filterForm');
    const resetBtn = document.getElementById('resetButton');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        console.log("submit formular");
        obtineProduse();   // AICI SE APELĂ FUNCTIA
    });

    resetBtn.addEventListener('click', function() {
        console.log("reset efectuat");
        form.reset();
        obtineProduse();
    });

});
