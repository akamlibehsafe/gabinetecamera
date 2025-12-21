# Camera Dry Cabinet – Projeto Completo

V1
- Hot chamber cooling: Noctua NH-U12S
- 1 Glass Shelf

Gabinete expositivo de alto padrão para câmeras fotográficas, com controle ativo
de umidade via módulo termoelétrico (Peltier / TEC), projetado para uso residencial
silencioso e preservação de longo prazo.

Este repositório/documentação contém **todas as especificações técnicas,
construtivas e elétricas** necessárias para fabricar, montar, comissionar e
manter o sistema.

---

## 🎯 Objetivo do Projeto

- Preservar ~35 câmeras (SLR, DSLR, rangefinder, vintage)
- Ambiente: sala de estar (baixo ruído)
- Local: Campinas–SP (clima úmido)
- Umidade alvo: **40–45% RH**
- Sistema:
  - ativo (sem sílica)
  - silencioso
  - seguro
  - expansível
- Integração com **Tuya** para monitoramento e alertas

---

## 🧠 Arquitetura de Controle (Resumo)

- **Controle primário:**  
  Controlador de umidade com fio (local, autoritativo)

- **Segurança absoluta:**  
  Termostato NC no dissipador quente (65–70 °C)

- **Integração smart:**  
  Tuya (monitoramento + override manual)

> O sistema funciona corretamente **mesmo sem internet**.

---

## 📁 Estrutura Recomendada de Pastas

Camera-Dry-Cabinet/
│
├── README.md
│
├── 00_MASTER/
│ └── ForteGB-Camera-Dry-Cabinet-Project-Spec.md
│
├── 01_ELECTRICAL/
│ ├── camera-dry-cabinet-wiring.md
│ └── camera-dry-cabinet-electronics-bom.md
│
├── 02_COMMISSIONING/
│ └── camera-dry-cabinet-commissioning.md
│
├── 03_BUILDER/
│ └── camera-dry-cabinet-builder-brief.md
│
└── 99_NOTES/
└── sketches, links, testes, fornecedores.txt



---

## 📄 Descrição dos Documentos

### 🔹 00_MASTER  
**ForteGB-Camera-Dry-Cabinet-Project-Spec.md**  
Documento principal do projeto.  
Contém:
- conceito geral
- dimensões
- marcenaria
- sistema térmico
- fluxo de ar
- controle
- segurança
- decisões finais de engenharia

👉 **Sempre leia este primeiro.**

---

### 🔹 01_ELECTRICAL  

**camera-dry-cabinet-wiring.md**  
- Arquitetura elétrica
- Cadeia de segurança do TEC
- Lógica de controle
- Integração Tuya

**camera-dry-cabinet-electronics-bom.md**  
- Lista de compras eletrônicas
- Componentes compatíveis com:
  - Mercado Livre (Brasil)
  - AliExpress (China)
- Indicação do que pode ser genérico e do que é crítico

---

### 🔹 02_COMMISSIONING  

**camera-dry-cabinet-commissioning.md**  
- Checklist completo de:
  - verificação mecânica
  - elétrica
  - testes de condensação
  - ajuste de umidade
  - validação final

👉 Deve ser seguido **antes de colocar as câmeras**.

---

### 🔹 03_BUILDER  

**camera-dry-cabinet-builder-brief.md**  
- Documento exclusivo para a marcenaria
- Materiais
- Dimensões
- Aberturas
- Restrições
- O que NÃO pode ser alterado

👉 Seguro para enviar ao marceneiro sem confundir com eletrônica.

---

## 🛠️ Fluxo Recomendado de Execução

1. Ler o **Master Project Spec**
2. Comprar componentes eletrônicos
3. Montar e testar o conjunto térmico em bancada
4. Fabricar o gabinete
5. Integrar eletrônica e ventilação
6. Executar o checklist de comissionamento
7. Ajustar RH
8. Colocar as câmeras

---

## 🔒 Princípios Importantes do Projeto

- Segurança térmica nunca depende de software ou internet
- Nenhuma carga mecânica deve ser aplicada no MDF via componentes
- Ventilação da câmara quente é independente da câmara das câmeras
- Ventoinhas são críticas para silêncio (usar Noctua)
- Projeto prevê expansão futura sem retrabalho estrutural

---

## 📌 Estado do Projeto

✔ Arquitetura definida  
✔ Especificações fechadas  
✔ Componentes especificados  
✔ Pronto para execução  

---

## 📝 Notas Finais

Este projeto foi documentado de forma intencionalmente detalhada para permitir:
- manutenção futura
- handoff para outros técnicos ou agentes de IA
- evolução sem perda de contexto

---

**FIM DO README**


