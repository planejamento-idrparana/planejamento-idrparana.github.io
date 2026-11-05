// Dinâmica da apresentação: respostas anônimas em uma tabela isolada do Supabase.
// A chave é pública por natureza; a tabela só aceita ler e inserir (RLS), e cada sessão é um dia.
window.DINAMICA = {
  rest: 'https://ejwzqrrudgweglxkktan.supabase.co/rest/v1/deplan_dinamica_respostas',
  cabecalho: { apikey: 'sb_publishable_yEpBSbKAaJPgxCcQVtWIcg_GsnoxibH' },
  site: 'https://planejamento-idrparana.github.io/',
  hoje: () => new Date().toLocaleDateString('en-CA'), // AAAA-MM-DD no fuso local
};
