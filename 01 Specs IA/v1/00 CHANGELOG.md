# Changelog – Camera Dry Cabinet Project

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue um padrão inspirado em *Keep a Changelog*,
adaptado para projetos de engenharia e produto físico.

---

## [1.0.0] – Projeto Fechado / Pronto para Execução
**Data:** 2025-12-16

### Adicionado
- Especificação completa do gabinete expositivo com controle ativo de umidade
- Arquitetura de desumidificação por módulo termoelétrico (TEC / Peltier)
- Projeto de gabinete com:
  - dimensões externas 2200 × 300 × 600 mm
  - dupla camada (MDF externo + Ultra MDF interno)
  - pintura PU automotiva interna
  - vedação com silicone
- Porta única em vidro:
  - abertura superior
  - pistões hidráulicos
  - moldura de alumínio
  - gaxeta contínua
- Divisão interna em três zonas:
  - caixa técnica esquerda (expansão futura)
  - câmara das câmeras
  - caixa técnica direita (desumidificador)
- Sistema térmico:
  - TEC1-12706
  - placa fria de cobre vertical
  - espalhador de alumínio
  - dissipador Noctua NH-U12S
- Sistema de clamp com hastes inox e molas
- Tratamento completo de condensado:
  - calha
  - drenagem
  - evaporação na câmara quente
- Arquitetura de fluxo de ar (Opção B):
  - ventoinha principal 120 mm (circulação)
  - ventoinha dedicada 92 mm (lavagem da placa fria)
- Ventilação lateral da câmara quente com defletor interno
- Sistema elétrico em 12 V DC
- Proteções obrigatórias:
  - fusíveis independentes
  - termostato NC 65–70 °C no dissipador
- Controle primário local com fio:
  - controlador XH-M452
  - sonda de umidade interna
- Integração Tuya:
  - sensor de temperatura/umidade (monitoramento)
  - relé Tuya (override manual)
- Documentação completa:
  - Master Project Spec
  - Wiring & Electrical Spec
  - Electronics BOM (Brasil / China)
  - Commissioning Checklist
  - Builder / Cabinet Maker Brief
  - README.md

### Alterado
- Largura do gabinete aumentada de 1800 mm para **2200 mm**
- Volume interno recalculado (+22%)
- Caixa técnica definida com largura fixa de **220 mm** em ambos os lados
- Dissipador quente final escolhido como **Noctua NH-U12S**
- Arquitetura de controle consolidada como:
  - local (autoridade)
  - Tuya apenas para supervisão/override

### Decisões Consolidadas
- Tuya **não** é controle primário
- Segurança térmica nunca depende de software ou cloud
- Nenhuma carga mecânica aplicada ao MDF
- Ventoinhas Noctua são componentes críticos
- Projeto prevê expansão futura sem retrabalho estrutural

---

## [0.9.x] – Fase de Concepção e Exploração
*(Histórico não versionado – fase de discussão e iteração)*

- Comparação de métodos de desumidificação
- Estudo de módulos TEC vs soluções prontas
- Definição de layout interno e fluxo de ar
- Avaliação de dissipadores e ventoinhas
- Integração com Tuya definida como secundária
- Iterações sobre estética vs funcionalidade
- Consolidação da estratégia de clamp térmico

---

## Próximas Versões (Planejadas)

### [1.1.0] – Execução / Build
- Fotos do build
- Ajustes finos de RPM e histerese
- Tempo real de recuperação de RH
- Notas de instalação na parede

### [1.2.0] – Otimizações
- Avaliação da necessidade de segundo TEC
- Otimização de consumo energético
- Ajustes de ruído (se necessário)

---

**Fim do Changelog**
