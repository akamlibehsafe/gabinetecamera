# Roteiro de Execução – Camera Dry Cabinet
Projeto: Gabinete Expositivo com Controle Ativo de Umidade (TEC)

Este roteiro descreve a execução do projeto em fases,
com foco em reduzir riscos, validar cedo e evoluir até a entrega final.

---

## VISÃO GERAL DAS FASES

1. Planejamento & Preparação
2. MVP Técnico (bancada)
3. MVP Integrado (gabinete simples)
4. Gabinete Final (marcenaria definitiva)
5. Integração Final & Ajustes
6. Entrega Final & Operação

---

## 1️⃣ FASE 1 – Planejamento & Preparação

🎯 Objetivo  
Garantir que todas as decisões estão consolidadas antes de comprar e construir.

### Atividades
- ☐ Revisar:
  - Master Project Spec
  - Wiring Spec
  - BOM
  - Checklist de Compra
- ☐ Validar espaço físico disponível na parede
- ☐ Alinhar expectativas com o marceneiro
- ☐ Definir cronograma aproximado
- ☐ Criar pasta do projeto (estrutura recomendada)

### Entregáveis
- ✔ Projeto fechado
- ✔ Lista de compras validada
- ✔ Arquitetura final congelada

---

## 2️⃣ FASE 2 – MVP TÉCNICO (BANCADA)

🎯 Objetivo  
Validar o **coração do sistema** antes de qualquer marcenaria definitiva.

👉 Esta é a fase mais importante para reduzir riscos.

### Escopo do MVP
- TEC + placa fria
- Espalhador + dissipador Noctua
- Ventoinhas
- Controlador XH-M452
- Termostato de segurança
- Fonte 12 V
- Sensor Tuya (monitoramento)

### Atividades
- ☐ Montar o stack térmico em bancada
- ☐ Ajustar pressão do clamp
- ☐ Verificar sentido térmico do TEC
- ☐ Testar ventilação da câmara quente
- ☐ Simular ambiente úmido (banheiro / dia chuvoso)
- ☐ Confirmar formação de condensação
- ☐ Testar desligamento por temperatura
- ☐ Medir consumo elétrico
- ☐ Ajustar RPMs para silêncio

### Critérios de Sucesso (Go / No-Go)
- ✔ Condensa água de forma estável
- ✔ Dissipador não superaquece
- ✔ Sistema silencioso
- ✔ Controle de RH responde corretamente

---

## 3️⃣ FASE 3 – MVP INTEGRADO (GABINETE SIMPLES)

🎯 Objetivo  
Validar **fluxo de ar, drenagem e controle de umidade em volume real**,
sem investir ainda na marcenaria final.

### Escopo
- Caixa simples (MDF cru ou compensado)
- Volume aproximado da câmara final
- Uma única porta simples (vedada provisoriamente)

### Atividades
- ☐ Instalar conjunto TEC em uma lateral
- ☐ Implementar calha e evaporação
- ☐ Instalar ventoinhas conforme projeto
- ☐ Selar juntas de forma provisória
- ☐ Rodar sistema por 48–72 h
- ☐ Abrir porta algumas vezes
- ☐ Medir tempo de recuperação do RH

### Critérios de Sucesso
- ✔ RH atinge 40–45%
- ✔ Recuperação após abertura < aceitável
- ✔ Sem condensação fora da placa fria
- ✔ Sistema estável por dias

👉 Se algo precisar mudar, **é aqui**.

---

## 4️⃣ FASE 4 – GABINETE FINAL (MARCENARIA)

🎯 Objetivo  
Construir o móvel definitivo com base em um sistema já validado.

### Atividades (Marcenaria)
- ☐ Construção dos painéis externos (MDF 18 mm)
- ☐ Construção da caixa interna (Ultra MDF)
- ☐ Pintura PU automotiva interna
- ☐ Vedação completa com silicone
- ☐ Execução das paredes Wall A e Wall B
- ☐ Preparação das caixas técnicas
- ☐ Instalação da porta de vidro
- ☐ Instalação da gaxeta
- ☐ Fixação na parede

### Entregáveis
- ✔ Gabinete esteticamente final
- ✔ Volume interno estanque
- ✔ Acessos técnicos funcionais

---

## 5️⃣ FASE 5 – INTEGRAÇÃO FINAL & AJUSTES

🎯 Objetivo  
Integrar eletrônica + gabinete definitivo e otimizar o sistema.

### Atividades
- ☐ Instalar stack térmico definitivo
- ☐ Fixar suportes e prateleiras
- ☐ Instalar ventoinhas definitivas
- ☐ Organizar cabeamento
- ☐ Revisar fusíveis e proteções
- ☐ Ajustar setpoint e histerese
- ☐ Integrar totalmente com Tuya
- ☐ Teste de ruído noturno
- ☐ Teste de uso real (abrir / fechar)

---

## 6️⃣ FASE 6 – ENTREGA FINAL & OPERAÇÃO

🎯 Objetivo  
Colocar o sistema em operação contínua com segurança.

### Atividades
- ☐ Executar checklist de comissionamento completo
- ☐ Documentar ajustes finais
- ☐ Registrar valores típicos de operação
- ☐ Fotografar instalação final
- ☐ Criar rotina de inspeção semestral

### Estado Final
- ✔ Sistema estável
- ✔ RH controlado
- ✔ Baixo ruído
- ✔ Integração smart ativa
- ✔ Pronto para anos de uso

---

## 7️⃣ Evoluções Futuras (Opcional)

- Segundo TEC (se necessário)
- Monitoramento avançado (ESP / Home Assistant)
- Registro histórico local
- Iluminação interna controlada
- Alarme de porta aberta

---

**FIM DO ROTEIRO DE EXECUÇÃO**
