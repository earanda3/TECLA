# TECLA — Aplicació Web

Benvingut a l'aplicació web de TECLA, un sintetitzador MIDI programable basat en navegador.

## 🚀 Com executar l'aplicació

### Pas 1: Executar el servidor

Fes **doble clic** al fitxer:

```
EXECUTAR_TECLA.command
```

### Pas 2: Permetre l'execució (només la primera vegada)

La primera vegada que executis el fitxer `.command`, macOS mostrarà un avís de seguretat perquè el fitxer no està signat per un desenvolupador verificat.

**Segueix aquests passos:**

1. **Apareixerà un missatge** dient que no es pot obrir el fitxer perquè és d'un desenvolupador no identificat.

2. **Obre Configuració del Sistema** (System Settings / Preferències del Sistema):
   - Fes clic a l'icona  a la barra de menú
   - Selecciona **Configuració del Sistema** (o **Preferències del Sistema** en versions antigues)

3. **Ves a Privacitat i Seguretat**:
   - Al menú lateral, selecciona **Privacitat i Seguretat** (Privacy & Security)
   - Desplaça't cap avall fins a la secció **Seguretat** (Security)

4. **Permet l'execució**:
   - Veuràs un missatge que diu: *"S'ha bloquejat l'ús de 'EXECUTAR_TECLA.command' perquè no és d'un desenvolupador identificat"*
   - Fes clic al botó **Obre igualment** (Open Anyway) o **Permet** (Allow)
   - Confirma amb la teva contrasenya o Touch ID si cal

5. **Torna a executar** el fitxer `EXECUTAR_TECLA.command`

6. Apareixerà un altre diàleg. Fes clic a **Obre** (Open)

Després d'aquest procés inicial, ja no caldrà repetir-lo. El fitxer s'executarà directament amb un doble clic.

### Pas 3: Utilitzar l'aplicació

Un cop executat el servidor:

- S'obrirà automàticament el navegador amb l'aplicació TECLA
- El servidor estarà actiu al port `8080` (o el següent disponible)
- Veuràs una finestra de Terminal amb el missatge: `✓ Servidor TECLA al port 8080`

**Per aturar el servidor:**
- Tanca la finestra del Terminal
- O prem `Ctrl+C` a la finestra del Terminal

## 📋 Requisits

- **macOS** (qualsevol versió recent)
- **Python 3** (ja instal·lat per defecte a macOS)
- **Navegador web modern** (Chrome, Safari, Firefox, Edge)

## 🎹 Funcionalitats

- **Simulador TECLA**: Prova els modes i efectes sense necessitat del dispositiu físic
- **Editor de modes**: Crea i edita modes personalitzats en Python
- **Gestió de firmware**: Instal·la i actualitza el firmware del dispositiu
- **Temes personalitzables**: Crea i desa temes de colors il·limitats
- **Connexió MIDI**: Connecta amb dispositius MIDI externs

## 🔧 Solució de problemes

### El servidor no s'inicia

Si el port 8080 està ocupat, l'script provarà automàticament amb el port 8081, 8082, etc.

### L'aplicació no es carrega al navegador

Obre manualment el navegador i ves a:
```
http://localhost:8080/tecla.html
```

### Problemes amb permisos

Si tens problemes amb permisos, pots executar manualment des del Terminal:

```bash
cd /Users/zen/Desktop/web_TECLA
python3 server.py
```

## 📁 Estructura del projecte

```
web_TECLA/
├── EXECUTAR_TECLA.command    # Script per iniciar el servidor
├── AppIcon.png                # Icona de l'aplicació
├── server.py                  # Servidor HTTP local
├── tecla.html                 # Aplicació web principal
├── js/                        # Mòduls JavaScript
├── py/                        # Modes Python
├── device_files/              # Fitxers del dispositiu
└── firmware/                  # Fitxers de firmware
```

## 💡 Consells

- **Manté el Terminal obert** mentre utilitzes l'aplicació
- **Connecta el dispositiu TECLA** abans d'obrir la pestanya "Tecles" per gestionar modes
- **Desa els teus modes** regularment des de l'editor
- **Crea temes personalitzats** a la pestanya "Aparença"

## 📞 Suport

Per a més informació sobre el projecte TECLA, consulta la documentació del dispositiu.

---

**Versió**: 1.0  
**Última actualització**: Març 2026
