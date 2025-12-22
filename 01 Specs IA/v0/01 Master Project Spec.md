# Camera Display Dry Cabinet – Complete Project Specification
**TEC-Based Dehumidified Display Cabinet**  
**Project Status: FINALIZED / READY FOR EXECUTION**

Este documento é a **fonte única da verdade** do projeto.
Ele consolida arquitetura, dimensões, marcenaria, sistema de desumidificação,
fluxo de ar, controle, segurança e integração Tuya.

---

## 0. Visão Geral do Projeto

Gabinete expositivo de alto padrão para câmeras fotográficas, com controle ativo
de umidade via módulo termoelétrico (Peltier / TEC), projetado para ambiente
residencial silencioso.

Arquitetura de controle:
- **Controle local com fio = autoridade**
- **Tuya = monitoramento, alertas e override manual**

O sistema funciona de forma segura **mesmo sem internet**.

---

## 1. Objetivos de Projeto

- Preservar ~35 câmeras (SLR, DSLR, rangefinder, vintage)
- Local: **Campinas–SP (clima úmido)**
- Umidade alvo interna: **40–45% RH**
- Operação silenciosa (sala de estar)
- Gabinete interno praticamente estanque
- Baixa manutenção (sem sílica)
- Seguro, estável e expansível

---

## 2. Dimensões Externas

- **Largura:** 2200 mm  
- **Profundidade:** 300 mm  
- **Altura:** 600 mm  

Fixado em parede, formato horizontal.

### Divisão interna (esquerda → direita)
- Caixa técnica esquerda: **220 mm**
- Câmara das câmeras: **1760 mm**
- Caixa técnica direita: **220 mm**

---

## 3. Construção do Gabinete

### 3.1 Painéis Externos
- MDF padrão **18 mm**
- Acabamento amadeirado (tom escuro)
- Função estrutural e estética

### 3.2 Caixa Interna Selada
- Ultra MDF
- Pintura **PU automotiva**
- Todas as juntas seladas com **silicone**

### 3.3 Estratégia
- Dupla camada:
  - Externa = móvel
  - Interna = volume técnico estanque
- Caixa interna recuada para porta ficar flush

---

## 4. Porta

- Vidro único
- Abertura para cima
- Pistões hidráulicos
- Moldura de alumínio
- **Gaxeta contínua de borracha/silicone**
- Vedação contra a face frontal do Ultra MDF

Uso:
- Fechada a maior parte do tempo
- Aberturas curtas e esporádicas

---

## 5. Layout Interno

- Prateleira de vidro (duas fileiras de câmeras)
- **Folga frontal de 3–5 cm** até o vidro
- Ajuda na equalização vertical do ar

---

## 6. Princípio de Desumidificação

- Ar interno circula continuamente
- Ar úmido entra em contato com **placa fria de cobre vertical**
- Umidade condensa
- Água escorre para calha
- Água evaporada na câmara quente
- Calor dissipado para o ambiente

❗ Não há entrada de ar externo na câmara das câmeras.

---

## 7. Caixa Técnica Direita (Desumidificador)

### Wall B (estrutural)
- Separa câmara das câmeras da câmara quente
- Abertura apenas para passagem da placa fria
- Vedação com espuma
- **Não recebe carga mecânica**

### Wall A (cosmética)
- Recuada **25–35 mm**
- Fenda vertical **10–15 mm**
- Esconde placa fria, espuma, calha e ventoinha

### Ventilação da Câmara Quente
- Fenda lateral externa
- Defletor interno (baffle)
- Entrada inferior / saída superior de ar

---

## 8. Hardware Térmico

### 8.1 TEC
- **TEC1-12706**
- 12 V / ~6 A
- 1 unidade instalada
- Espaço para 2ª unidade futura

### 8.2 Placa Fria
- Cobre ~100 × 140 × 8 mm
- Vertical, meia-altura
- Face lisa exposta às câmeras
- Vedada à Wall B com espuma

### 8.3 Espalhador Quente
- Alumínio 50 × 50 × 6 mm

### 8.4 Dissipador Quente
- **Noctua NH-U12S**
- Base plana contra espalhador
- Torre vertical
- Ventilador soprando para a saída lateral
- Peso apoiado em prateleira/suporte

---

## 9. Sistema de Aperto (Clamp)

- 4 hastes roscadas inox (M4 ou M5)
- Molas de compressão
- Arruelas + porcas travantes

Função:
- Pressão uniforme:
  **placa fria → TEC → espalhador → dissipador**

Regras:
- MDF não recebe carga
- Parafusos não rosqueiam no dissipador
- Suporte separado sustenta o peso

---

## 10. Fluxo de Ar – OPÇÃO FINAL (B)

### Ventoinha principal
- **Noctua NF-A12x25 – 120 mm**
- Inferior esquerda
- Fluxo esquerda → direita
- Sempre ligada (~300–500 RPM)

### Ventoinha da placa fria
- **Noctua NF-A9 – 92 mm**
- Inferior direita
- Fluxo de baixo para cima
- Ligada somente quando o TEC está ativo

---

## 11. Elétrica

- Sistema **12 V DC**
- Fonte recomendada: **12 V / 20 A**
- Proteções obrigatórias:
  - Fusível TEC: 15 A
  - Fusível controle: 3 A
  - Termostato NC 65–70 °C no dissipador

---

## 12. Controle & Tuya

### Controle primário (local)
- **XH-M452** com sensor com fio
- Setpoint: 45% RH
- Histerese: 3–5%

### Tuya (secundário)
- Sensor Tuya T/UR
- Relé Tuya para override manual

Hierarquia:
1. Termostato de segurança
2. Controlador local
3. Tuya

---

## 13. Condensado

- Calha sob a placa fria
- Dreno para câmara quente
- Bandeja + pavio
- Evaporação passiva com ar quente

---

## 14. Capacidade

- Aumento de volume (~+22%) já considerado
- 1 TEC suficiente para gabinete bem vedado
- Caixa esquerda permite expansão futura

---

## 15. Status

✔ Projeto fechado  
✔ Componentes definidos  
✔ Pronto para compra, marcenaria e montagem  

---

**FIM DO DOCUMENTO**
