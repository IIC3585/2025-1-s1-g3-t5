<script>
  export let chatbotlink;
  let isOpen = false;
  let isLoaded = false;

  function toggleChat() {
    isOpen = !isOpen;
    if (isOpen && !isLoaded) {
      isLoaded = true;
    }
  }
</script>
<button
  on:click={toggleChat}
  class="fixed bottom-6 right-6 bg-blue-600 text-white p-4 rounded-full shadow-lg hover:bg-blue-700 transition-colors z-50"
  aria-label={isOpen ? 'Cerrar chat' : 'Abrir chat'}
>
  {isOpen ? '✕' : '💬'}
</button>

{#if isOpen}
  <div class="fixed bottom-24 right-6 w-[380px] h-[80%] bg-white rounded-lg shadow-xl overflow-hidden z-40">
    {#if isLoaded}
      <iframe
        src={chatbotlink}
        title="Asistente virtual de Chatbase"
        allow="microphone"
        class="w-full h-full border-none"
        sandbox="allow-scripts allow-same-origin"
      ></iframe>
    {:else}
      <div class="flex items-center justify-center h-full bg-gray-100">
        <p>Cargando chat...</p>
      </div>
    {/if}
  </div>
{/if}

<style>
  iframe {
    transition: opacity 0.3s ease;
  }
</style>