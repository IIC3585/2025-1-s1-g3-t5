# Proyecto Astro + Content Collections

## Instalación

```bash
npm install
npm run dev
```

## Contenido consultado
- https://docs.astro.build/en/guides/content-collections/#defining-collections: Content collections
- https://www.youtube.com/watch?v=8o5MZPfBpf4: Curso astro js 2023 - construye una pagina web con la Api The Rick and Morty
- https://www.youtube.com/watch?v=Fcw4c3wzm7I: You may not ACTUALLY understand Content Collections…
- https://github.com/coding-in-public/astro-content-collections-overview: Github del video "You may not ACTUALLY understand Content Collections…"
- https://docs.astro.build/en/guides/styling/#add-tailwind-4: 

## Datos obtenidos:
- Aves: https://github.com/NinjasCL/chileanbirds-dataset/tree/master/data
- Personajes: https://query.wikidata.org

## Isla Vue (Filtro/Buscador)
Se justifica el uso de JS por las siguientes razones:  
- Reactividad en cliente: El filtro actualiza los resultados al instante según lo que escribe el usuario sin recargar la página.
- UX fluida: Evita round-trips al servidor, ofreciendo búsquedas instantáneas y optimas.
- Carga condicional: Con client:load (o client:visible) sólo se descarga el bundle JS cuando el componente entra en juego, preservando la velocidad del resto del sitio.
- Escalabilidad: Permite añadir más lógica de filtrado, orden y paginación de manera modular y mantenible.  
Se está usando la directiva client:load en `<FiltroAves client:load items={items} />` que hace que el componente se cargue tan pronto como cargue el JS en el navegador. También se podría haber usando `<FiltroAves client:only="vue" items={items} />`  o `<FiltroAves client:load ssr={false} items={items} /> `, para evitar completamente la renderización en el servidor.

## Notas extra

- Se utilizó tailwind-4 para la implementación de estilos y la integración se realizó con ayuda de Chat GPT