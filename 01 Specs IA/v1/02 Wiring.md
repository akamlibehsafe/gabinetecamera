# Camera Dry Cabinet – Wiring & Electrical Specification
**Arquitetura FINAL – Controle Local + Tuya (monitoramento/override)**

Este documento descreve toda a lógica elétrica e de controle do gabinete,
incluindo proteções obrigatórias e hierarquia de autoridade.

---

## 1. Visão Geral Elétrica

- Tensão principal do sistema: **12 V DC**
- Fonte recomendada: **12 V / 20 A**
- Derivação opcional de **5 V** via conversor DC-DC (sensores, ESP futuro)

---

## 2. Distribuição de Energia

### Caminho principal
Rede AC
→ Fonte 12 V DC
→ Chave geral DC
→ Bloco de fusíveis
→ Cargas


### Ramificações com fusível
- **Linha TEC:** fusível **15 A**
- **Linha controle + ventoinhas:** fusível **3 A**

---

## 3. Cadeia de Segurança do TEC (OBRIGATÓRIA)

O TEC **sempre** deve estar ligado em série pelos seguintes elementos:

+12 V
→ Fusível 15 A
→ Termostato NC 65–70 °C (no dissipador)
→ Saída do controlador de umidade local
→ Relé Tuya (override manual – opcional)
→ TEC +
→ TEC –
→ GND (0 V)


### Importante
- O termostato NC tem **prioridade absoluta**
- Mesmo que:
  - o controlador falhe
  - o Tuya falhe
  - o Wi-Fi caia  
  👉 o TEC será desligado por segurança

---

## 4. Ventoinhas (Opção B – Final)

### Sempre ligadas
- Ventoinha principal da câmara:
  - Noctua NF-A12x25 (120 mm)
- Ventoinha do dissipador quente:
  - Noctua NF-A12x25 (120 mm)

Essas podem ser ligadas diretamente após o fusível de 3 A.

---

### Ligada junto com o TEC
- Ventoinha da placa fria:
  - Noctua NF-A9 (92 mm)

Implementação recomendada:
- Alimentar a NF-A9 a partir do **mesmo ponto comutado do TEC**
- Assim ela:
  - nunca liga sem o TEC
  - nunca fica soprando ar sem condensação

---

## 5. Controle Primário – Controlador com Fio

- Modelo recomendado: **XH-M452**
- Alimentação: 12 V
- Sensor: sonda de umidade com fio

Configuração típica:
- Setpoint: **45% RH**
- Histerese: **3–5%**

Função:
- Decide localmente quando ligar/desligar o TEC
- Funciona sem internet

---

## 6. Integração Tuya

### Sensores Tuya
- Sensor de temperatura/umidade Tuya
- Função: **monitoramento, histórico, alertas**
- Não controla o TEC diretamente

### Relé Tuya (opcional, recomendado)
- Relé Wi-Fi Tuya 12 V
- Inserido **após** o controlador local
- Função:
  - desligar o TEC remotamente
  - modo manutenção
  - override manual

⚠️ Nunca usar Tuya como controle primário de umidade.

---

## 7. Bitolas e Conexões

### Bitolas recomendadas
- TEC: **AWG 16**
- Ventoinhas: **AWG 20–22**
- Sensores: **AWG 24**

### Conectores
- WAGO 221 (distribuição)
- XT30 / XT60 (linha TEC – opcional)
- JST-XH (ventoinhas e sensores – opcional)

---

## 8. Aterramento

- Carcaça metálica da fonte: **ligada ao terra AC**
- GND DC comum a todo o sistema

---

## 9. Boas Práticas

- Separar fisicamente cabos de potência (TEC) de sensores
- Usar termo-retrátil em todas as emendas
- Identificar fios (etiquetas)

---

**FIM DO DOCUMENTO**
