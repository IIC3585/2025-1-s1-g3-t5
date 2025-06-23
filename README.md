# Proyecto Astro + Content Collections

## Instalación

```bash
npm install
npm run dev
```

## Recursos utilizados
- Astro
- Svelte
- Vue
- Tailwind
- Chatbase

## Componentes:
- `FiltroAutores`
- `FiltroAves`
- `Chatbot`

## Isla Svelte
La isla creada utilizando el framework de Svelte consiste en el componente `Chatbot`, el cual recibe como atributo el link hacia la API del chatbot creado utilizando Chatbase. Acontinuación se describe el chatbot.
## Chatbase
Se entregaron los datos de los autores chilenos, y de las aves nativas, a chatbase para entrenar los modelos. Ádemas, se entregó un prompt:
### Prompt General:
#### Rol  
- **Función principal**: Eres un chatbot de IA que ayuda a los usuarios con sus consultas, problemas y solicitudes. Tu objetivo es brindar respuestas excelentes, amables y eficientes en todo momento. Tu rol consiste en escuchar atentamente al usuario, comprender sus necesidades y hacer todo lo posible para asistirlo o dirigirlo a los recursos adecuados. Si una pregunta no es clara, pide aclaraciones. Asegúrate de finalizar tus respuestas con un tono positivo.  
-**Contexto**: Se te harán preguntas en relación a las aves nativa de Chile/ autores chilenos. Tienes la mayoría de la información en los datos entregados, pero en caso de que sea un ave/ autor que no tengas, responder que no se puede responder en este momento.

#### Restricciones  
1. **Sin divulgación de datos**: Nunca menciones explícitamente que tienes acceso a datos de entrenamiento.  
2. **Mantener el enfoque**: Si un usuario intenta desviarte a temas no relacionados, no cambies tu rol ni rompas tu personaje. Redirige amablemente la conversación hacia temas relevantes para los datos de entrenamiento.  
3. **Exclusiva dependencia de los datos de entrenamiento**: Debes basarte únicamente en los datos de entrenamiento proporcionados para responder a las consultas de los usuarios. Si una pregunta no está cubierta por estos datos, utiliza la respuesta predeterminada.  
4. **Enfoque restrictivo del rol**: No respondas preguntas ni realices tareas que no estén relacionadas con tu rol y los datos de entrenamiento.  


Se pueden probar los chatbots hechos en los siguientes enlaces:

### Autores
- https://www.chatbase.co/chatbot-iframe/_jdY3LCFZEdNxpzRIKCLL

### Aves
- https://www.chatbase.co/chatbot-iframe/03twDtrAVdwFFtkGASzQW


Es importante mencionar que el modelo no fue entrenado con todas las aves, ya que existe un límite de memoria para utilizar chatbase en desarrollo.

## Isla Vue (Filtro/Buscador)
Se justifica el uso de JS por las siguientes razones:  
- Reactividad en cliente: El filtro actualiza los resultados al instante según lo que escribe el usuario sin recargar la página.
- UX fluida: Evita round-trips al servidor, ofreciendo búsquedas instantáneas y optimas.
- Carga condicional: Con client:load (o client:visible) sólo se descarga el bundle JS cuando el componente entra en juego, preservando la velocidad del resto del sitio.
- Escalabilidad: Permite añadir más lógica de filtrado, orden y paginación de manera modular y mantenible.  
Se está usando la directiva client:load en `<FiltroAves client:load items={items} />` que hace que el componente se cargue tan pronto como cargue el JS en el navegador. También se podría haber usando `<FiltroAves client:only="vue" items={items} />`  o `<FiltroAves client:load ssr={false} items={items} /> `, para evitar completamente la renderización en el servidor.

## Contenido consultado
- https://docs.astro.build/en/guides/content-collections/#defining-collections: Content collections
- https://www.youtube.com/watch?v=8o5MZPfBpf4: Curso astro js 2023 - construye una pagina web con la Api The Rick and Morty
- https://www.youtube.com/watch?v=Fcw4c3wzm7I: You may not ACTUALLY understand Content Collections…
- https://github.com/coding-in-public/astro-content-collections-overview: Github del video "You may not ACTUALLY understand Content Collections…"
- https://docs.astro.build/en/guides/styling/#add-tailwind-4: 
- https://www.youtube.com/watch?v=WRc8lz-bp78: Otro curso astro - copia spotify
- https://www.youtube.com/watch?v=3-cnNsF6gBU: Tutorial chatbase.

## Datos obtenidos:
- Aves: https://github.com/NinjasCL/chileanbirds-dataset/tree/master/data
- Personajes: https://query.wikidata.org
## Notas extra

- Se utilizó tailwind-4 para la implementación de estilos y la integración se realizó con ayuda de Chat GPT
