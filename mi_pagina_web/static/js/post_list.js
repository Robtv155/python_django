function cardHTML(post) {
    return `
        <div class="tarjeta">
            <h2>${post.title}</h2>
            <p>${post.content.slice(0, 50)}...</p>
            <a href="/post/${post.id}/">Lee el post</a>
            ${post.tags.map(
               t => `<a class="tag" href="/post_by_tag/${t.id}/">${t.name}</a>`
            ).join('')}
        </div>`;
}

function loadPost(page = 1) {
    fetch(`/api/posts/?page=${page}`)
        .then(r => r.json())
        .then(json => {
            const lista = Array.isArray(json) ? json : json.results;
            const cont = document.querySelector('.grid');
            lista.forEach(p => cont.insertAdjacentHTML('beforeend', cardHTML(p)));
            nextPage = json.next ?? null;
        })
        .catch(err => console.error('Error al cargar posts:', err));
}

let nextPage = 1;
loadPost();
