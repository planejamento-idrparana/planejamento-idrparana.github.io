// Conteúdo do ecossistema DEPLAN. Para adicionar um item, inclua um objeto em `itens`.
// { nome, descricao, url, tag }
window.ECOSSISTEMA = [
  {
    id: 'realidade-rural', titulo: 'Realidade Rural',
    sub: 'Retratos do campo paranaense: produção, território e pessoas.',
    itens: [
      {
        nome: 'Datageo Paraná', url: 'https://datageoparana.github.io', tag: 'Plataforma pública',
        descricao: '10 painéis interativos sobre preços, produção, crédito rural, comércio exterior, emprego e demografia, com dados oficiais (DERAL/SEAB, BCB, MDIC, IBGE).',
      },
      {
        nome: 'DGP-Comando', url: 'https://dgp-comando.github.io', tag: 'Sala de Situação',
        descricao: 'Sala de Situação do Paraná: mapa e globo com mais de 80 camadas de dados dos 399 municípios.',
      },
    ],
  },
  {
    id: 'monitoramento', titulo: 'Monitoramento e Relatórios',
    sub: 'Acompanhamento das ações e resultados do Instituto.',
    itens: [],
  },
  {
    id: 'planejamento', titulo: 'Planejamento',
    sub: 'Programas, metas e instrumentos de gestão estratégica.',
    itens: [
      {
        nome: 'Rede Paranaense de ATER', url: 'https://rededeaterparana.github.io', tag: 'Rede estadual',
        descricao: 'Rede de entidades de Assistência Técnica e Extensão Rural do Paraná, com cadastro de adesão e mapa da capacidade instalada.',
      },
      {
        nome: 'Arranjos Regionais 2027', url: 'https://arranjos-regionais-idr.github.io', tag: 'Acesso restrito',
        descricao: 'Montagem dos arranjos regionais de 2027: cada regional combina cadeias produtivas, áreas transversais, público, municípios e equipe, com acesso por código da DEPLAN.',
      },
    ],
  },
  {
    id: 'ferramentas', titulo: 'Ferramentas e Instrumentos Técnicos',
    sub: 'Aplicativos, bases e métodos de apoio ao trabalho técnico.',
    itens: [
      {
        nome: 'GETEC', url: 'http://www.idrgetec.idr.pr.gov.br', tag: 'Sistema institucional',
        descricao: 'Sistema de Gestão Técnica do IDR-Paraná, para registro e acompanhamento das atividades técnicas.',
      },
      // SAFE (Sistema Administrativo e Financeiro): entra quando houver URL.
    ],
  },
];
