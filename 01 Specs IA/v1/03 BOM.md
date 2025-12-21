# Camera Dry Cabinet – Electronics BOM (Brasil / China)
**Arquitetura:** Controle local com fio (primário) + Tuya (monitoramento e override)

Este documento lista **todos os componentes eletrônicos** necessários,
com foco em disponibilidade no **Mercado Livre (Brasil)** e **AliExpress (China)**.

---

## A) Alimentação

### A1. Fonte 12 V DC (Principal)
**Especificação:**
- 12 V
- ≥ 20 A
- Fonte chaveada metálica (tipo LED / CFTV)

**Buscar no Mercado Livre:**
- “Fonte chaveada 12V 20A bivolt”
- “Fonte 12V 20A metálica LED”
- “Fonte 12V 20A CFTV”

**AliExpress:**
- “12V 20A switching power supply metal case”

✔ Genérica é aceitável  
✔ Deve ter ventilação e aterramento

---

### A2. Conversor DC-DC (opcional – 12 V → 5 V)
- Modelo: **LM2596**

Buscar:
- “Conversor DC DC LM2596 12V 5V”

Usado apenas se adicionar sensores ou ESP futuramente.

---

## B) Controle Primário (Local – Autoritativo)

### B1. Controlador de Umidade com Fio
**Modelo recomendado:** **XH-M452**

- Alimentação: 12 V
- Sensor de umidade com fio incluso
- Ajuste de setpoint e histerese
- Saída por relé

**Buscar:**
- Mercado Livre: “Controlador de umidade XH-M452”
- AliExpress: “XH-M452 humidity controller”

✔ Simples  
✔ Confiável  
✔ Funciona sem internet

---

## C) Integração Tuya

### C1. Sensor Tuya de Temperatura / Umidade (Monitoramento)
Função:
- Monitorar RH e temperatura
- Histórico no app
- Alertas

**Buscar (Brasil):**
- “Sensor temperatura umidade Tuya WiFi”
- “Sensor umidade Tuya Smart”

Marcas comuns:
- Moes
- Zemismart
- Positivo Casa Inteligente (rebrand Tuya)

**AliExpress:**
- “Tuya WiFi temperature humidity sensor”
- Versão Zigbee se já houver hub Tuya Zigbee

⚠️ Não usar como controle primário.

---

### C2. Relé Tuya (Override Manual)

#### Opção preferida – DC (12 V)
- Relé Wi-Fi Tuya 12 V

Buscar:
- “Relé WiFi Tuya 12V”
- “Tuya 12V relay module”

Função:
- Desligar/ligar TEC remotamente
- Modo manutenção

---

#### Opção alternativa – AC
- Tomada ou interruptor Wi-Fi Tuya 16 A

Buscar:
- “Tomada WiFi Tuya”
- “Interruptor WiFi Tuya”

⚠️ Desliga todo o sistema (inclusive ventoinhas)

---

## D) Segurança (OBRIGATÓRIA)

### D1. Termostato de Segurança (NC)
- Tipo: **Normalmente Fechado**
- Temperatura de corte: **65–70 °C**
- Modelo típico: **KSD9700**

Buscar:
- “KSD9700 70C NC”
- “Protetor térmico 70 graus normalmente fechado”

Deve ser fixado diretamente no dissipador quente.

---

### D2. Fusíveis e Porta-fusíveis
- Fusível TEC: **15 A**
- Fusível controle/ventoinhas: **3 A**
- Tipo automotivo (lâmina)

Buscar:
- “Porta fusível automotivo”
- “Fusível lâmina 15A”
- “Fusível lâmina 3A”

---

## E) Ventoinhas (NÃO ECONOMIZAR)

### E1. Ventoinhas 120 mm
- **Noctua NF-A12x25 PWM** (2 unidades)
  - Circulação principal
  - Dissipador quente

### E2. Ventoinha 92 mm
- **Noctua NF-A9 PWM** (1 unidade)
  - Placa fria

Mercado Livre:
- Revendedores oficiais

AliExpress:
- Preferir loja oficial Noctua
- Evitar clones

---

## F) Sensores Opcionais

### F1. Sensor de Temperatura do Dissipador
- **DS18B20 impermeável**

Buscar:
- “DS18B20 impermeável”

Usado apenas para monitoramento (não segurança).

---

## G) Cabeamento e Conectores

### Bitolas
- TEC: **AWG 16**
- Ventoinhas: **AWG 20–22**
- Sensores: **AWG 24**

### Conectores recomendados
- **WAGO 221** (distribuição)
- **XT30 / XT60** (linha TEC – opcional)
- **JST-XH** (sensores e ventoinhas – opcional)

---

## H) Genérico vs Crítico

| Item | Pode ser genérico? | Observação |
|----|----|----|
| Fonte 12 V | Sim | Qualidade razoável |
| Controlador XH-M452 | Sim | Muito comum |
| Termostato | Sim | KSD9700 |
| Relé Tuya | Sim | Qualquer compatível |
| Sensor Tuya | Sim | Qualquer Tuya |
| Ventoinhas | ❌ Não | Usar Noctua |
| TEC | Sim | Comprar reserva |
| LM2596 | Sim | Módulo padrão |

---

**FIM DO DOCUMENTO**
