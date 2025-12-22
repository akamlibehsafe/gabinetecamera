# Camera Dry Cabinet – Checklist de Comissionamento & Ajuste
**Objetivo:** garantir segurança, funcionamento correto, silêncio e estabilidade
do controle de umidade antes do uso contínuo com as câmeras.

Este checklist deve ser seguido **na ordem**.

---

## 1. Verificações Mecânicas (ANTES DE LIGAR)

☐ Pintura PU do Ultra MDF totalmente curada (sem cheiro)  
☐ Todas as juntas internas seladas com silicone  
☐ Nenhum MDF cru exposto internamente  
☐ Gaxeta da porta contínua, sem emendas abertas  
☐ Porta fecha com compressão uniforme da gaxeta  

### Placa fria e condensado
☐ Placa fria bem vedada na Wall B (espuma contínua)  
☐ Nenhum ponto onde água possa escorrer para MDF  
☐ Calha posicionada exatamente sob a placa fria  
☐ Caminho de drenagem contínuo até a câmara quente  

### Dissipador e clamp
☐ Dissipador quente apoiado em suporte/prateleira  
☐ Peso NÃO apoiado na placa fria nem no MDF  
☐ Hastes roscadas alinhadas  
☐ Molas comprimidas de forma uniforme  
☐ Nada encostando nas pás das ventoinhas  

---

## 2. Verificações Elétricas (SEM TEC ATIVO)

☐ Fonte ligada ao terra AC  
☐ Tensão da fonte entre 12,0 e 12,5 V  
☐ Fusível TEC: 15 A  
☐ Fusível controle: 3 A  
☐ Termostato NC instalado fisicamente no dissipador  
☐ Cadeia do TEC em série (fusível → termostato → controlador → Tuya → TEC)  
☐ Polaridade do TEC conferida (lado frio para a câmara das câmeras)  

---

## 3. Primeiro Power-On (SOMENTE VENTOINHAS)

☐ Chave geral ligada  
☐ Ventoinha principal (120 mm esquerda) girando  
☐ Ventoinha do dissipador quente girando  
☐ Ventoinha da placa fria DESLIGADA  
☐ Nenhum ruído mecânico, vibração ou zumbido  

👉 Se houver ruído:  
- reduzir RPM  
- conferir fixações  
- checar se cabos encostam nas hélices  

---

## 4. Teste do TEC (CURTO E MONITORADO)

☐ Ativar TEC manualmente (ou ajustar setpoint temporariamente)  
☐ Placa fria começa a esfriar em 30–60 s  
☐ Ventoinha da placa fria liga junto com o TEC  
☐ Dissipador quente começa a aquecer gradualmente  

Monitorar:
☐ Dissipador NÃO aquece rapidamente demais  
☐ Termostato de segurança NÃO dispara  

Se aquecer rápido:
- revisar contato térmico
- revisar pasta térmica
- revisar ventilação da câmara quente

---

## 5. Teste de Condensação e Drenagem

Em dia úmido ou após abrir a porta:

☐ Formação visível de gotículas na placa fria  
☐ Gotas caem na calha (não para fora)  
☐ Água chega à bandeja de evaporação  
☐ Nenhuma gota em paredes de MDF  

---

## 6. Ajuste de Umidade (TUNING)

Configurar controlador local:
- Setpoint: **45% RH**
- Histerese: **3–5%**

☐ Deixar sistema rodar 6–24 h (primeira secagem)  
☐ RH desce gradualmente até o setpoint  
☐ TEC desliga ao atingir o valor  
☐ Sistema cicla de forma estável  

---

## 7. Teste de Recuperação (Abertura da Porta)

☐ Abrir a porta por 1–2 minutos  
☐ Fechar porta  
☐ Observar subida temporária de RH  
☐ Verificar retorno ao setpoint em tempo razoável  
☐ Sem oscilação excessiva do TEC  

---

## 8. Integração Tuya

☐ Sensor Tuya instalado longe da placa fria  
☐ Valores coerentes com controlador local (diferença ≤2–3%)  
☐ Histórico visível no app  
☐ Alertas configurados (ex: RH > 50%)  

### Relé Tuya (se instalado)
☐ Desligamento remoto do TEC funciona  
☐ Religar sistema funciona  
☐ Termostato de segurança mantém prioridade  

---

## 9. Critérios de Aceitação Final

☐ RH estável entre 40–45%  
☐ Nenhum vazamento de água  
☐ Sistema silencioso para ambiente residencial  
☐ Segurança térmica funcional  
☐ Tuya monitora corretamente  

---

**SISTEMA APROVADO PARA USO CONTÍNUO**
